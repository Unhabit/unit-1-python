"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        #try to perform the division operation
        result = num1 / num2
    except ZeroDivisionError:
        # i a ZeroDivisionError occurs (dividing by zero), this block will be executed
        print("Error: Cannot divide by zero.")
    else:
        #if no exception occurs, this block will be executed
        print("Result:", result)

# Example usage:
divide_numbers(10, 0)



"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        #try to open and read the file
        file = open(filename, 'r')
        contents = file.read()
    except FileNotFoundError:
        #if a FileNotFoundError occurs (file does not exist), this block will be executed
        print("Error: The file was not found.")
    else:
        #if no exception occurs, this block will be executed
        print("File contents:", contents)
    finally:
        #this block will always run, whether or not an exception occurred
        try:
            file.close()  #close the file if it was opened
        except NameError:
            #if the file variable was never created (due to an exception), this handles that case
            pass

# Example usage:
read_file("nonexistent.txt")


"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        #try to access the item at the given index
        item = lst[index]
    except IndexError:
        #if an IndexError occurs (index is out of range), this block will be executed
        print("Error: Index is out of range.")
    else:
        # if no exception occurs, this block will be executed
        print("Item:", item)

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)



"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:
        #try to retrieve the value for the given key
        value = dictionary[key]
    except KeyError:
        #if a KeyError occurs (key is not found in the dictionary), this block will be executed
        print("Error: Key not found in the dictionary.")
    else:
        #if no exception occurs, this block will be executed
        print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")



"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        #try to open and read the file
        file = open(filename, 'r')
    except FileNotFoundError:
        #if the file is not found, this block will be executed
        print("Error: File not found.")
    else:
        #if no exception occurs, this block will be executed
        contents = file.read()
        print("File contents:", contents)
    finally:
        #this block will always be executed, whether or not an exception occurs
        try:
            file.close()  # close the file if it was opened
            print("File closed.")
        except NameError:
            # if file wasn't opened (due to an exception), this handles the case
            print("No file was opened, so nothing to close.")

# Example usage:
process_file("example.txt")
