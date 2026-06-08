'''----------------------------------------------------
Problem Statement: Contact Directory Management System

Sample Data

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

Tasks
• Display all contact names in alphabetical order.
• Count the total number of contacts.
• Search for a given contact name.
• Create a list of contacts whose names start with a vowel.
• Stop the search using break once the required contact is found.
----------------------------------------------------'''

# creating dictionary to store contact names and phone numbers

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

#--------------------------------------------------
# Task-1 : Display all contact names in alphabetical order

# convert dictionary keys into a list
contact_names = list(contacts.keys())

# sort the list alphabetically
contact_names.sort()

print("Contact Names In Alphabetical Order :")

# display all names one by one
for name in contact_names:
    print(name)

#--------------------------------------------------
# Task-2 : Count the total number of contacts

count = 0

# traverse all contacts
for contact in contacts.values():
    count += 1

print("\nTotal Number Of Contacts :", count)

#--------------------------------------------------
# Task-3 : Search for a given contact name

name = input("\nEnter the name to search : ")

found = False

# traverse all contact names
for contact_name in contacts.keys():

    # check for exact match
    if name == contact_name:

        print("Contact Found")
        print("Name :", contact_name)
        print("Phone Number :", contacts[contact_name])

        found = True

        # stop searching once contact is found
        break

# executed if contact is not found
if found == False:
    print("Contact Not Found")

#--------------------------------------------------
# Task-4 : Create a list of contacts whose names start with a vowel

vowel_contacts = []

# traverse all contact names
for name in contacts.keys():

    # check whether first character is a vowel
    if name[0] in "AEIOUaeiou":
        vowel_contacts.append(name)

print("\nContacts Starting With Vowel :")
print(vowel_contacts)

#--------------------------------------------------
# Task-5 : Stop the search using break once the required contact is found

name = input("\nEnter the contact name to search again : ")

for contact_name in contacts.keys():

    # check whether contact exists
    if name == contact_name:

        print("Contact Found")

        # stop loop immediately after finding contact
        break

else:
    print("Contact Not Found")

#--------------------------------------------------

'''
Sample Output:

Contact Names In Alphabetical Order :
Amit
Anjali
Arjun
Karan
Neha
Pooja
Priya
Rahul
Rohan
Sneha

Total Number Of Contacts : 10

Enter the name to search : Priya

Contact Found
Name : Priya
Phone Number : 9876543211

Contacts Starting With Vowel :
['Amit', 'Anjali', 'Arjun']

Enter the contact name to search again : Rahul

Contact Found
'''
