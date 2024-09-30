#file to store todos
FILENAME = "to-do.txt"

#load existing todos if the file exists, otherwise start with an empty list
file = open(FILENAME, 'r') if 'to-do.txt' in open(FILENAME, 'a+').name else None

if file:
    todos = file.read().splitlines()  #reads each line as a todo item
    file.close()
else:
    todos = []  #if the file doesn't exist, start with an empty list

#main application loop
while True:  #tarts infinite loop :)
    #display current todos with numbers
    print("\n-------------------------------------------")
    print("\nYour current todos are:")
    for i in range(len(todos)):  #loops through todos
        print(f"{i+1}. {todos[i]}")  #prints each todo with its index
    print("\n-------------------------------------------")

    #display menu options
    print("\nchoose an option:")
    print("1 - add a todo")
    print("2 - remove a todo")
    print("3 - quit")  #option to quit the program

    print("\n-------------------------------------------")
    #get the user's choice
    action = input("\nEnter an option (1/2/3): ").lower()

    if action not in ['1', '2', '3', 'add', 'remove', 'quit']:  #checks if choice is valid
        print("\nInvalid input. please enter an option (add/remove/quit) or (1/2/3).")
        continue  #skips to the next iteration of loop

    if action == '1' or action == 'add':  #if choice is 1 or add
        print("\n-------------------------------------------")
        #add a new todo
        new_todo = input("\nWhat is your new to-do? ")
        todos.append(new_todo)  #add new todo to the list

    elif action == '2' or action == 'remove':  #if choice is 2 or remove
        print("\n-------------------------------------------")
        #remove an existing todo by its index
        index_to_remove = input(f"\nWhich # todo would you like to remove (1-{len(todos)}): ")
        
        if not index_to_remove.isdigit():  #checks if input is a digit
            print("\nInvalid input. please enter a number.")
            continue  #skip to the next iteration of loop
        
        index_to_remove = int(index_to_remove)  #converts input to integer
        
        if 1 <= index_to_remove <= len(todos):  #checks if index is within valid range
            removed_todo = todos.pop(index_to_remove - 1)  #removes todo from the list
            print(f"\nRemoved: {removed_todo}")
        else:
            print("\nInvalid number. please enter a valid index.")

    elif action == '3' or action == 'quit':  #if choice is 3 or quit
        print("\nSaving your todos and exiting...")
        #save the todos to the file
        with open(FILENAME, 'w') as file:
            for todo in todos:
                file.write(todo + "\n")  #writes each todo on a new line
        break  #exits the loop and ends the program