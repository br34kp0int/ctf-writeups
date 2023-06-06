# Kapsul CTF OSINT Çözümleri: 

## Belediyenin Sana İhtiyacı Var

![belediye](images/belediye.png)

https://www.usom.gov.tr/ sitesinde "Zararlı Bağlantılar" sekmesinden "konya" yanzdığınızda en güncel olan "konyamkart.net" sitesi aradığımız sitedir.

![usom](images/usom.png)

https://www.whois.com/whois/konyamkart.net şeklinde whois sorgusu yaparak domain posta koduna erişebilirsiniz.

![whois](images/whois.png)

    Flag : HACKME{M4K3K1}

## Bir Gece Ansızın Gelebilirim

![gece](images/gece.png)

Verilen linke tıkladığımızda sonuç gelmediğini görüyoruz.

https://web.archive.org sitesinden verilen youtube linkini web arşivde arayıp, kanalın snapshotlarını buluyoruz. 20 Mayıstaki snapshota bakabiliriz.

![archive](images/archive.png)

Kanalda görünmeyen videoyu arşivde bulduk:

![archive](images/archive2.png)

Tarama çubuğundaki youtube linkini ayıklayıp yeni sekmede videoyu oynatabilirsiniz.

![archive](images/archive3.png)

Videonun 30.saniyesinde bir QR kod göreceğiz :

![video](images/video.png)

QR'ı tarattığımızda google mapste bir yer açılıyor :

![harita](images/harita.png)

Yorumlarda flagi görüyoruz.

    Flag : HACKME{PEŞİNDEYİZVESENİİYİTANIYORUZ}
    
## Derya Nolur Geri Dön Seni Çok Seviyom

![derya](images/derya.png)

"derya bakanlık hack" tarzı bir google araması yaptığınızda "aşkı için maliye bakanlığı sitesini hack'lemek" sonucunu görürsünüz.

![tarama](images/google.png)

"aşkı için maliye bakanlığı sitesini hacklemek" şeklinde bir arama daha yaparak görsellerde sonucu bulabiliriz.

![tarama](images/aşk.png)

![mato](images/themato.jpeg)

    Flag : HACKME{TheMato}
    
## Kaçma Yorgun Öleceksin

![kaçma](images/kaçma.png)

Verilen site yine sonuç döndürmüyor ve archive kayıtları da yok. 

https://toolbox.googleapps.com/apps/dig adresinden dns kayıtlarını inceliyoruz :

txt kısmında bir link bırakıldığını görüyoruz ("https://groups.google.com/g/internationalespionage")

![dns](images/dns.png)

Linke gidelim :

![groups](images/groups.png)

Flagi bulduk

![groups2](images/groups2.png)

    Flag : HACKME{82NIJNIN0VG0R0D}
    
## Yoksa Hala Takip Etmediniz Mi?

Ctfi hazırlayan LastGuard'ın instagram adresindeki fotoğrafta flagi buluyoruz.

     https://www.instagram.com/lastguardsec/
     
 ![instagram](images/insta.png)
 
 
 @ElliotAlderson




