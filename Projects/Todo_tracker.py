todos = ['earn money', 'buy a porsche', 'drive the porsche']

while True:  # tarts infinite loop :)
    # isplays current todos with numbers
    print("\n-------------------------------------------")
    print("\nYour current todos are:")
    for i in range(len(todos)):  #loops through todos
        print(f"{i+1}. {todos[i]}") #prints each todo with its index
    print("\n-------------------------------------------")

    #displays menu options
    print("\nChoose an option:")
    print("1 - Add a todo")
    print("2 - Remove a todo")
    print("3 - Quit")  #option to quit the program if they want to

    print("\n-------------------------------------------")
    #gets the user's choice
    action = input("\nEnter an option (1/2/3): ").lower()
    
    if action not in ['1', '2', '3', 'add', 'remove', 'quit']:  #checks if choice is valid
        print("\nInvalid input. Please enter an option (add/remove/quit) or (1/2/3).")
        continue  #skips to next iteration of loop

    if action == '1' or action == 'add':  #if choice is 1 or add
        print("\n-------------------------------------------")
        #adds a new todo
        new_todo = input("\nWhat is your new to-do? ")
        todos.append(new_todo)  #adds new todo to the list

    elif action == '2' or action == 'remove':  #if choice is 2 or remove
        print("\n-------------------------------------------")
        #removes an existing todo by its index
        index_to_remove = input(f"\nWhich # todo would you like to remove (1-{len(todos)}): ")
        
        if not index_to_remove.isdigit():  #checks if input is a digit
            print("\nInvalid input. Please enter a number.")
            continue  #skip to next iteration of loop
        
        index_to_remove = int(index_to_remove)  #converts input to integer
        
        if 1 <= index_to_remove <= len(todos):  #checks if index is within valid range
            removed_todo = todos.pop(index_to_remove - 1)  #removes todo from the list
            print(f"\nRemoved: {removed_todo}")
        else:
            print("\nInvalid number. Please enter a valid index.")

    elif action == '3' or action == 'quit':  #if choice is 3 or quit
        print("\nBye byE!!")
        break  #exits the loop and ends the program