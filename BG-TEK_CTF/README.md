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

Mini ctf yarışması için ideal bir seviyedeydi diyebiliriz. Web kategorisi telefonla katılan yarışmacılar için biraz zor denilebilir.