"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
float_variable = 2.99  #float variable

int_variable = int(float_variable) #converting the float variable to an integer

#printing the orginal float into a converted integer
print("Original float:", float_variable)  
print("Converted integer:", int_variable)  


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
#taking a number as input from the user

number = float(input("Enter a number: ")) #making it so the number they enter is allwoing decimal points

#checking if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")  #if the number is greater than 0, it's positive
elif number < 0:
    print("The number is negative.")  #if the number is less than 0, it's negative
else:
    print("The number is zero.")  #if the number is neither greater or less than 0, it's zero

"""
TASK 3:
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
#inputing 2 numbers 

integer_number = int(input("Enter an integer: "))  #taking an integer input
float_number = float(input("Enter a float: "))  #taking a float input

#operations thingy

addition = integer_number + float_number  #adding the integer and float
subtraction = integer_number - float_number  #subtracting the float from the integer
multiplication = integer_number * float_number  #multiplying the integer and float
division = integer_number / float_number  #dividing the integer by the float

#printing the results of each operation things

print("Addition:", addition)  #displaying the result of addition
print("Subtraction:", subtraction)  #displaying the result of subtraction
print("Multiplication:", multiplication)  #displaying the result of multiplication
print("Division:", division)  #displaying the result of division

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#creating a dictionary with fruit names as keys and their quantities as values
fruit_quantities = {
    "pear": 4,      #the key is "pear" and the value is 4
    "mango": 6,      #the key is "mango" and the value is 6
    "orange": 8,      #the key is "orange" and the value is 8
    "hog plum": 10      #the key is "hog plum" and the value is 10
}

#printing the quantity of one of the fruits
print("Quantity of hog plum:", fruit_quantities["hog plum"])  #accessing the quantity of "hog plum" from the dictionary

#hog plum is the best fruit of fruits no debate
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
# Creating a string variable that represents a list of numbers
numbers_string = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17"

# Converting the string into a tuple
numbers_tuple = tuple(map(int, numbers_string.split(", ")))  #split the string by ", " , convert each part to an integer, and then create a tuple

#print of orginal and tuple
print("Original string:", numbers_string)  #displaying the original string
print("Converted tuple:", numbers_tuple)  #displaying the tuple after conversion
