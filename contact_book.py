def add_contact(name, mobno, email):
    with open("contact_file.txt", "a") as f:
        f.write(f"Name: {name} \nMobile number: {mobno} \nEmail: {email} \n\n")
    
def view_contacts():
    with open("contact_file.txt","r") as f:
        content = f.read()
        print(content)

def search_contact():
    name =input("Enter name : ")
    found = False

    with open("contact_file.txt","r") as f:
        lines = f.readlines()

        for i in range(0,len(lines),4):
            if name.lower() in lines[i].lower():
                print("\nContact found!\n")
                print(lines[i], end ="")
                print(lines[i+1], end = "")
                print(lines[i+2], end ="")
                found =  True
                break

def delete_contact():
    name = input("Enter Contact Name to Delete : ") 
    found =  False

    with open("contact_file.txt","r") as f :
        lines = f.readlines()

    new_lines = []

    for i in range(0, len(lines), 4):
        if  name.lower() in lines[i].lower():
            found = True
            
            print("\nContact Found!")
            print(lines[i], end="")
            print(lines[i+1], end="")
            print(lines[i+2], end="")

            continue
            
        new_lines.append(lines[i])
        new_lines.append(lines[i+1])
        new_lines.append(lines[i+2])
        new_lines.append(lines[i+3])

    if found:
        with open("contact_file.txt","w") as f:
            f.writelines(new_lines)
        print("Contact Deleted Successfully!")
    else :
        print("Contact Not Found!")


def edit_contacts():
    name = input("Enter name to edit : ")
    found = False

    with open("contact_file.txt","r") as f :
        lines = f.readlines()

    for i in range(0, len(lines), 4) :
        if name.lower() in lines[i].lower():
            found = True

            print("\nContacts Found!")
            print(lines[i], end="")
            print(lines[i+1], end="")
            print(lines[i+2], end="")

            new_name = input("\nEnter New Name : ")
            new_mobno = input("Enter New Mobile Number : ")
            new_email = input("Enter New Email : ")

            lines[i] = f"Name : {new_name}\n"
            lines[i+1] = f"Mobile number : {new_mobno}\n"
            lines[i+2] = f"Email : {new_email}\n"
            break

    if found:
        with open("contact_file.txt","w") as f :
            f.writelines(lines)
        print("\nContact Updated Successfully!")
    else : 
        print("\nContact Not Found!")

def total_contacts():
    try:
        count = 0
        with open("contact_file.txt","r") as f:
            for line  in f :
                count += 1
            print("\n\nTotal number of Contacts : ",count//4)
    except FileNotFoundError:
        print("\n\nTotal number of Contacts : 0")

while True:
    print("\n\n- - - - - - - - - - - Contact Book - - - - - - - - -\n\n")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Total Number of Contacts")
    print("7. Exit")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    n = int(input("Enter Your Choice : "))
    if n == 1 :
        name = input("Enter your name : ")
        mobno = input("Mobile number : ")
        email = input("Email : ")
        add_contact(name, mobno, email)
        print("Details added!")
    elif n == 2:
        view_contacts()
    elif n == 3 :
        search_contact()
    elif n == 4 :
        delete_contact()
    elif n == 5 :
        edit_contacts()
    elif n == 6 :
        total_contacts()
    elif n == 7:
        exit()
    else :
        print("Invalid Choice!")
