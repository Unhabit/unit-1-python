#code 2
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ": # added a space because it didn't define anything in if char
       count += 1

print(count)

#code 3

print("give me a number")
n = int(input())  #converts input to integer

for num in range(1, n+1):  #loop from 1 to n 
    if num % 2 == 0:  #correct condition for even numbers
        print(num, "is even.")
    else:
        print(num, "is odd.")


# code 4

num2 = int(input("Enter an integer: "))

if num2 < 0:
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num2 + 1):  #correcting the range
        result *= i   

    print("Factorial of " + str(num2) + " is " + str(result))  #convert num to string same for result


#code 5

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:  #checks for the correct password
        print("Correct password!")
        break  #exit the loop if the password is correct
    else:
        print("Incorrect password")

    if attempts >= 3:  #checks if attempts exceed 3
        print("Too many attempts")
        break
