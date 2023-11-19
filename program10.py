def text_analyzer():
    num_of_he=0
    num_of_she=0
    user_choice = input("Enter 1 to Try Text Analyzer. Enter 2 to Exit: ")
    if user_choice == "1":
        file = open('Info.txt', 'r')
        file_text = file.read()
        file_texts = file_text.split()
        for i in file_texts:
            if i.lower() == "he":
                num_of_he += 1
            elif i.lower() == "she":
                num_of_she += 1
        analyzed_text = f'''Analyzed: 
        No. of "He" used in file are: {str(num_of_he)}
        No. of "She" used in file are: {str(num_of_she)}
        '''
        print(analyzed_text)

        text_analyzer()
    else:
        print("Thank You!!!")
text_analyzer()