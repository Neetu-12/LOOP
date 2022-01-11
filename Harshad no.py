i=1
a=0 
while i<=10:
    j=i
    sum=0
    while j>0:
        a=j%10
        sum+=a
        j=j//10
    if i%sum==0:
        print(i,"Harshad no")
    i+=1



##check harshad no.
n=int(input("enter no."))
t=n
s=0
while t>0:
	a=t%10
	s=s+a
	t=t//10
if n%s==0:
	print(n,"harshad no.")
else:

	print(n,"is not harshad no.")



# n=int(input("enter:-" ))
# if n%4==0:
#     if n%400==0:
#         print(" Leap year")
# elif n%100==0:
#     print(" Not Leap year")
# else:
#     print("not leap year")



# yr=int(input("enter leap year "))
# if yr%100==0:
# 	if yr%400==0:
# 		print("leap year")
# 	else:
# 		print("not leap yr")
# else:
# 	if yr%4==0:
# 		print("leap year")
# 	else:
# 		print("not a leap year")


# def is_leap(year):
#     if year%4==0:
#         if  year%100==0:
#             return False
#     else:
#         if year%400==0:
#             return True
# year = int(input())
# print(is_leap(year))

