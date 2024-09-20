'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

number = int(input("Enter a number: "))
result = number > 10 and number % 2 == 0 #checks if number is greater than 10 and even.
print(result)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes" #converts input to lowercase and checks if the user is a student.


if age < 18 or is_student: #if the user is under 18 or a student, set the price to 10.
    price = 10
else:  #otherwise, set the price to 20.
    price = 20

print(f"Ticket price: ${price}")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruit_list = ["apple", "banana", "orange", "grape", "mango"]
prompt = "Please enter the name of a fruit to check if it's in the list: "
fruit_name = input(prompt).lower() #takes input from the user and converts it to lowercase.

if fruit_name in fruit_list: #checks if the fruit is in the predefined list.
    print("Yes, that fruit is in the list.")
else: #if not in the list, prints a different message.
    print("No, that fruit is not in the list.")



'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

year = int(input("Enter a year: ")) 
is_century = year % 100 == 0 #checks if the year is a century year (divisible by 100).
is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) #checks if the year is a leap year based on leap year rules.

print(f"Century year: {is_century}")
print(f"Leap year: {is_leap}")


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

weight = float(input("Enter the weight of the order: "))
zone = input("Enter the destination zone (A/B): ").upper() #takes input for the destination zone and converts it to uppercase.

if weight < 0: #checks if the weight is negative and prints an error if so.
    print("Error: Order weight cannot be negative.")
elif zone == 'A': #if the zone is 'A', calculates the cost using $5 per kilogram.
    cost = weight * 5
    print(f"Shipping cost: ${cost}")
elif zone == 'B': #if the zone is 'B', calculates the cost using $7 per kilogram.
    cost = weight * 7
    print(f"Shipping cost: ${cost}")
else:
    print("Error: Invalid zone.")


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.

'''

a = float(input("Enter side length a: "))
b = float(input("Enter side length b: "))
c = float(input("Enter side length c: "))

if a + b <= c or a + c <= b or b + c <= a: #checks if the sides form a valid triangle.
    print("Not a triangle")
elif a == b == c: #if all sides are equal, it's an equilateral triangle.
    print("Equilateral")
elif a == b or b == c or a == c: #if two sides are equal, it's an isosceles triangle.
    print("Isosceles")
else: #otherwise, it's a scalene triangle (all sides different).
    print("Scalene")

