## Güzellik
Bize bir zip dosyası verilmiş ve ismi 65535.zip. Açtıkça ismi bir azalacak şekilde yapılmış. Bir script yazarak bunları 1.zip'e kadar açtık.
https://github.com/Kazgangap/infinite-zip-unzipper
Sonuncusu şifreliydi ve içeriside 1.txt vardı.
Zip2john kullanarak hash formatına getirdik vevarsayılan wordlistlerde denemeler yaptık.Zip şifresi sqlmap wordlist içersinden çıktı bunu yazıp 1.txt dosyasının içeriğindeki flag'a ulaştık.

