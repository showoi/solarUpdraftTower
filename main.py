#import-necessary-libraries--------------#
import json
#language-declaration--------------------#
with open('languages.json', 'r') as f:
    translations = json.load(f)


while True:
    print("Which language would you like to use?")
    print("1. English")
    print("2. Türkçe")
    language_choice = int(input("Enter your choice (1 or 2): "))
    if language_choice == 1:
        language_choice = "en"
        break
    elif language_choice == 2:
        language_choice = "tr"
        break
    else:       
        print("Invalid choice, please try again or press (ctrl+c) to exit.\n \n")
        print(chr(27) + "[2J")
        continue

#----------------------------------------#
def menu():
    print("""
               __                   ___    __          __      
              /\ \__               /\_ \  /\ \      __/\ \__   
  ____  __  __\ \ ,_\   ___     ___\//\ \ \ \ \/'\ /\_\ \ ,_\  
 /',__\/\ \/\ \\ \ \/  / __`\  / __`\\ \ \ \ \ , < \/\ \ \ \/  
/\__, `\ \ \_\ \\ \ \_/\ \L\ \/\ \L\ \\_\ \_\ \ \\`\\ \ \ \ \_ 
\/\____/\ \____/ \ \__\ \____/\ \____//\____\\ \_\ \_\ \_\ \__\
 \/___/  \/___/   \/__/\/___/  \/___/ \/____/ \/_/\/_/\/_/\/__/
                                                               
                                                               
""")
    print("1. Script 1")
    print("2. Script 2")
    print("3. Script 3")