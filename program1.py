def calculator():
    user_choice = input("Enter 1 to Open Calculator. Enter 2 to Exit: ")
    if user_choice == "1":
        print('''Arithmetic Calculator
        Enter 1 -> +
        Enter 2 -> -
        Enter 3 -> *
        Enter 4 -> /
        Enter 5 -> %
        ''')

        choice = input("Enter your choice: ")
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        if choice == "1":
            print(first_num + second_num)
        elif choice == "2":
            print(first_num - second_num)
        elif choice == "3":
            print(first_num * second_num)
        elif choice == "4":
            print(first_num / second_num)
        elif choice == "5":
            print(first_num % second_num)
        else:
            print("Invalid Choice")
        calculator()
    else:
        print("Thank You!!!")
calculator()