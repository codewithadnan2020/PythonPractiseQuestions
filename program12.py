def text_analyzer():
    user_choice = input("Enter 1 to copy lines start with 'a' or 'A' from one file to another. Enter 2 to Exit: ")
    if user_choice == "1":
        file2 = open("SampleFiltered.txt", "w")
        file1 =  open("Sample.txt", "r")
        for i in file1.readlines():
            if i.lower().startswith('a'):
                file2.write(i)
        file1.close()
        file2.close()
        text_analyzer()
    else:
        print("Thank You!!!")
text_analyzer()