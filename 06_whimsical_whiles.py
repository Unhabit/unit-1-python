"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

i=0
while i<10: # made the while loop until 10
    i+=1 # adds 1 until condition becomes false
    print(i)


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

a=10
while a>=1: # 
    print(a)
    a-=1 # subtracts 1 

    
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

num = int(input("Enter a number to find its factorial: "))

factorial = 1
h = num

#while loop to calculate factorial
while h > 0:
    factorial *= h  #multiply factorial by the current value of i
    h -= 1  #subtracts 1

print(f"The factorial of {num} is {factorial}.")


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

correct_password = "python123"

guess = input("Guess the password: ")

#while loop to keep asking until the correct password is guessed
while guess != correct_password:
    print("Incorrect password, try again.")
    guess = input("Guess the password: ")

#when the loop ends, they guessed the right password
print("Congratulations! You've guessed the correct password.")


""" Do not need to do
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""



"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

n = int(input("Enter the number of Fibonacci numbers to print: "))

#initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

#while loop to generate Fibonacci numbers
while count < n:
    print(a) 
    a, b = b, a + b  #update values for the next Fibonacci number
    count += 1  # adds 1

