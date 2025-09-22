s=input("enter a word")
temp=s[0]
new=s[0]+s[1:len(s)].replace(temp,"$")

print(new)

