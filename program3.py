import random
def rand_num_gen():
    user_choice = input("Enter 1 to Simulate dice. Enter 2 to Exit: ")
    if user_choice == "1":
        print(random.randint(1,6))
        rand_num_gen()
    else:
        print("Thank You!!!")
rand_num_gen()