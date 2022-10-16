## Pandora's Box (5 pts)
![pandoras](https://i.ibb.co/vdry0ZC/pandoras.png)
I wrote a python script that shifts the letter backwards as amount of given numbers.

>flag{dont_let_her_out}

## 'D' is for Dumb Mistakes (15 pts)
Rsa algorithm question. Prime numbers and exponent were given and flag format was flag{d=VALUE}. Used a script to solve this challenge.

>flag{d=1457215}

## Ozymandias (50 pts)
Ciphertext:
> JBEFQQ3CIE3G423KINYTIMKZINDXAZ3VO5UEKTSU PFGEE6DHNVBUQ33LOUZE24S2GJDVU6CQIZJWCMZR ORFGSUKGOUZWE6KRJA3UOSCYONAXESDJGF3UEZCT NFIXQSSZLEYVU4DYGJIHG33SNZAUEZD2NNYUESTO MRFFG4JZMNZE4MSNOY2UYR3PKRUVS2BYLFSG4MLP NF2EG3KBJRLGQOCLOZXDKSDJNZGEIZCTOZTWK6DU JBHEE6LQJZZVS4JRNIZWQ32HMVUXS===

First thing comes to my mind is base64 encoding, however it is slightly different, hence base64 decoding didn't work. Then I used [CyberChef](https://gchq.github.io/CyberChef/) tool and removed spaces. Tool detected that the encodings were base32, base58, and base85 respectively.

![Ozymandias](https://i.ibb.co/R2SR9Pg/4.png)

## Two Dead Boys
Question starts with this:

> Good evening, this is a NEWSFLASH from Quick News Network (QNN)... I'm Crime News Reporter Frank Viginere...

And the ciphertext was:
> Gla ktwulpbr pg Klkw Urao ax qlsn{Pvelnnad Aumjcnyg: Ibrwpaty ENLECPZNYG!}

Frank Viginere name was a sign of the Vigenere cipher and the key was newsflash which is written in capital letters in the question.

Plaintext was:
> The solution to Fake News is flag{Critical Thinking: Question EVERYTHING!}



