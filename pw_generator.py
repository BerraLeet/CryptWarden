import secrets
import string

password = ""
choices = []

while True:
    # accepts number of characters from 6 to 36, not raising, loops till valid number given
    while True:
        length = input("Enter the password length (between 6 and 36): ")

        try:
            length = int(length)
            if 6 <= length <= 36:
                break
            else:
                print("Password length must be between 6 and 36. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    # Loop for adding number characterset to choices
    while True:
        num_within = input("Do you want numbers in your password: y/n\n\n")
       
        if num_within == "y":
            choices += string.digits
            break
        elif num_within == "n":
            break
        else:
            print("Please insert 'y' or 'n'")

   # Loop for adding symbols characterset to choices
    while True:
        sym_within = input("Do you want symbols in your password: y/n\n\n")
       
        if sym_within == "y":
            choices += string.punctuation
            break
        elif sym_within == "n":
            break
        else:
            print("Please insert 'y' or 'n'")

    # Loop for adding uppercase ascii characterset to choices
    while True:
        upper_within = input("Do you want uppercase letters in your password: y/n\n\n")
       
        if upper_within == "y":
            choices += string.ascii_uppercase
            break
        elif upper_within == "n":
            break
        else:
            print("Please insert 'y' or 'n'")

   # Loop for adding lowercase ascii characterset to choices
    while True:
        lower_within = input("Do you want lowercase letters in your password: y/n\n\n")
       
        if lower_within == "y":
            choices += string.ascii_lowercase
            break
        elif lower_within == "n":
            break
        else:
            print("Please insert 'y' or 'n'")
   
   # Randomly generate string from selected character sets 
    try:
        for i in range(length):
            password += secrets.choice(choices)

        print("Generated password:", password)
    except:
        # if user inputs no on each option it will not be generated
        IndexError 
        print("you choose none of the character sets and therefore no password will be generated \n")

     # if user input yes password and choices are resetted before next iteration
    another_password = input("Do you want to generate another password? (y for yes otherwise prec CTRL + C)\n\n")
    if another_password.lower() != 'y':
        break
    else:
        password = ""  
        choices = []   