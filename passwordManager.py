"""
Description: Finish the code to create a password manager


Author: Hannelore Sanokklis
Class: CSI-160-01
Assignment: Password Manager
Due Date: 11/29/2023


Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


import pickle
import sys
#import pwnedpasswords

# The password list - We start with it populated for testing purposes
entries = {'yahoo': {'username': 'johndoe', 'password': 'cus#u%S tu', 'url': 'https://www.yahoo.com'},
           'google': {'username': 'johndoe', 'password': '`q$$( #tABCD^ %fu#*W  t', 'url': 'https://www.google.com'}}

# The password file name to store the data to
password_file_name = "PasswordFile.pickle"
# The encryption key for the caesar cypher
encryption_key = 16

menu_text = """
What would you like to do:
1. Open password file
2. Add an entry
3. Lookup an entry
4. Save password file
5. Quit program
6. Print dictionary for testing
7. Delete Entry
8. Edit Entry
Please enter a number (1-8): """


def password_encrypt(unencrypted_message, key):
    """Returns an encrypted message using a caesar cypher

    :param unencryptedMessage (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    """
    result_string = ''
    min_limit = 32
    max_limit = 126
    for character in unencrypted_message:
        value = ord(character) - min_limit + key
        value = value % (max_limit - min_limit + 1)
        value = value + min_limit
        result_string = result_string + chr(value)
    return result_string

def password_decrypt(encrypted_message, key):
    """Returns a decrypted message.

    :param encrypted_message (string):
    :param key (int) The offset that was used to encrypt the message
    :return (string): The decrypted message
    """
    return password_encrypt(encrypted_message, -key)

def load_password_file():
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a pickle file in the correct format
    """
    global entries, encryption_key
    try:
        entries, encryption_key = pickle.load(open(password_file_name, "rb"))
    except Exception as e:
        print("Something went wrong. Try Again.")
        print(str(e))


def save_password_file():
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    try:
        pickle.dump((entries, encryption_key), open(password_file_name, "wb"))
    except Exception as e:
        print("Something went wrong. Try Again.")
        print(str(e))

def add_entry():
    """Adds an entry with an entry title, username, password and url

    Includes all user interface interactions to get the necessary information from the user
    """

    entry_title = input("Please give your entry a title: ")
    username = input("Enter the username for your account: ")
    #encrypts the password that is inputted by the user
    password = password_encrypt(input("Enter the password for your account: "), encryption_key)
    url = input("Enter the URL for your account: ")

    #dictionary of dictonaries to store each entry
    entries[entry_title] = {'username': username, 'password': password, 'url': url}

def print_entry():
    """
    Asks the user for the name of the entry and prints all related information in a pretty format. Includes all information about an entry.

    I don't feel like I need a try/except for the dictionary keys since I used an if statement
    """
    print("Which entry do you want to lookup the information for? ")
    for key in entries:
        print(key)
    entry = input('Enter entry name: ')
    if entry in entries:
        data = entries[entry]
        print("The username is", data['username'])
        print("The password is", password_decrypt(data['password'], encryption_key))
        print("The URL for this account is", data['url'])
    else:
        print("Does not exist, please try again or pick another option")

def delete_entry():
    """
        Asks the user for what entry they would like to delete and deletes the entry

        I don't feel like I need a try/except for the dictionary keys since I used an if statement
        """
    print("Which entry do you want to delete?")
    for key in entries:
        print(key)

    entry = input('Enter entry name: ')

    if entry in entries:
        entries.pop(entry)
        print("Entry Deleted")
    else:
        print("Entry does not exist.")

def edit_entry():
    """
    Asks the user for what data they would like to edit within an entry and edits it

    I don't feel like I need a try/except for the dictionary keys since I used an if statement
    """
    print("Which entry do you want to edit?")
    for key in entries:
        print(key)

    entry = input('Enter entry name: ')

    if entry in entries:
        # Figure out which part of an entry the user wants to edit
        action = input("""
What would you like to do:
1. Change entry name
2. Change Username
3. Change Password
4. Change URL
Please enter a number (1-4): """)

        #edit entry title
        if action == '1':
            data = entries[entry]
            entries.pop(entry)
            new_title=input("What is the new title: ")
            entries[new_title] = data
        #edit username
        elif action == '2':
            entries[entry]['username'] = input("Enter a new username: ")
        #edit password
        elif action == '3':
            entries[entry]['password'] = password_encrypt(input("Enter a new password: "), encryption_key)
        #edit URL
        elif action == '4':
            entries[entry]['url'] = input("Enter a new URL: ")
        else:
            print("Something went wrong. Try again.")




def end_program():
    sys.exit()

def print_dictionary():
    print(entries)


menu_dict = {'1': load_password_file,
             '2': add_entry,
             '3': print_entry,
             '4': save_password_file,
             '5': end_program,
             '6': print_dictionary,
             '7': delete_entry,
             '8': edit_entry}

while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')