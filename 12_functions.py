
def greet(name):  # This function takes a name as a parameter and prints a greeting message.
    print(f"Hello, {name}!")

greet("Nahid")  # Example call to greet function.


def square(num):  # This function takes an integer as an argument and returns its square.
    return num * num

print(square(5))  # Example call to square function.


def is_even(num):  # This function takes a number as an argument and returns True if the number is even, False otherwise.
    return num % 2 == 0

print(is_even(4))  # Example call to check if a number is even.


def area_of_rectangle(length, width):  # This function takes the length and width of a rectangle and returns its area.
    return length * width

print(area_of_rectangle(10, 5))  # Example call to area_of_rectangle function.


def celsius_to_fahrenheit(celsius):  # This function takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit.
    return (celsius * 9/5) + 32  # Formula for Celsius to Fahrenheit conversion.

print(celsius_to_fahrenheit(0))  # Example call to celsius_to_fahrenheit function.


def average(numbers):  # This function takes a list of numbers and returns the average (mean) of those numbers.
    return sum(numbers) / len(numbers)  # It sums the numbers and divides by the count to get the average.

print(average([1, 2, 3, 4, 5]))  # Example call to average function.


def calculate_total(price, quantity, discount=0):  # This function takes price and quantity, and optionally a discount.
    total = price * quantity  # It calculates the total by multiplying price and quantity.
    if discount:  # If a discount is provided, it reduces the total based on the discount percentage.
        total -= total * (discount / 100)  
    return total

print(calculate_total(100, 5))   # without discount
print(calculate_total(100, 5, 10))   # with dicsount
