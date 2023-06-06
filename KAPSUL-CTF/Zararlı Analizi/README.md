## PAKET

![Paket](https://s2.loli.net/2023/06/07/aZUliDsetWXd8kf.png)

Programı Ghidra aracında incelediğimizde UPX stringlerini görüyoruz.

```bash
upx -d PAKET.exe -o UNPAKET.exe
```

Sıkıştırılmış dosyayı açtığımızda stringleri tekrar inceliyoruz ve flagi buluyoruz.

```bash
strings UNPAKET.exe |grep -i "hackme"
```

```
HACKME{F4zl4Kol4y0lduD1_m1}
```

## Zaman Zaman Ama Ne Zaman

Verilen dosyanın içindeki stringleri incelediğimizde pyinstaller, requests, urllib3 gibi stringlerle karşılaşıyoruz bu da çalıştırabilir dosyanın python'da yazıldığı anlamına gelmektedir.

Verilen dosyanın içeriğini çıkarmak için öncelikle pyinstxtractor aracını kullanıyoruz. Ardından Decompyle++ aracını kullanarak pyc uzantılı dosyayı okunabilir formata çeviriyoruz.

```python
# Source Generated with Decompyle++
# File: 2newq.pyc (Python 3.7)

import random
import string
import datetime
import uuid
import requests

def hayde():
    print('Hoşgeldin yaaaar, yüreğimeeee,boşver be, elalem ne der se de sin haydi haydi haydi. Böyle devam krall bi incele bakayım buraları.')


def get_mac_address():
    mac_address = ':'.join((lambda .0: [ '{:02x}'.format(uuid.getnode() >> ele & 255) for ele in .0 ])(range(0, 48, 8))[::-1])
    return mac_address


def generate_domain(seed):
    random.seed(seed)
    domain_length = random.randint(5, 10)
    domain = ''.join((lambda .0: pass)(range(domain_length)))
    return domain


def generate_dga_domains(num_domains):
    domains = []
    seed = datetime.datetime.now().strftime('%Y%m%d%H')
    for _ in range(num_domains):
        domain = generate_domain(seed)
        domains.append(domain)
        seed = domain
    
    return domains


def main():
    num_domains = 2
    dga_domains = generate_dga_domains(num_domains)
    
    try:
        url = f'''https://{dga_domains[0]}.github.io/{dga_domains[1]}.flg'''
        print('DGA başlatıldı...')
        res = requests.post(url)
    except:
        print('The server cannot communicate!')


if __name__ == '__main__':
    allowed_corp = '00:15:17'
    mac = get_mac_address()
    if mac.startswith(allowed_corp):
        print('The system is among the targets, attack started')
        main()
    else:
        print('Your MAC: ' + mac)
        print('The system is not among the targets')
```

Kodu incelediğimizde MAC adresine göre saldırı yapıldığını görüyoruz. Burada tek yapmamız gereken seedi tahmin etmek. Bunun için de çalıştırılabilir dosyanın oluşturulduğu zamandan itibaren for döngüsü oluşturulup tek tek github adresine istek gönderilebilir ve http durum koduna göre doğru adres tahmin edilebilir.

Fakat .flg uzantılı dosyayı gördüğümde bu dosyayı githubda aradım. Arama çubuğuna \*.flg yazmak yeterli olacaktır.

![zaman](https://s2.loli.net/2023/06/07/x2GWhvnYuRgDcMs.png)

Commit sekmesine gelip sonuçları zamana göre sıraladığımda .flg dosyalı bir dosyanın oluşturulduğunu fark ediyorum.

![base](https://s2.loli.net/2023/06/07/QfnsxNDa7TerC2I.png)

Dosyanın içeriğini base64 decode ettiğimizde flagi buluyoruz.

```bash
echo "SEFDS01FezFuczF5NHQxZl80bDF5MHJ1bV9CdV9TMHJ1X0Mwa19HMGw0eX0=
" | base64 -d
```

```
HACKME{1ns1y4t1f_4l1y0rum_Bu_S0ru_C0k_G0l4y}
```
