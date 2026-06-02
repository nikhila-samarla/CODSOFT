# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact Added Successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- Contact List -----")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['Phone']}")

def search_contact():
    search = input("Enter Name or Phone Number: ")

    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["Phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])
            found = True
            break

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter Contact Name to Update: ")

    if name in contacts:
        contacts[name]["Phone"] = input("Enter New Phone Number: ")
        contacts[name]["Email"] = input("Enter New Email: ")
        contacts[name]["Address"] = input("Enter New Address: ")

        print("Contact Updated Successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter Contact Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break
    else:
        print("Invalid Choice! Please Try Again.")
