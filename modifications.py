from clients import Client


class Modifications(Client):
    """This class is to create a temporary object that can retrieve account/client data from client_book dictionary
    so it can modify some information using methods from BankAccount, Client classes """

    def __init__(self, account_id, account_balance, account_password, account_type, nation_id, f_name, l_name, mobile):
        Client.__init__(self)  # Just to remove the warning
        self.account_id = account_id
        self.account_balance = account_balance
        self.account_password = account_password
        self.account_type = account_type
        self.national_id = nation_id
        self.first_name = f_name
        self.last_name = l_name
        self.mobile = mobile
