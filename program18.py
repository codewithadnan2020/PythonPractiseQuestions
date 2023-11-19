stack = []
def push_peek_stack():
    choice = input("Enter 1 to try stack (Popped Item / Peek). Enter 2 to Exit:")
    if choice == "1":
        print('''Enter 1 -> Push
Enter 2 -> Pop
Enter 3 -> Peek''')
        user_choice = input("Enter your choice:")
        if user_choice == "1":
            val = input("Enter a value:")
            stack.append(val)
        elif user_choice == "2":
            print("Popped item = "+ stack.pop())
        elif user_choice == "3":
            stack_len = len(stack) - 1
            print(stack[stack_len])
        else:
            print("Invalid Choice")
        push_peek_stack()
    else:
        print("Thank You!!!")
push_peek_stack()
