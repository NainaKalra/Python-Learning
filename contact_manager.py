import datetime  # we need this for storing dates like created_date and last_modified
from collections import Counter, defaultdict   # this is for statistics and duplicate finding

#1.1 Contact Data Structure design - 

def create_contact():
    """
    Ask the user for contact details and return a dictionary.
    Required fields: first name, last name, phone.
    Optional: email, address, category, notes.
    """
    # Required inputs (using while loop until user gives something)
    first_name = input("Enter First Name: ").strip()
    while not first_name:
        first_name = input("First Name is required. Please enter again: ").strip()

    last_name = input("Enter Last Name: ").strip()
    while not last_name:
        last_name = input("Last Name is required. Please enter again: ").strip()

    phone = input("Enter Phone Number (e.g., 123-456-7890): ").strip()
    while not phone:
        phone = input("Phone Number is required. Please enter again: ").strip()

    # Optional fields
    email = input("Email (optional): ").strip()
    street = input("Street (optional): ").strip()
    city = input("City (optional): ").strip()
    state = input("State (optional): ").strip()
    zip_code = input("Zip Code (optional): ").strip()
    category = input("Category (personal/work/family): ").strip().lower()

    if category not in ["personal", "work", "family"]:
        category = "personal"   # default if invalid category

    notes = input("Notes (optional): ").strip()

    today = datetime.date.today().isoformat()

    # storing contact as a dictionary
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email,
        "address": {
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code
        },
        "category": category,
        "notes": notes,
        "created_date": today,
        "last_modified": today
    }
    return contact


#1.2 Contact storage design -

contacts_db = {}   # will go like {"contact_001": {...}, "contact_002": {...}}

#Function to add contact-

def add_contact(contacts_db, contact_data):
    """Add a contact and generate a new ID (contact_001, contact_002, etc)."""
    contact_id = f"contact_{len(contacts_db) + 1:03d}" #3 digit ID :03d
    contacts_db[contact_id] = contact_data
    return contact_id


# Function to display contact-

