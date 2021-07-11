# Finding the grade of the student based on his/her marks
M1 = int(input("Enter M1 marks:"))
M2 = int(input("Enter M2 marks:"))
M3 = int(input("Enter M3 marks:"))
M4 = int(input("Enter M4 marks:"))
M5 = int(input("Enter M5 marks:"))
if ((M1>100 or M2>100 or M3>100 or M4>100 or M5>100) or (M1<0 or M2<0 or M3<0 or M4<0 or M5<0)):
    print("Please enter valid Marks")
else:
    aggregate = (M1+M2+M3+M4+M5)/5
    print("Your aggregate marks are: "+str(aggregate))
    if aggregate >= 40:
        print('Pass')
        if (aggregate > 75):
            grade = "Distinction"
        elif (aggregate >= 60 and aggregate < 75):
            grade = "1st class"
        elif (aggregate >= 50 and aggregate < 60):
            grade = "2nd class"
        elif (aggregate >= 40 and aggregate < 50):
            grade = "3rd class"
        print("Your Grade is "+grade+".")
    else:
        print("Fail")