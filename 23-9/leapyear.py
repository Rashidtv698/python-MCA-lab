limit1=int(input("enter first index"))
limit2=int(input("enter last index"))
for i in range(limit1,limit2):
    if (i%4==0 and (i%100!=0)):
        print(i)
