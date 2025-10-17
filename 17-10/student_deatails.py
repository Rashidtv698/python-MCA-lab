student={
    "name": "Raashi",
    "roll_number":"33",
    "register_number":"45677",
    "department":"MCA",
    "semester":"s1"
    }

mark=int(input("enter total mark"))


if (mark>=90):
    grade="A"
elif(mark>=82):
    grade="B"
elif(mark>=75):
    grade="C"
elif(mark>=60):
    grade="D"
elif(mark>=50):
    grade="P"
else:
    grade="F"

student["Grade"]=grade
student.pop("roll_number")

print(student)
