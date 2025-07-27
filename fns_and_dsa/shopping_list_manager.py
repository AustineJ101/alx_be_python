

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    def add_item(item):
        nonlocal shopping_list
        shopping_list.append(item)
   
    def remove_item(item):
        nonlocal shopping_list
        shopping_list.remove(item)


    def display_list():
        for item in shopping_list:
            print(f" - {item}")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item you want to add: ")
            add_item(item)
        elif choice == "2":
            item = input("Enter item you want to remove: ")
            remove_item(item)
        elif choice == "3":
            display_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else: 
            print("Invalid Choice. Please try again.")
    
main()


