def get_factorial():
    user_choice = input("Enter 1 to Get Factorial of a number. Enter 2 to Exit: ")
    if user_choice == "1":
        num = int(input("Enter a number: "))
        factorial = 1
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
            print("The factorial of",num,"is",factorial)

        get_factorial()
    else:
        print("Thank You!!!")
get_factorial()