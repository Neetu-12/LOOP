# a=input("enter name:-")
# i=0
# s=""
# while i<len(a):
# 	s=a[i]+s
# 	if i+1==len(a):
# 		if s==a:
# 			print("pelindrom")
# 		else:
# 			print("not pelindrom")			
# 	i+=1



# n=(input(":-"))
# i=-1
# s=""
# while i>=-len(n):
#     s=s+n[i]
#     i=i-1
# if n==s:
#     print("pallindrome")
# else:
#     print("not pallindrome")


n=input("enter the no.:-")
i=0
s=""
while i<len(n):
    s=n[i]+s
    if i+1==len(n):
        if n==s:
            print('pallindrome')
        else:
            print("not pallindrome")
    i=i+1