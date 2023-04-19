#RAMANDEEP SINGH
#22076254
# Create an empty dictionary to store the phone directory
a = {}

# Display the main menu options
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU ")
print("1. Add a record")
print("2. Search a record")
print("3. Change a record")
print("4. Delete a record")
print("5. Quit")

# using Loop until the user chooses to quit
while True:
    # taking input from user
    choice = int(input("\nEnter your choice: "))
    
    # Adding record
    if choice == 1:
        name = input("\nEnter name: ")
        number = input("Enter your 10-digit phone number: ")
        if len(number) != 10:
            print("Invalid phone number. Phone number must be 10-digit.")
        else:
            a[name] = number
            print("Record added")
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
    
    # Searching record
    elif choice == 2:
        name = input("\nEnter name to search: ")
        if name in a:
            print(name + ": " + a[name])
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
        else:
            print("Record not found")
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
    
    # Updating record
    elif choice == 3:
        name = input("\nEnter name: ")
        if name in a:
            number = input("Enter new 10-digit phone number: ")
            if len(number) != 10:
                print("Invalid phone number. Phone number must be 10-digit.")
                print("Menu ")
                print("1. Add a record")
                print("2. Search a record")
                print("3. Change a record")
                print("4. Delete a record")
                print("5. Quit")
            else:
                a[name] = number
                print("Record updated")
                print("Menu ")
                print("1. Add a record")
                print("2. Search a record")
                print("3. Change a record")
                print("4. Delete a record")
                print("5. Quit")
        else:
            print("Record not found")
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
    # Deleting record
    elif choice == 4:
        name = input("\nEnter name: ")
        if name in a:
            del a[name]
            print("Record deleted")
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
        else:
            print("Record not found")
            print("Menu ")
            print("1. Add a record")
            print("2. Search a record")
            print("3. Change a record")
            print("4. Delete a record")
            print("5. Quit")
    
    # To quit program
    elif choice == 5:
        break
    
    # if input is invalid
    else:
        print("\nInvalid choice. Please try again.")