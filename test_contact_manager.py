# Import contact_manager as cm (short form)

import contact_manager as cm

# Test 1: Create a new contact
def test_create_contact():
    # A fake contact to test with
    c = {
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '123',
        'email': '',
        'address': {
            'street': '',
            'city': '',
            'state': '',
            'zip_code': ''
        },
        'category': 'personal',
        'notes': '',
        'created_date': '2024-01-01',
        'last_modified': '2024-01-01'
    }

    # Adding the contact to the database
    cid = cm.add_contact(cm.contacts_db, c)

    # Checking if it was really added
    assert cid in cm.contacts_db
    print(".....test_create_contact passed.....")


# Test 2: Search contacts by name
def test_search_functionality():
    results = cm.search_contacts_by_name(cm.contacts_db, "Test")

    # Make sure we got some results
    assert results
    print(".....test_search_functionality passed.....")


# Test 3: Update and delete a contact
def test_contact_operations():
    # Pick the first contact ID from the database
    cid = list(cm.contacts_db.keys())[0]

    # Update the notes field
    cm.update_contact(cm.contacts_db, cid, {'notes': 'updated'})

    # Check if it was updated correctly
    assert cm.contacts_db[cid]['notes'] == 'updated'

    # Now delete the contact
    cm.delete_contact(cm.contacts_db, cid)
    print(".....test_contact_operations passed.....")


# Test 4: Check statistics
def test_data_analysis():
    stats = cm.generate_contact_statistics(cm.contacts_db)

    # Make sure stats has "total_contacts"
    assert 'total_contacts' in stats
    print(".....test_data_analysis passed.....")


# Run all tests one by one
def run_all_tests():
    test_create_contact()
    test_search_functionality()
    test_contact_operations()
    test_data_analysis()
    print("\n .....Congrats! All tests passed!.....")


# To run automatically if file is executed directly
if __name__ == "__main__":
    run_all_tests()
