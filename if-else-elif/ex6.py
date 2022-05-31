# Make a program that asks for a password 
# and prints Welcome!, Access denied or 
# You didn't enter anything depending on
#  whether the user entered the correct password, 
#  a wrong password, or nothing at all by 
#  pressing Enter without typing anything.

password = input("Enter your password: ")

if password =="pingas": 
    print("Welcome!")
elif password == "":
    print("You didn't enter anything")

else:
    print("Access denied.")
