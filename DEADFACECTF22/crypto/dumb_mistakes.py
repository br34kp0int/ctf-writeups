import math
import string

# rsa algorithm
p=2063
q=1049
e=777887
n = p*q
tot = (p-1)*(q-1) # euler's totient function
d = pow(e,-1,tot) # d = e^-1 mod(tot)
print('flag{d=%s}' % d)