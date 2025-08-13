#welcome to my shopping list app
#this file contains the main logic for managing a shopping list
'''
step 1: create a list to hold the shopping items
step 2: define functions to add, remove, and view items in the list
step 3: implement a simple user interface to interact with the shopping list
step 4: allow the user to exit the app
'''
shopping_list=[]
def add_items(item):
 shopping_list.append(item)
def remove_items(item):
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} not found in the shopping list.")

def view_items():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")
        
# Main loop to interact with the user
while True:
    x=int(input("Enter 1 to add items, 2 to remove items, 3 to view items, or 4 to exit: "))
    if x == 1:
        item = input("Enter the item to add: ")
        add_items(item)
    elif x==2:
        remove_items(input("Enter the item to remove: "))
    elif x==3:
        view_items()
    elif x==4:
        print("Exiting the shopping list app. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")