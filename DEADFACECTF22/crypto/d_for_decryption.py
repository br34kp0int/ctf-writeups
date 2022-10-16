import math
import string

p=2063
q=1049
e=777887
n = p*q
tot = (p-1)*(q-1)
d = pow(e,-1,tot)
c="992478-1726930-1622358-1635603-1385290"  # ciphertext
c_int=c.split(sep='-')
message_num=[]
m=''
for number in c_int:  # rsa decryption
	message_num.append(pow(int(number), d, n))

for num in message_num: # convert numbers to letters (1=a, 2=b, etc.)
	m+=m.join('{}'.format(chr(ord('`')+num)))

print('flag{%s}' % m)