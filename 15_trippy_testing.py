"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """
  if b == 0:
    return None
  else:
    return a / b


assert divide(10, 2) == 5   # True: 10 divided by 2 should return 5
assert divide(9, 3) == 4    # False: 9 divided by 3 should return 3, not 4

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


assert factorial(0) == 1      # True: Factorial of 0 is 1
assert factorial(3) == 10     # False: Factorial of 3 is 6, not 10

"""
Exercise 3: String Reverse !
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """
  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string


assert reverse_string("hello") == "olleh"     # True: "hello" reversed should be "olleh"
assert reverse_string("world") == "dlorw"     # False: "world" reversed is "dlrow", not "dlorw"

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5  # True: The 5th Fibonacci number is 5
assert fibonacci(6) == 20 # False: The 6th Fibonacci number is 8, not 20

"""
Exercise 5: Email Validation
"""
import re

def is_valid_email(email):
  """Determines whether email is valid or not.

  Args:
    email: The email to validate.

  Returns:
    Boolean value if the email is valid.
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None


assert is_valid_email("test@example.com") == True       # True: Valid email
assert is_valid_email("invalid-email") == True          # False: Invalid email (missing domain)
