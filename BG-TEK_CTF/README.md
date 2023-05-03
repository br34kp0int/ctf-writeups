# BG-TEK CTF Çözümleri

Teknofest İstanbul'da gerçekleştirilen mini ctf yarışmasının çözümlerini paylaşacağım.

## Web

### İyi Aile Robotu

	http://ctf.bg-tek.net:8087/

Sayfayı açtığımızda karşımıza bir gif çıkıyor fakat burada ilginç bir şey göremiyoruz. Kaynak kodlarını inceleyelim.

![Robots](https://s2.loli.net/2023/04/30/oFZxIlCj7J6A4Kc.png)

Yorum bize robots.txt'yi işaret ediyor. http://ctf.bg-tek.net:8087/robots.txt adresine gidelim.

![robots.txt](https://s2.loli.net/2023/04/30/ZWXbUSeF6vqIPHG.png)

Görünen o ki mevcut bir admin panelimiz var. http://ctf.bg-tek.net:8087/adminpanel/ bizi login sayfasına yönlendiriyor.

![login1](https://s2.loli.net/2023/04/30/aeVbSRunQdyXmHv.png)

Burada sql injection denemesi yapıyoruz. OR ifadesinin filtrelendiğini görüyoruz. OR yerine OORR ifadesini kullanıyoruz.

![flag](https://s2.loli.net/2023/04/30/5Ah9uG62SQHINLi.png)

Başarılı bir şekilde filtrelemeyi bypass edebildiğimizi görüyoruz. Daha güçlü bir filteleme uygulanabilirmiş.

	BG-TEK{B4BÜR_WILL_R3TURN}


### I came I saw I conquered

	flag.php içinde senin için bir mesaj var. 
	http://ctf.bg-tek.net:8090/

Bu soruda karşımıza bir SMS uygulaması geliyor.

![page](https://s2.loli.net/2023/04/30/DCW3JgHfUnKh5pk.png)

Bu soruda POST request için Burp Suite kullanacağız. Dilerseniz curl de kullanabilirsiniz.

Varsayılan değerlerle sms gönderelim ve burp'te inceleyelim.

![burp1](https://s2.loli.net/2023/04/30/sLSitpTcR143um6.png)

Görüldüğü üzere xml formatında istek gönderiliyor ve mesaj olarak "test" dönüyor.
XXE zafiyetini kullanabiliriz. Öncelikle /etc/passwd dosyasını okumaya çalışalım.

![passwd](https://s2.loli.net/2023/04/30/lgTEqSLPZ2ckYON.png)

Burada isteği url encoded olarak yaptığımızı belirtmekte fayda var. Görüldüğü üzere uygulama XXE zafiyeti barındırıyor. Dönen "test" mesajı username etiketinin içerisinde olduğu için zafiyet burada mevcut. Şimdi flag.php yi nasıl okutabileceğimize bakalım. flag.php sayfasında sadece localhost'un bu sayfaya erişebileceğini görüyoruz.

![flagphp](https://s2.loli.net/2023/04/30/F6H5zuq8vVR7n14.png)

O halde php dönüşüm filtrelerini(conversion filters) kullanarak dosyanın içeriğini base64 formatına çevirebiliiriz.

![phpconversionfilter](https://s2.loli.net/2023/04/30/atZsxULP7Idbivr.png)

Evet dönen yanıt base64 formatında.

	PD9waHAKCmlmKCRfU0VSVkVSWyJSRU1PVEVfQUREUiJdICE9ICIxMjcuMC4wLjEiKXsKICAgIGVjaG8gIsSwemluc2l6IElQISE8YnIgLz4gU2FkZWNlIGxvY2FsaG9zdCDDvHplcmluZGVuIGdlbGVuIGlzdGVrbGVyIGthYnVsIGVkaWxpci48YnIvPiIuJF9TRVJWRVJbIlJFTU9URV9BRERSIl0uIiE9MTI3LjAuMC4xIjsKICAgIGV4aXQ7Cn1lbHNlewogICAgZWNobyAiQkctVEVLe1NVQ1VLX0HEnkFDSX0iOwp9Cg==

Herhangi bir base64 aracı kullanarak decode edebiliriz.

![flag](https://s2.loli.net/2023/04/30/EHLfP3IogeKT9RQ.png)

XXE zafiyetini ve php dönüşüm filtrelerini kullanarak dosyanın içeriğini okumayı başardık.

	BG-TEK{SUCUK_AĞACI}

### Green Leaf

	[http://ctf.bg-tek.net:8089]

Tekrar bir login sayfasıyla karşılaşıyoruz. Kullanıcı adı ve şifreyi admin olarak girdikten sonra şöyle bir yanıt alıyoruz.

![Login1](https://s2.loli.net/2023/05/03/HVnGMirZsvge7P8.png)

Sayfa kaynak koduna baktığımızda /js dizini altında login.js dosyası olduğunu görüyoruz. Dosyayı inceleyelim.

```javascript
$(document).ready(function(){

	$("#login_form").submit(function(e){
        e.preventDefault();
    });

 	$("#login_submit").on('click', function(){
 		var a = $('#login_form').serializeArray();
 		var post_data = {};
 		$.each(a, function () {
 			if (post_data[this.name]) {
                if (!post_data[this.name].push) {
                    post_data[this.name] = [post_data[this.name]];
                }
                post_data[this.name].push(this.value || '');
            } else {
                post_data[this.name] = this.value || '';
            }
        });
        alert(JSON.stringify(post_data));
    	$.ajax({
     		type: "POST",
 			url: "/user/login",
 			dataType: 'json',
            contentType: 'application/json',
 			data: JSON.stringify(post_data),
         	success: function(msg){
            	$('#response').html(msg.msg);
         	},
 			error: function(){
 				alert("failure");
 			}
       	});
 	});
});
```

İsteğin alert fonksiyonundan sonra gönderildiğini görüyoruz. JSON formatında gönderildiği için NOSQL veritabanı kullanıldığını düşünebiliriz. Bu aşamada NOSQL injection denemesi yapıyoruz. Bu sefer curl kullanacağız.

	curl -X POST -H 'Content-Type: application/json' -d '{"username":{"$ne": "br34kp0int"},"password":{"$ne": "123"}}' http://ctf.bg-tek.net:8089/user/login

![success](https://s2.loli.net/2023/05/03/FQ5uSktKPUlXeN2.png)

Görüldüğü üzere NOSQL injection zafiyeti mevcut ve sanitization kullanılmamış. $ne operatörü kullandığımız için kullanıcı adı ve şifre yerine istediğimiz değeri girebiliriz. Örneğin:

	{"username":{"$ne": null},"password":{"$ne": null}}

İki örnekte de veritabanında bulunan ilk kullanıcı olarak giriş yapabiliyoruz. Burada dikkat edilmesi gereken, şifreyi "yanlış" girmektir. Eğer doğru şifreyi tahmin etseydik veritabanındaki ilk kullanıcıyı atlamış olacaktık. Bu nedenle bir şifre girmektense null değeri bizi daha doğru sonuca götürecektir.

	BG-TEK{N0SQL_1NJ3CT1ON}


## Crypto

### B4Bür sana bir mesaj bıraktı

	Babür sana bir mesaj bıraktı. Babürün sana ne dediğini öğrenmen gerekiyor.
	01001100 01010011 00110100 01110101 01001100 01101001 01000001 01110100 01001100 01010011 00110100 01100111 01001100 01010011 01000001 01110101 01001001 01000011 00110000 01110101 01001100 01010011 01000001 01110100 01001100 01101001 00110000 01110101 01001001 01000011 00110000 01110100 01001100 01010011 01000001 01110101 01001100 01101001 00110100 01100111 01001100 01101001 00110000 01110101 01001100 01101001 01000001 01110101 01001100 01010011 01000001 01110100
Verilen binary'yi okunabilir metne çevirmek için cyberchef'i kullanacağız.

![cyberflag](https://s2.loli.net/2023/04/30/F7B3ILPRrKZmHjU.png)

Farklı araçlar da kullanılabilirdi fakat cyberchef sırasıyla binary, base64 ve mors kodunu kendisi tespit ettiği için başka bir araç kullanmamıza gerek kalmadı.

	BG-TEK{BGTEKCOSLAT}


## OSINT

### B4BüR_RETURNED

	Aldığımız bir bilgiye göre Babür sosyal medya üzerinde BaburHacke6843 nickini kullanıyor Babürün sosyal medya hesabını bulup gizlediği bir mesajı bize bildirmen gerekiyor.

Verilen kullanıcı adını twitterda aradığımızda bir profille karşılaşıyoruz. İki tweeti mevcut. İlk tweet bize wayback machine kullanmamız için yol gösteriyor.

![wayback](https://s2.loli.net/2023/04/30/MIB3LJfNk7ltv6V.png)


Wayback machine'de kullanıcının twitter adresini sorguladığımızda bir snapshot kaydedildiğini görüyoruz.

![](https://s2.loli.net/2023/04/30/CmeZtXky9DHToiV.png)

İlgili snapshot'ı ziyaret ettiğimizde iki tweetin arasında silinen bir tweet daha olduğunu görüyoruz.

![waybackflag](https://s2.loli.net/2023/04/30/Yzj5JlQcOsLCXDw.png)

Böylece flagi bulmuş oluyoruz.

	BG-TEK{W4YB4CK_M4CH1N3}

### Agent47

```
Bir süredir yakalamaya çalıştığımız ajan sana vermiş olduğumuz 1. fotoğrafı gizli bir chat uygulamasında paylaştı. Aldığımız bilgiye göre buradan sonra bir kiliseye gidecek ve gideceği kilisede sana vermiş olduğumuz 2. fotoğraftaki gibi bir alan bulunuyor. Senden ajanın gideceği kilisenin ismini öğrenmeni istiyoruz.

Flag formatı: BG-TEK{FLAG_FORMATI} boşluklar yerine _ kullan , bütün karakterler büyük harf olmak zorunda ve İ yerine I kullan.
```

Soruda bize iki farklı fotoğraf verilmiş.

| ![](https://s2.loli.net/2023/05/03/YbBCosTIPrRKMyi.jpg) | ![](https://s2.loli.net/2023/05/03/u81fiJCrMF5qDXK.png) |
|:-------------------------------------------------------:|:-------------------------------------------------------:|
|                       1.fotoğraf                        |                       2.fotoğraf                        |

İlk fotoğrafı Google Lens'te aradığımızda görselin Kastellorizo'da çekildiğini buluyoruz.

![Kastellorizo](https://s2.loli.net/2023/05/03/pWoCd6fBLDruiUg.png)

Ardından Kastellorizo'daki kiliseleri Google Maps'te arıyoruz. "kastellorizo church" şeklinde arama yapıp görselleri incelediğimizde 5.kilisenin görseli 2.fotoğrafla eşleşiyor.

![Church](https://s2.loli.net/2023/05/03/O1pyd8lC7ZwicPQ.png)

Flag olarak birkaç hatalı denemenin ardından mapsteki ismin aynısını girdiğimizde doğru cevaba ulaşıyoruz.

	BG-TEK{SAINT_GEORGE_AT_PIGADI_ORTHODOX_CHURCH}

Mini ctf yarışması için ideal bir seviyedeydi diyebiliriz. Web kategorisi telefonla katılan yarışmacılar için biraz zor denilebilir.