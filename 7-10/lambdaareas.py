sq=int(input("enter side of square:"))
sqarea= lambda x:x*x
r1=int(input("enter 1st side of rectangle:"))
r2=int(input("enter 2nd side of rectangle:"))
recarea= lambda x,y:x*y
base=int(input("enter base side of triangle:"))
height=int(input("enter hight side of triangle:"))
triarea= lambda x,y:(x*y)/2


print("Area of triangle :",triarea(base,height))
print("Area of rectangle :",recarea(r1,r2))
print("Area of square :",sqarea(sq))

