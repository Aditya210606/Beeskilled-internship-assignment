


num1 = int(input("Enter the marks of 1 subject  : "))
num2 = int(input("Enter the marks of 2 subject  : "))
num3 = int(input("Enter the marks of 3 subject  : "))
num4 = int(input("Enter the marks of 4 subject  : "))
num5 = int(input("Enter the marks of 5 sub : "))

avg = round((num1 + num2 + num3 + num4 + num5) / 5, 2)  #logical part to calculate avg

print("Average marks : ",avg)

# condition statements for obtaining the grade according to marks 
if avg >= 90:
    print("Your grade is O")

elif avg >= 80:
    print("Your grade is A")

elif avg >= 70:
    print("Your grade is B")

elif avg >= 60:
    print("Your grade is C")

else:
    print("You failed in the exam") 


