# n=int(input("enter the no."))    
# i=0
# while i<=n:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
    
#     if c==2:
#         print(i)
#     i=i+1


n=int(input("enter the no."))    
i=0
while i<=n:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    i=i+1
    
if c==2:
    print("prime no.")
else:
    print("not prime no.")