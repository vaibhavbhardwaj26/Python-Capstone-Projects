import sys
print("--------------------------------------------------")
print("Hello! Welcome to my Phone directory")
print("--------------------------------------------------")

def menu():
    print("--------------------------------------------------")
    print("\t\tPHONE DIRECTORY", flush=False)
    print("--------------------------------------------------")
    print("You can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Update a contact")
    print("3. Remove an existing contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Delete all contacts")
    print("7. Exit phonebook")
    mychoice = int(input("Please enter your choice: "))
    return mychoice

def adding(pb):
    add = []
    for i in range(len(pb[0])):
        if i == 0:
            add.append(str(input("*Enter name*:")))
        if i == 1:
            add.append(int(input("*Enter Number*:")))
        if i == 2:
            add.append(str(input("Enter Email Address:")))
    pb.append(add)
    return pb

def update(pb):
    choice = int(input("Choose a cateogory to update\n\n1. Name\n2. Number\n3. Email-id\n\nPlease enter the category number: "))
    check = -1
    if choice == 1:
        cont = str(input("Enter the name you want to update:"))
        up = str(input("Enter the updated name:"))
        for i in range(len(pb)):
            if cont == pb[i][0]:
                pb[i][0] = up
                check = i

    elif choice == 2:
        cont = int(input("Enter the number you want to update:"))
        up = str(input("Enter the updated number:"))
        for i in range(len(pb)):
            if cont == pb[i][1]:
                pb[i][1] = up
                check = i

    elif choice == 3:
        cont = str(input("Enter the email you want to update:"))
        up = str(input("Enter the updated email:"))
        for i in range(len(pb)):
            if cont == pb[i][2]:
                pb[i][2] = up
                check = i

    else:
        print("Invalid Search Category")
        return -1
    if check == -1:
        return -1
    else:
        display(pb)
        return check

def remove(pb):
    cont = str(input("Enter the name of the contact to remove:"))
    nocont = 0
    for i in range(len(pb)):
        if cont == pb[i][0]:
            nocont += 1
            print(pb.pop(i))
            print("This Contact has now been removed")
            return pb
        if nocont == 0:
            print("SORRY!, You Have Entered Wrong contact.\ PLEASE try again later")
            return pb
            
def search(pb):
    choice = int(input("Choose the search cateogory\n\n1. Name\n2. Number\n3. Email-id\n\
 \nPlease enter the category number: "))
    t = []
    check = -1
    if choice == 1:
        cont = str(input("Enter the name you want to search:"))
        for i in range(len(pb)):
            if cont == pb[i][0]:
                check = i
                t.append(pb[i])

    elif choice == 2:
        cont = int(input("Enter the number you want to search:"))
        for i in range(len(pb)):
            if cont == pb[i][1]:
                check = i
                t.append(pb[i])

    elif choice == 3:
        cont = str(input("Enter the email you want to search:"))
        for i in range(len(pb)):
            if cont == pb[i][2]:
                check = i
                t.append(pb[i])

    else:
        print("Invalid Search Category")
        return -1
    if check == -1:
        return -1
    else:
        display(t)
        return check

def display(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])

def delete(pb):
    return pb.clear()

def exit():
    print("--------------------------------------------------")
    sys.exit("THANK YOU FOR USING PHONEBOOK")

def phonedirect():
    phonebook = []
    print('--------------------------------------------------')
    print(f"Status of Phonebook:{phonebook}")
    print('--------------------------------------------------')
    rows,cols = int(input('Please enter initial number of contacts :')),3

    for i in range(rows):
        print(f'\nEnter the Contact NO.{i+1} in the following order')
        print("NOTE: * indicates mandatory fields")
        print('--------------------------------------------------')
        temp=[]
        for j in range(cols):
            if j == 0:
                temp.append(str(input("*Enter name*:")))
                if temp[j]==' ' or temp[j]=='':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")

            if j == 1:
                temp.append(int(input("*Enter Number*:")))

            if j == 2:
                temp.append(str(input("Enter Email Address:")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        phonebook.append(temp)
    print('--------------------------------------------------')
    print("STATUS OF CURRENT PHONEBOOK")
    print(phonebook)
    print('--------------------------------------------------')
    return phonebook

ch = 1
pb = phonedirect()
while ch in (1,2,3,4,5,6):
    ch = menu()
    if ch == 1:
        pb = adding(pb)
    elif ch == 2:
        u = update(pb)
        if u == -1:
            print("The contact does not exist. Please try again")
    elif ch == 3:
        pb = remove()
    elif ch == 4:
        d = search(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        pb = display(pb)
    elif ch == 6:
        pb = delete(pb)
    else:
        exit()
