from accounts import BankAccount


class Client(BankAccount):
    """This class is the responsible for creating new clients + associated account at once, it also has some other
     methods such as personal_display and mobile_setter"""

    #  The initiation method for a new client, and calling the BankAccount Class for creating the account
    def __init__(self, client_id="", national_id=0, first_name="", last_name="", mobile=0):
        BankAccount.__init__(self)  # Just to remove the warning
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.mobile = mobile
        super(Client, self).account_setter(self.national_id)  # To create the account based on the client national ID

    #  This method is to save the current created object to a dictionary before using the same object for a new creation
    def client_info_setter(self):
        return {
            'personal_info': {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'National_id': self.national_id,
                'mobile_no': self.mobile
            },
            'account_info': {
                'account_id': self.account_id,
                'account_balance': self.account_balance,
                'account_type': self.account_type,
                'account_password': self.account_password,
            }
        }

    # This method is to show the client information.
    def personal_display(self):
        print(f"Client Name is : {self.first_name} {self.last_name} ")
        print(f"Client national ID is : {self.national_id}")
        print(f"Client Mobile Number is : {self.mobile}")

    def mobile_setter(self, new_number):  # To change the client mobile number
        self.mobile = int(new_number)
        return self.mobile
