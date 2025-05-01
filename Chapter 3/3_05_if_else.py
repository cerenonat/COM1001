# 3.5 Reimplementing with if-else
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
else:
    if grade >= 80:
        print("B")
    else:
        if grade >= 70:
            print("C")
        else:
            if grade >= 60:
                print("D")
            else:
                print("F")
