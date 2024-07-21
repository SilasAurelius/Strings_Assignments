"""
Task 1: Input Length Validator 
Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
"""

def input_length_validator():
    while True:
        user_first_name = input("Enter your first name: ")
        user_last_name = input("Enter your last name: ")
        
        if len(user_first_name) >= 2 and len(user_last_name) >= 2:
            print("Minimum character length met.")
            break
        else:
            print("Error: Both first name and last name must be at least 2 characters long. Please try again.")

input_length_validator()

     
     

