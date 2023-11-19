def text_analyzer():
    vowels = ['a','e','i','o','u']
    num_of_vowels=0
    num_of_consonants=0
    num_of_upperCase=0
    num_of_lowerCase=0
    user_choice = input("Enter 1 to Try Text Analyzer. Enter 2 to Exit: ")
    if user_choice == "1":
        file = open('Story.txt', 'r')
        file_text = file.read()
        for i in file_text:
            if i.isalpha():
                if (i.lower() in vowels):
                    num_of_vowels += 1
                else:
                    num_of_consonants += 1
                
                if i.isupper():
                    num_of_upperCase += 1
                else:
                    num_of_lowerCase += 1
        analyzed_text = f'''Analyzed: 
        No. of vowels:  {str(num_of_vowels)}
        No. of consonants:{str(num_of_consonants)}
        No. of Upper Case Character:{str(num_of_upperCase)}
        No. of Lower Case Character:{str(num_of_lowerCase)}
        '''
        print(analyzed_text)

        text_analyzer()
    else:
        print("Thank You!!!")
text_analyzer()