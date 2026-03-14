n=int(input())
b=0;a=1
while n:
    b+=n%10*a
    a*=10
    n//=10
print(b)    
