# My Contacts App

import json 
import os 

CONTACTS_FILE = 'myContacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
                contacts = json.load(f)
            print("Contacts were loaded successfully.")
            return contacts
        except json.JSONDecodeError:
            print("Error: Program could not decode JSON from myContacts.json. Starting with empty contats...")
            return []
        
        except IOError as e:
            print(f"Error: An error occours ... {e}. Starting with empty contats...")
            return []

    else:
        print("myContacts.json not found. Program try to use empty lists.")
        return []

def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False )
        print("Contacts saved successfully.")
    except IOError as e:
        print(f"Error saving {CONTACTS_FILE}: {e}")

def add_contacts(contacts):
    print("\n----- Add New Contact -----")
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone: ").strip()
    email = input("Enter contact email: ").strip()

    if not name or not phone:
        print("Name and Phone number are required.")
        return
    
    #Checking duplicted entries
    for contact in contacts:
        if contact['phone'] == phone:
            print(f"Error: phone number {phone} already exits for the name of {contact['name']}.")
            return
        
    contact = {
        'name': name,
        'phone': phone,
        'email': email if email else 'N/A'
    }

    contacts.append(contact)
    print(f"Contact {name} added successfully.")
    save_contacts(contacts)

def view_contacts(contacts):
    if not contacts:
        print("You have no contacts in your list.")
        return
    
    print("\n----- All contacts -----")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print("***********************")


def search_contacts(contacts):
    print("\n ----- Search Contact -----")
    search_term = input("Enter name to search: ").strip().lower()

    found_contacts = []
    for contact in contacts:
        if search_term in contact['name'].lower():
            found_contacts.append(contact)

    if not found_contacts:
        print(f"No contacts found with this name '{name}'.")
    else:
        print(f"\n ----- Found {len(found_contacts)} Contact(s) -----")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("***********************")

def del_contacts(contacts):
    print("\n ----- Delete Contact -----")
    search_term = input("Enter name to delete: ").strip().lower()

    original_len = len(contacts)
    contacts[:] = [contact for contact in contacts if 
                   search_term not in contact['name'].lower() and 
                   search_term not in contact['phone'].lower()]
    
    if len(contacts) < original_len:
        print(f"Contact '{search_term}' was deleted successfully.")
        save_contacts(contacts)

    else: 
        print(f"No contact found with this name '{search_term}'.")

def main_menu():
    print("\n----- My Contacts -----")
    print("***********************")
    print("1. Add Contacts")
    print("2. View all contacts")
    print("3. Search Contact")
    print("4. Delete contacts")
    print("5. Exit program")
    print("***********************")


def run_contacts_app():
    contacts = load_contacts()

    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contacts(contacts)

        elif choice == '2':
            view_contacts(contacts)
        
        elif choice == '3':
            search_contacts(contacts)

        elif choice == '4':
            del_contacts(contacts)

        elif choice == '5':
            print("Thank you for using my contact app. Goodbye!")
            break

        else:
            print("Invalid. Please, enter number 1 to 5 only.")

if __name__ == "__main__":
    run_contacts_app()
