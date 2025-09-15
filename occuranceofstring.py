s="welcome to the the great mes mes"
a=s.split()
l=len(a)
i=0
count=0

while(i<l):
    j=i
    while(j<l):
        if(a[i]==a[j]):
            count= count+1
        
        j=j+1
    print(f"{a[i]}{count}")
    count=0
    i=i+1

 
   
