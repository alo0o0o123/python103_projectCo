from clients import Client
from modifications import Modifications
import re
import ast
import pprint


def new_entry(entry):
    new_client = ""  # A string that should contains the word "client" + a number that's not in used_sequence list
    pattern = re.compile(r"\d{10}, ?[a-zA-Z]+, ?[a-zA-Z]+, ?5\d{8}$")
    if re.match(pattern, entry):
        entry_parts = entry.split(',')
        cl_n_id = int(entry_parts[0])  # To get client's national ID
        cl_f_name = entry_parts[1].lower().capitalize()  # To get client's first name
        cl_l_name = entry_parts[2].lower().capitalize()  # To get client's last name
        cl_mobile = int(entry_parts[3])  # To get client's mobile number

        # Review the new client info
        print(f"Person's name is: '{cl_f_name} {cl_l_name}', ID {cl_n_id},"
              f" Phone number is: '{cl_mobile}'\n")
        submit = input(
            "Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

        if submit == "y":
            # This is a key for a sub-dictionary that represents the value of that key
            new_client += f"client{i}"
            client_info = Client(new_client, cl_n_id, cl_f_name, cl_l_name,
                                 cl_mobile)  # Create an object

            # THIS LINE NOT USEFUL WITH WORKING WITH FILES BECAUSE IT WILL START THE NUMBER ALL OVER AGAIN
            used_sequence.append(i)  # Add this number to used_sequence so it will not be used again

            # Add the new client info to a clients_book using a setter method
            clients_book[new_client] = client_info.client_info_setter()
            client_info.account_display()  # Call a method to display the new client account info
            client_info.personal_display()  # Call a method to display the new client personal info
            return False  # Terminate the while loop
    else:
        return True


def calling_modifications(client_book_item):
    return Modifications(account_id=client_book_item['account_info']['account_id'],
                         account_balance=client_book_item['account_info']['account_balance'],
                         account_password=client_book_item['account_info']['account_password'],
                         account_type=client_book_item['account_info']['account_type'],
                         national_id=client_book_item['personal_info']['National_id'],
                         first_name=client_book_item['personal_info']['first_name'],
                         last_name=client_book_item['personal_info']['last_name'],
                         mobile=client_book_item['personal_info']['mobile_no'])


running = True  # The boolean variable that used by the main while loop of this program
used_sequence = []  # A serial number list that contains a suffix number of newly created client. Ex client1, client2,..
item = {}  # Declare here so it will not give warning that says (variable can be unidentified)
# clients_book = {}  # It's the empty version of the database that contains all clients details.

# Next dictionary is an example with tow clients info that can be used instead of the empty clients_book dictionary
# clients_book = {'client00': {'account_info': {'account_balance': 0,
#                                               'account_id': 1022821753,
#                                               'account_password': '0000',
#                                               'account_type': 'normal'},
#                              'personal_info': {'National_id': 1022818684,
#                                                'first_name': 'Khalid',
#                                                'last_name': 'Waleed',
#                                                'mobile_no': 500053197}},
#                 'client0': {'account_info': {'account_balance': 0,
#                                              'account_id': 1066865284,
#                                              'account_password': '0000',
#                                              'account_type': 'normal'},
#                             'personal_info': {'National_id': 1066858745,
#                                               'first_name': 'Ali',
#                                               'last_name': 'Ahmed',
#                                               'mobile_no': 533222025}}}


while running:  # Program starts here.
    # To open the file that has dictionary inside, read it all, and save it in a dictionary variable
    # The code is doing good, BUT THAT IS NOT GOOD BECAUSE IT READS THE WHOLE FILE WHILE I NEED ONLY ONE PART OF
    # THAT FILE
    with open('clients_book.txt', 'r+') as c:
        cont = c.read()
        clients_book = ast.literal_eval(cont)

    choice1 = input("Enter the account number, or"
                    " '1' to create a new account,"
                    " '2' to check the clients book"
                    " '0' to stop the program :\n")
    # choices
    if choice1 == "1":  # 1st choice
        i = len(used_sequence)+1  # This variable to make sure that the selected number is not in used_sequence

        if i not in used_sequence:
            review = True  # For the second while loop
            while review:  # Start adding new client info
                new = input("Please follow this format for creating a new account 'National ID, first name, last name, "
                            "Mobile Number' Where:\nNational ID is 10 digits long\nMobile number is 9 digit long "
                            "starts with 5\nExample: '1200220022, Khalid, Ali, 500005000'\n")
                review = new_entry(new)

                # To open the file in write mode and update it with new client that has been created
                # This is working fine, BUT THE PROBLEM IS THAT THIS CODE WILL OVERRIDE THE WHOLE FILE WHERE I ONLY NEED
                # TO APPEND THE NEW CLIENT TO THE DICTIONARY INSIDE THE FILE
                clients_book = pprint.pformat(clients_book)
                with open('clients_book.txt', 'w') as c:
                    c.write(str(clients_book))

    elif choice1 == "0":  # 2nd choice
        running = False  # To stop the program

    elif choice1 == "2":  # 3rd choice
        for key, value in clients_book.items():
            print(key)
            item = value
            current_client = calling_modifications(item)
            current_client.account_display()
            current_client.personal_display()
            print('\n')

        # pprint(clients_book)  # To print the whole book of clients and their information

    else:  # Last choice To retrieve a client by its account number for making some transactions
        attempts = 0  # Declare here so it will not give warning that says (variable can be unidentified)

        for element in clients_book.items():
            if str(element[1]['account_info']['account_id']) == choice1:  # Here the choice can be an account number
                item = element[1]  # This is a sub-dictionary from the clients_book contains client/account info
                # print(item)
                attempts = 3  # Give the user 3 attempts to enter the password correctly
                break  # stop the for loop after finding the account number

        if attempts == 0:  # If the account number in not the the clients_book print the message
            print("Sorry that item is not available.")

        while attempts != 0:  # If the account has been found this line will work
            password = input('Enter your password:\n')
            if password == item['account_info']['account_password']:
                # Create an object contains the data for that selected account
                current_client = calling_modifications(item)
                attempts = 0  # To make sure that the upper while loop can not run without a correct account id
                inside = True  # This is for the next loop that designed for a client special menu
                while inside:  # Start client menu here
                    choice2 = input("\nEnter '1' for Deposit:\n"
                                    "Enter '2' for Withdraw:\n"
                                    "Enter '3' for update Mobile No:\n"
                                    "Enter '4' for updating password:\n"
                                    "Enter '5' for Account Info:\n"
                                    "or\n"
                                    "Enter 0 to logoff:\n"
                                    "NOTE:\n"
                                    "YOU MUST ENTER 0 TO SAVE ALL MODIFICATIONS YOU'VE MADE TO THE CLIENT ACCOUNT\n")
                    print('\n')
                    if choice2 == '1':
                        deposit = True
                        while deposit:
                            choice2 = input("enter amount for deposit:\n")
                            transaction_pattern = re.compile(r"\d+")
                            if re.match(transaction_pattern, choice2):
                                # To add money then update the clients book dictionary
                                item['account_info']['account_balance'] = current_client.deposit_setter(choice2)
                                deposit = False
                            else:
                                print("Wrong Entry, please enter an integer number only!")
                                deposit = True

                    elif choice2 == '2':
                        withdraw = True
                        while withdraw:
                            choice2 = input("enter amount to withdraw:\n")
                            transaction_pattern = re.compile(r"\d+")
                            if re.match(transaction_pattern, choice2):
                                # To deduct money then update the clients book dictionary
                                item['account_info']['account_balance'] = current_client.withdraw_setter(choice2)
                                withdraw = False
                            else:
                                print("Wrong Entry, please enter an integer number only!")
                                withdraw = True

                    elif choice2 == '3':
                        mobile_update = True
                        while mobile_update:
                            choice2 = input("enter new mobile no :\n")
                            transaction_pattern = re.compile(r"5\d{8}$")
                            if re.match(transaction_pattern, choice2):
                                # To modify the client mobile number
                                item['personal_info']['mobile_no'] = current_client.mobile_setter(choice2)
                                mobile_update = False
                            else:
                                print("Wrong Entry, please enter an integer number only!")
                                mobile_update = True

                    elif choice2 == '4':
                        password_value = item['account_info']['account_password']
                        the_new_password = current_client.password_setter(password_value)
                        if the_new_password == 'Wrong password':
                            inside = False  # to leave the client account entirely
                        else:
                            item['account_info']['account_password'] = the_new_password  # update the client book

                    elif choice2 == '5':  # To print the client info
                        current_client.account_display()
                        current_client.personal_display()

                    elif choice2 == '0':  # To leave and close the account
                        # To open the file in write mode and update it with with all transaction that happened to
                        # the selected client
                        # This is working fine, BUT THE PROBLEM IS THAT THIS CODE WILL OVERRIDE THE WHOLE FILE WHERE I
                        # ONLY NEED TO UPDATE THE SELECTED CLIENT ACCOUNT
                        clients_book = pprint.pformat(clients_book)
                        with open('clients_book.txt', 'w') as c:
                            c.write(str(clients_book))
                        inside = False

                    else:  # For unexpected entry from the user
                        print("Invalid Entry, Try again")

            else:  # If the client entered a wrong password
                attempts -= 1  # The attempts will be reduced by one
                print(f"Incorrect password, you still have {attempts} attempts ")
