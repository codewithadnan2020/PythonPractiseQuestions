def fibonacci_series():
    user_choice = input("Enter 1 to See Fibonacci Series of a number. Enter 2 to Exit: ")
    if user_choice == "1":
        num = int(input("Enter a number: "))
        n1,n2 = 0, 1
        count = 2
        if num < 0:
            print("Plese enter a positive integer")
        elif num == 1:
            print(n1)
        else:
            print(n1, end=' ')
            print(n2, end=' ')
            while count < num:
                n3 = n1 + n2
                print(n3, end=' ')
                count+=1
                n1=n2
                n2=n3
            print()
        fibonacci_series()
    else:
        print("Thank You!!!")
fibonacci_series()