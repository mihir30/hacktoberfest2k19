n=int(input("Enter an integer:"))
print("Factors are:")
i=1
c=0
while(i<=n):
    if(n%i==0):
        print(i)
        c=c+1;
    i=i+1;
if(c==2):
    print (n,"is a prime number");
else:
    print(n,"is not a prime number");

    