def area_calculator():
    user_choice = input("Enter 1 to Try Area Calculator. Enter 2 to Exit: ")
    if user_choice == "1":
        print('''Area calculator
Enter 1 to Calculate Area of Circle
Enter 2 to Calculate Area of Rectangle
Enter 3 to Calculate Area of Triangle''')
        choice = input("Enter your choice: ")
        if choice == "1":
            r = int(input("Enter radius:"))
            PI = 3.142
            print("Area is circle with radius " + str(r) + "="+str((PI * (r*r))))
        elif choice == "2":
            length = int(input("Enter length:"))
            width = int(input("Enter width:"))
            print("Area is Rectangle with length " + str(length) + " & width " + str(width) +" = "+str((length * width)))
        elif choice == "3":
            base = int(input("Enter base:"))
            height = int(input("Enter height:"))
            print("Area is Triangle with base " + str(base) + " & height " + str(height) +" = "+str(((base * height)/2)))
        else:
            print("Invalid Choice")
        area_calculator()
    else:
        print("Thank You!!!")
area_calculator()