def display_contact(contacts_db, contact_id):
    """Print one contact’s details in a readable way."""
    contact = contacts_db.get(contact_id)
    if not contact:
        print(f"No contact found with ID: {contact_id}")
        return False

    print(f"\n--- Contact {contact_id} ---")
    print(f"Name: {contact['first_name']} {contact['last_name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print("Address:")
    for key, value in contact["address"].items():
        print(f"  {key.capitalize()}: {value}")
    print(f"Category: {contact['category']}")
    print(f"Notes: {contact['notes']}")
    print(f"Created: {contact['created_date']}")
    print(f"Last Modified: {contact['last_modified']}")
    print("----------------------------")
    return True


# Function to list all contacts-

def list_all_contacts(contacts_db):
    """Show all contacts with ID, Name, and Phone."""
    if not contacts_db:
        print("No contacts in database.")
        return
    print("\n--- All Contacts ---")
    for cid, contact in contacts_db.items():
        print(f"{cid}: {contact['first_name']} {contact['last_name']} - {contact['phone']}")
    print("---------------------")


#1.3 Search and Retrieval- 

#Function to search contacts by name
def search_contacts_by_name(contacts_db, search_term):
    """Search contacts by first/last name (case-insensitive)."""
    results = {}
    search_term = search_term.lower()
    for cid, contact in contacts_db.items():
        if (search_term in contact["first_name"].lower()) or (search_term in contact["last_name"].lower()):
            results[cid] = contact
    return results

#to search by category

def search_contacts_by_category(contacts_db, category):
    """Return contacts in a given category."""
    results = {}
    for cid, contact in contacts_db.items():
        if contact.get("category", "").lower() == category.lower():
            results[cid] = contact
    return results

#to search by phone

def find_contact_by_phone(contacts_db, phone_number):
    """Find a contact by exact phone number."""
    for cid, contact in contacts_db.items():
        if contact.get("phone") == phone_number:
            return (cid, contact)
    return (None, None)


#2.1 Contact modification and deletion -

#to update -

def update_contact(contacts_db, contact_id, field_updates):
    """Update specific fields of a contact"""
    contact = contacts_db.get(contact_id)
    if not contact:
        print("No such contact.")
        return False

    for field, value in field_updates.items():
        if field in contact:
            contact[field] = value
        elif field in contact["address"]:
            contact["address"][field] = value
        else:
            print(f"Unknown field: {field}")

    contact["last_modified"] = datetime.date.today().isoformat()
    return True


# to delete a contact-

def delete_contact(contacts_db, contact_id):
    """Delete a contact after confirmation."""
    if contact_id in contacts_db:
        confirm = input(f"Delete {contact_id}? (y/n): ")
        if confirm.lower() == "y":
            del contacts_db[contact_id]
            print("Deleted successfully.")
            return True
    print("Contact not found or not deleted.")
    return False

#function to merge contacts-

def merge_contacts(contacts_db, contact_id1, contact_id2):
    """Merge two contacts. Keeps contact_id1 and removes contact_id2."""
    c1 = contacts_db.get(contact_id1)
    c2 = contacts_db.get(contact_id2)

    if not c1 or not c2:
        print("none of the contacts not found.")
        return None

    # Merge basic fields (prefer c2's values if not empty)
    for field in ['first_name', 'last_name', 'phone', 'email', 'category', 'notes']:
        if c2.get(field):  # if c2 has data, use it
            c1[field] = c2[field]

    # Merge address (field by field)
    for part in ['street', 'city', 'state', 'zip_code']:
        if c2['address'].get(part):
            c1['address'][part] = c2['address'][part]

    # Update last_modified (keep the newer one)
    c1['last_modified'] = max(c1['last_modified'], c2['last_modified'])

    # Remove the second contact
    del contacts_db[contact_id2]

    return contact_id1


# Data analysis and reporting - 

#function to generate contact stats-

def generate_contact_statistics(contacts_db):
    """
    Generate statistics:
    - total contacts
    - contacts by category
    - contacts by state
    - average per category
    - most common area code
    - number without email
    """
    stats = {
        "total_contacts": len(contacts_db),
        "contacts_by_category": {},
        "contacts_by_state": {},
        "average_contacts_per_category": 0.0,
        "most_common_area_code": None,
        "contacts_without_email": 0
    }

    # Counters are like smart dictionaries for counting (used Chatgpt to learn this :) )
    category_counter = Counter()
    state_counter = Counter()
    area_code_counter = Counter()

    for contact in contacts_db.values():
        # Count categories
        category_counter[contact["category"]] += 1

        # Count states
        state = contact["address"].get("state", "")
        if state:
            state_counter[state] += 1

        # Count area codes (first 3 digits before "-")
        phone = contact.get("phone", "")
        if phone and "-" in phone:
            area_code_counter[phone.split("-")[0]] += 1

        # Count missing emails
        if not contact.get("email"):
            stats["contacts_without_email"] += 1

    # Saving the  results
    stats["contacts_by_category"] = dict(category_counter)
    stats["contacts_by_state"] = dict(state_counter)
    stats["average_contacts_per_category"] = (
        len(contacts_db) / len(category_counter) if category_counter else 0
    )
    if area_code_counter:
        stats["most_common_area_code"] = area_code_counter.most_common(1)[0][0]

    return stats

# function to find duplicates

def find_duplicate_contacts(contacts_db):
    """
    This function finds possible duplicate contacts.

    A contact is considered duplicate if:
    - Two contacts have the same phone number
    - OR two contacts have the same email
    - OR two contacts have the same first+last name

    """

    # Where we will store the duplicates
    duplicates = {
        "phone_duplicates": [],
        "email_duplicates": [],
        "name_duplicates": []
    }

    #dictionaries that will help to check duplicates
    phone_map = {}  # phone -> [contact_ids]
    email_map = {}  # email -> [contact_ids]
    name_map = {}   # name -> [contact_ids]

    # Going through each contact
    for cid, info in contacts_db.items():
        phone = info.get("phone")
        email = info.get("email")
        name = (info.get("first_name"), info.get("last_name"))

    # Grouping by phone
        if phone:
            phone_map.setdefault(phone, []).append(cid)

    # Grouping by email
        if email:
            email_map.setdefault(email, []).append(cid)

    # Grouping by name
        name_map.setdefault(name, []).append(cid)

    # Adding only groups that have more than 1 contact
    for ids in phone_map.values():
        if len(ids) > 1:
            duplicates["phone_duplicates"].append(ids)

    for ids in email_map.values():
        if len(ids) > 1:
            duplicates["email_duplicates"].append(ids)

    for ids in name_map.values():
        if len(ids) > 1:
            duplicates["name_duplicates"].append(ids)

    return duplicates


# User Interface and Integration-

#3.1 Command Line Interface

#creating a menu-

def main_menu():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. List All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Generate Statistics")
        print("7. Find Duplicates")
        print("8. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            contact = create_contact()
            cid = add_contact(contacts_db, contact)
            print(f"Contact added with ID {cid}")

        elif choice == "2":
            term = input("Enter name to search: ")
            results = search_contacts_by_name(contacts_db, term)
            for cid in results:
                display_contact(contacts_db, cid)

        elif choice == "3":
            list_all_contacts(contacts_db)

        elif choice == "4":
            cid = input("Enter contact ID to update: ")
            field = input("Field to update (first_name, last_name, phone, email, category, notes, city, state): ")
            value = input(f"Updated value for {field}: ")
            update_contact(contacts_db, cid, {field: value})

        elif choice == "5":
            cid = input("Enter contact ID to delete: ")
            delete_contact(contacts_db, cid)

        elif choice == "6":
            stats = generate_contact_statistics(contacts_db)
            print("\n.....Contact Statistics.....")
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choice == "7":
            duplicates = find_duplicate_contacts(contacts_db)
            print("\n.....Duplicate Contacts.....")
            for dtype, groups in duplicates.items():
                print(f"{dtype}: {groups}")

        elif choice == "8":
            print("Exiting... ThankYou.... Bye :)")
            break

        else:
            print("Your choice is invalid,please try again.")


# to run the program
if __name__ == "__main__":
    print("......Welcome to Contact Manager!.....")
    main_menu()
