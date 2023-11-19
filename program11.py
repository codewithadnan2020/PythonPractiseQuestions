def text_analyzer():
    user_choice = input("Enter 1 to separate each word by [#] on every line. Enter 2 to Exit: ")
    if user_choice == "1":
        file = open('Story.txt', 'r')
        file_text = file.readlines()
        for i in file_text:
            print(i.replace(' ', '#'))
        text_analyzer()
    else:
        print("Thank You!!!")
text_analyzer()