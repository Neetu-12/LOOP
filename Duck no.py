n=int(input("enter your no."))
i=0
while n>0:
    a=n%10
    n=n//10
    if a==0:
        i=i+1
if i>=1:
    print("it's a duck no.")
else:
    print("it's not a duck no.")