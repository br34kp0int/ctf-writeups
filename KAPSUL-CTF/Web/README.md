
## Yeni Yazılımcı

Dizin taraması yapıldığında /clients dizini olduğu bulunur.

/clients dizinindeki tüm kelimeleri bir wordlistte topladıktan sonra anasayfada login denemeleri yapılır. Bu aşamada Burpsuite aracının intruder özelliğini kullanabiliriz.

Öncelikle username parametresindeki değer için wordlistteki kelimeleri deniyoruz.

İsteklere dönen yanıtları incelediğimizde sadece bir kez "hatalı parola" yanıtını görüyoruz. Username değerine baktığımızda "admin" değeri için bu yanıtın döndüğünü buluyoruz.

Username parametresini admin olarak atadıktan sonra aynı işlemi password parametresi için uyguluyoruz. Gelen isteklerin sadece birinde http durum kodunun 302 olduğunu görüyoruz. Bu da başarılı bir şekilde giriş yapıldığı anlamına geliyor. Parola parametresine baktığımızda "icecream" değerini buluyoruz.

Sisteme giriş yaptığımızda komut çalıştırabileceiğimiz bir formla karşılaşıyoruz. Ancak girilen komut çalıştırılmıyor ve aynı sayfayla karşılaşıyoruz.

ls komutunu girmeyi deneyelim ve trafiği gözlemleyelim. İsteğin /route?run=ls gibi(ss almadığım için bu kısımda yanlışlık olabilir) bir formda olduğunu gözlemliyoruz.

Burpsuite'te anasayfaya yönlendirilmeden önceki son isteği repeater'a yolluyoruz.

ls komutunun çıktısını yanıtta görebiliyoruz. flag.txt dosyasını örneğin "/route?run=cat+flag.txt" gibi bir istekle okumaya çalıştığımızda boş yanıt dönüyor. Bu da demektir ki bir filtreleme söz konusu.

Burada biraz vakit kaybettikten sonra boşluksuz ve url encoded olacak şekilde payload denemesi yapıyoruz. "/route?run=cat%24%7BIFS%7Dflag.txt"

```python
cat${IFS}flag.txt
```

Böylece flagi okumuş oluyoruz. Kullandığımız komuttaki ${IFS} ifadesi iki iki argümanı birbirinden ayıran bir değerdir. Boşluk değeri gibi düşünülebilir.

```
HACKME{C0mM4Nd!nJ3Ct1On1Sb3sT}
```


## SeVGi Paylaştıkça Artar

Verilen sayfada bizden dosya yüklememiz ve ekrana flag bastırmamız isteniyor. Bazı uzantılar filtrelenmiş fakat soru isminden yola çıkarak svg yükleyebildiğimizi keşfediyoruz. XSS zafiyetini sömürebiliriz.

Kullandığımız svg dosyasının içeriği:

```html
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="full">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
    alert("flag");
  </script>
</svg>
```

```
HACKME{s3Vm36EN_D3_b3n1}
```

## Vadi

- Verilen ipucundan yola çıkarak /Dockerfile , /docker-compose.yml dosyaları bulunur. (dizin wordlistinde bulamadık.)
- docker-compose.yml dosyasından Dockerfile.mysql adlı bir dosya daha olduğu görülür. 
- Dockerfile.mysql dosyasından da "cxzcx8as6d5ad3sa1das.sql" adlı dosya keşfedilir.
- Bu dosya okunduğunda flag tablosu oluşturulduğu ve içine parolası base64 encode edilmiş bir değer atandığını görüyoruz.
- Herhangi bir base64 toolu kullanılarak decode edilebilir. Biz bash kullandık.

```bash
echo "SEFDS01Fe0tbX11yN0w0UjFuX1Y0ZDFTMX0=" | base64 -d
```

```
HACKME{K[_]r7L4R1n_V4d1S1}
```
