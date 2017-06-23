a=int(raw_input("Enter a number"))
b=0
n=a
while a!=0:
	r=a%10
	b=b*10+r
	a=a/10
if (b==n):
	print ("It is palindrome",n)
else:
	print ("It is not palindrome",n)
 
