"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]
print(car_brands)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

food = []
food.append("Chicken Over Rice") #append adds a item at the end of the list
food.append("Beef Biryani") #append adds a item at the end of the list
print(food)


"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi", "Fiat"]
car_brands.remove("Audi") # used the remove function to remove a element

print(car_brands)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]
car_brands[3] = "Koenigsegg" # made index 3 in the variable car_brands "Koenigsegg"

print(car_brands)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]

new_brands= ["Maserati", "Rolls Royce", "Honda", "Toyota", "Dodge"]

#append the entire list as a single element
car_brands.append(new_brands)

print(car_brands)


"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]

# Delete element at index 2 
del car_brands[2]

print(car_brands)


"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]

first_two_brands = car_brands[0:2] #made a new variable that only prints index 0 and index 1

print(first_two_brands)


"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

car_brands = ["Porsche", "BMW", "Mercedes", "Audi"]

#another list to extend the original list with
more_brands = ["Tesla", "Ferrari", "Lamborghini"]

#extending the original list
car_brands= car_brands+more_brands

print(car_brands)
