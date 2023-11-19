def vowel_counter():
    vowels = ['a','e','i','o','u']
    num_of_vowels = 0
    num_of_vowels_det = {'a': 0,'e':0,'i':0,'o':0,'u':0}
    user_choice = input("Enter 1 to Try Vowel Counter. Enter 2 to Exit: ")
    if user_choice == "1":
        sentence = input("Enter your Sentence: ")
        for i in sentence:
            for j in vowels:
                if i == j:
                    num_of_vowels += 1
                    num_of_vowels_det[j] = num_of_vowels_det[j] + 1
        print("Total number of vowel detected: "+str(num_of_vowels))
        print("Total number of vowel detected (detailed): "+str(num_of_vowels_det))
        vowel_counter()
    else:
        print("Thank You!!!")
vowel_counter()