def sum_of_even_num():
    sum_of_even_nums = 0
    user_choice = input("Enter 1 to Get Sum Of Even numbers. Enter 2 to Exit: ")
    if user_choice == "1":
        list_of_nums = eval(input("Enter your list of numbers; Eg. [1, 2, 3]: "))
        for i in list_of_nums:
            if i % 2 == 0:
                sum_of_even_nums += i
        print("Sum of even num : "+str(sum_of_even_nums))
        sum_of_even_num()
    else:
        print("Thank You!!!")
sum_of_even_num()