from tr_script import main 
from en_script import main 

while True:
    print("Which language would you like to use?")
    print("1. English")
    print("2. Türkçe")
    language_choice = int(input("Enter your choice (1 or 2): "))
    if language_choice == 1:
        language_choice = "en"
        main.en_script()
    elif language_choice == 2:
        language_choice = "tr"
        main.tr_script()
    else:       
        print("Invalid choice, please try again or press (ctrl+c) to exit.\n \n")
        print(chr(27) + "[2J")
        continue 
