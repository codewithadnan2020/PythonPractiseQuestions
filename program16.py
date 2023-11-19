stack = []
def push_pop_stack():
    choice = input("Enter 1 to try stack (Push / Pop). Enter 2 to Exit:")
    if choice == "1":
        print('''Enter 1 -> Push
Enter 2 -> Pop
Enter 3 -> view''')
        user_choice = input("Enter your choice:")
        if user_choice == "1":
            val = input("Enter a value:")
            stack.append(val)
        elif user_choice == "2":
            stack.pop()
            print(stack)
        elif user_choice == "3":
            print(stack)
        else:
            print("Invalid Choice")
        push_pop_stack()
    else:
        print("Thank You!!!")
push_pop_stack()
