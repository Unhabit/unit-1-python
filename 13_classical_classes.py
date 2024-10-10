"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

# a class called Person with attributes name and age.
class Person:
    def __init__(self, name, age):
        # initialize name and age attributes
        self.name = name
        self.age = age

    # introduce the person
    def introduce(self):
        # string introducing the person
        return f"Hi, my name is {self.name} and I am {self.age} years old."

person1 = Person("John", 25)
print(person1.introduce())  

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

# class Animal with an empty method called speak
class Animal:
    # Empty speak method to be overridden by subclasses
    def speak(self):
        pass

# Dog class inheriting from Animal and overriding speak method
class Dog(Animal):
    #speak method to return "Woof"
    def speak(self):
        return "Woof"

# Cat class inheriting from Animal and overriding speak method
class Cat(Animal):
    # speak method to return "Meow"
    def speak(self):
        return "Meow"

# objects of Dog and Cat classes and call their speak method
dog = Dog()
cat = Cat()

print(dog.speak())  
print(cat.speak())  



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""


# Class BankAccount with attributes balance and owner
class BankAccount:
    def __init__(self, owner, balance=0):
        # initialize owner and balance attributes
        self.owner = owner
        self.balance = balance

    # Method for depositing money, increases the balance
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."

    # Method for withdrawing money, decreases the balance if sufficient
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."

account = BankAccount("Alice", 100)
print(account.deposit(50))   
print(account.withdraw(30)) 
print(account.withdraw(200)) 

