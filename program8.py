import math

def math_fun_calculator():
    user_choice = input("Enter 1 to Try Mathematical Functions. Enter 2 to Exit: ")
    if user_choice == "1":
        print('''Math Function Calculator
Enter 1 to Calculate Square of a number
Enter 2 to Calculate Log of a Number ( i.e. Log10 )
Enter 3 to Calculate Quad of a number''')
        choice = input("Enter your choice: ")
        num = int(input("Enter a number: "))
        if choice == "1":
            print("Square of " + str(num) + " = " + str((num**2)))
        elif choice == "2":
            print("Log10 of " + str(num) + " = " + str(math.log10(num)))
        elif choice == "3":
            print("Quad of " + str(num) + " = " + str(num))
        else:
            print("Invalid Choice")
        math_fun_calculator()
    else:
        print("Thank You!!!")
math_fun_calculator()