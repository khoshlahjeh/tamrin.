Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
temp=0
>>> while(temp>10):
	for i in range(len(a)):
		temp +=int(a[i])
		a=temp
		temp=0
		print(a)