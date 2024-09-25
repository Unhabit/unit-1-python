"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

string = "Hello World!"

#using a for loop to print each character
for char in string: #I used for each character in string print each character
    print(char)


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

numbers = [10, 20, 30, 40, 50]
total_sum = 0

for num in numbers: #using a for loop to iterate through each element in the list
    total_sum += num    #added the current element to the total sum

print("The sum of the list elements is:", total_sum)


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

sentence = "Chicken over rice is the best"

#spliting the sentence into a list of words
words = sentence.split()

#using a for loop to iterate through each word in the list
for word in words:
    print(f"The length of '{word}' is {len(word)}")


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
student_grades = { #dictionary of students and grades
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

#iterating through the dictionary and printing the key-value pairs
for student, grade in student_grades.items():
    print(f"Student: {student}, Grades: {grade}")


#The output shows the students and their grades. The order is what I expected because Python keeps the order of keys the same as when they were added to the dictionary.