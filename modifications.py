from clients import Client


class Modifications(Client, dict):
    """This class is to create a temporary object that can retrieve account/client data from client_book dictionary
    so it can modify some information using methods from BankAccount, Client classes """

    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)
        self.__dict__ = self
