n=int(input("enter a number(min 4 numbers)"))
if n<1000:
    print("Enter min 4 digt number")
    n=int(input("enter a number(min 4 numbers)"))


def rev(n):
    new=0
    while(n>0):
        temp=n%10
        new=new*10+temp
        n=n//10
    return new
print("reversed :",rev(n))
    


 
    
