count_back= '3686 526 814 518'
cipher ='guvz qgz pfv tvb'
i=0
msg=''
for val in count_back:
	if val == ' ':
		msg += '_'
		i += 1
		continue
	result = ord(cipher[i])-int(val)
	if result < ord('a'):
		result += 26
	msg += chr(result)
	i+=1

print(f'flag{{{msg}}}')
