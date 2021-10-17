from random import randint
from datetime import datetime


class BankAccount:
    """ This Class creates a bank account based on Client class, this class supposed to initiate a bank account
    whenever a new client was created, this class has methods like
     account_display, deposit_setter, withdraw_setter, password_setter"""

    # Used in transaction details
    ar_weekday = ['الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت']
    months = ['يناير', 'فبراير', 'مارس', 'ابريل', 'مايو', 'يونيو', 'يوليو', 'اغسطس', 'سبتمبر', 'اكتوبر', 'نوفمبر',
              'ديسمبر']

    # THE NEXT 4 LINES SHOULD BE BETTER THAN THIS
    transaction_info = datetime.now()
    today_date = transaction_info.date().strftime('%d %m %Y').split(" ")  # Make a list of ['DD','MM','YYYY']
    month_name = months[int(today_date[1])]  # Get the name of the month based on the month number
    today_date[1] = month_name  # Change the second element from being month number to be the arabic name of the month
    today_date = ' '.join(today_date)  # convert the list to a string
    day_number = transaction_info.strftime('%w')  # Get the day number of the week
    day_name = ar_weekday[int(day_number)]  # Get the arabic day name based on the day number of the week
    transaction_time = transaction_info.time().strftime('%I:%M %p').split(' ')  # Get the time in am/pm format as a list
    if transaction_time[1].lower() == 'am':
        transaction_time[1] = 'صباحاً'
    else:
        transaction_time[1] = 'مساءاً'
    transaction_time = ' '.join(transaction_time)  # Convert the time to a string

    # I used default values for this init method because I have tow different scenarios.
    # 1: is calling this class for creating a new account, and that will use the default values to create the object
    #   then will go to account_setter to give the official values for that created account.

    # 2: is when calling this class for retrieving account data that already exists, and for that
    #   the init method will use the real data that has been passed to it.
    def __init__(self, account_id=0, account_balance=0, account_type=0, account_password=0):
        self.account_id = account_id
        self.account_balance = account_balance
        self.account_type = account_type
        self.account_password = account_password

    def account_setter(self, national_id):  # To pass the client national ID and use it for creating Bank Account
        self.account_id = national_id + randint(1000, 9999)  # Calculates the Account ID based on national ID
        self.account_balance = 0  # Set the balance equals 0 whenever a new account is created

        # the plan for account type to be used with special treatment when a client has more than 250,000, but not yet.
        self.account_type = 'normal'  # Set the account type to normal whenever a new account is created.
        self.account_password = '0000'  # Set the account password equals 0000 whenever a new account is created

    # This method is to show the account information.
    def account_display(self):
        print(f"Account ID is : {self.account_id} ")
        print(f"Account Balance is : {self.account_balance}")
        print(f"Account Password is : {self.account_password}")
        print(f"Account Type is : {self.account_type}")

    def deposit_setter(self, add):  # To add money to the account and print the transaction details
        # this line is to apply the change to the object it self, so it can accept another transaction without having
        # to logoff from the object and create it again
        self.account_balance = self.account_balance + int(add)
        print(f'تم ايداع {add} ريال لرصيدك البنكي في يوم '
              f'{BankAccount.day_name} بتاريخ  {BankAccount.today_date} الساعه {BankAccount.transaction_time}')
        return self.account_balance

    def withdraw_setter(self, deduct):  # To deduct money to the account and print the transaction details
        if self.account_balance >= int(deduct):  # To check whether or not the account is sufficient
            # this line is to apply the change to the object it self, so it can accept another transaction without
            # having to logoff from the object and create it again
            self.account_balance = self.account_balance - int(deduct)
            print(f'تم خصم {deduct} ريال من رصيدك البنكي في يوم .'
                  f'{BankAccount.day_name} بتاريخ  {BankAccount.today_date} الساعه {BankAccount.transaction_time}')
            return self.account_balance
        else:
            print('Your account balance is not sufficient for this withdraw!!!')
            return self.account_balance

    def password_setter(self, current_password):  # To change the account password
        old_password = input("enter current password :\n")  # To make sure that the user is the client
        confirmation = False  # For the next while loop
        if old_password == current_password:  # If the password is correct
            while not confirmation:  # Start a loop of giving the new password twice
                new_password = input("enter a new password :\n")
                confirm_password = input("enter the password again :\n")
                if new_password == confirm_password:
                    # this line is to apply the change to the object it self, so it can accept another transaction
                    # without having to logoff from the object and create it again
                    self.account_password = new_password
                    return self.account_password
                else:
                    print(f"Incorrect confirmation, try again")
        else:
            print(f"Incorrect password, You are redirected to the main screen ")
            return 'Wrong password'  # to leave the client account entirely
