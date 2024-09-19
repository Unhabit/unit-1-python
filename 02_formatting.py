"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
correct_password = "Password@123!"

user_input = input("Enter your password: ")

#checking if the user's input matches the correct password (ignores case sensitivity)
if user_input.lower() == correct_password.lower():
    #if the password matches, accepted
    print("Access granted.")
else:
    #if the password does not match, denied
    print("Incorrect password. Access denied.")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
user_input2 = input("Enter a string: ")

#checking if the string is empty
if user_input2 == "" " ":
    #if the input is an empty string, print "invalid" 
    print(f"'{user_input2}' is invalid") #used f string to get variable value
else:
    #if the input is not empty, print "valid" 
    print(f"'{user_input2}' is valid") #used f string to get variable value


"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
user_input3 = input("Enter a sentence: ")

#using str.replace() with case folding to handle case-insensitivity
updated_input = user_input3.replace("cat", "dog").replace("Cat", "Dog").replace("CAT", "DOG") #made it so every time they say cat or cats it will be replaced as dog or dogs

#output of the updated string
print(f"Updated sentence: {updated_input}") #used f string to get variable value


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = input("Enter your name: ")

age = input("Enter your age: ")

print(f"Hey {name} how old are you?") #used f string to get variable value
print(f"{name} : I just turned {age}") #used f string to get variable value


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
num_1 = float(input("Enter a float number: ")) #float 1
num_2 = float(input("Enter another float number: ")) # float 2

if num_2 != 0:
    quotient = num_1 / num_2
    print(f"The quotient is: {quotient:.1f}") #used f to get variable value. Then used the .1f that makes it so its down 1 decimal of the output
else:
    print("Error")
