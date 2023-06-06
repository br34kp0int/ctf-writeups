## .rav şi rib et'ters uB

Kategori ve soru başlığı ters olduğu için verilen metni de ters çevirdik ve birkaç kez base64 encode edildiğini fark ettik.

![ters](https://s2.loli.net/2023/06/07/2PAih34L5fRvgeK.png)

Metni cyberchef'te sırasıyla rev ardından 4 kez base64 decode'dan geçirdiğimizde fake flag ve şifreli metinle karşılaşıyoruz. Verilen şifreli metni yine cyberchef'te bacon cipher decode'a attığımızda flagi buluyoruz.

![flag](https://s2.loli.net/2023/06/07/8zgvnjtIWOfQ5yh.png)

```
HACKME{BUCRYPTOLARDACOKKOLAYBE}
```
