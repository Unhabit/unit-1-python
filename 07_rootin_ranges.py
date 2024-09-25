"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

for i in range(1, 11): #1 is start 11 is the end. But 11 doesn't get counted
    print(i)


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

for i in range(900, 1001, 10): #900 is the start 1001 is the end and 10 is how much its going up by. 1001 doesnt count. 1001 is not counted
    print(i)



"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for i in range(1, 101, 9): # 1 is what it starts at 101 is where it should end and 9 is how much its going up by from 1. 101 is not counted.
    print(i)


"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

total_sum = 0

#loop through numbers from 1 to 10
for i in range(1, 11):
    total_sum += i  #adding each number to total_sum
print("The sum of numbers from 1 to 10 is:", total_sum)


"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

*
* *
* * *
* * * *
* * * * *

- Explain the iterative process that this code executes to get that output

The outer loop iterates from 0 to 4 for each row, while the inner loop prints an increasing number of asterisks based on the current row index. This creates a right-angled triangle pattern of asterisks.

"""
rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()