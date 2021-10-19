from clients import Client


class Modifications(Client, dict):
    """This class is to create a temporary object that can retrieve account/client data from client_book dictionary
    so it can modify some information using methods from BankAccount, Client classes """

    # This function get one item from client_book dictionary
    def __init__(self, **kwargs):  # This is your standard __init__ method.
        dict.__init__(self, **kwargs)  # The call to dict.__init__(...) is to utilize the super class constructor method
        # The final line, self.__dict__ = self makes it so the keyword-arguments (kwargs) you pass to the __init__
        # method can be accessed like attributes,
        # for example: current_client.account_id, current_client.account_balance in the code in main.py
        self.__dict__ = self

    # If confused,, check function calling_modifications in main.py
