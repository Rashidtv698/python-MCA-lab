a =[1,2,3,4,5]
b = [1,2,3,5]

if len(a)==len(b):
    print("same length")
else :
    print("Not same length")
    
sum1=0
sum2=0

for i in a:
    sum1=sum1+i
for i in b:
    sum2=sum2+i

if sum1==sum2:
    print("same sum")
else :
    print("Not same sum")

for i in a:
    for j in b:
        if i==j:
            print(i)
