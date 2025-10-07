def fibnoci(l):
    n1=0
    n2=1

    for i in range(l):
        sum=n1+n2
        print(sum)
        n1=n2
        n2=sum
limit=int(input("enter the limit:"))

fibnoci(limit)

      
