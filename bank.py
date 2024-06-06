from rich.table import Table

class Account:
    def __init__(self, pin, name, surname, balance):
        self.pin = pin
        self.name = name
        self.surname = surname
        self.balance = balance

    def interface_print(self):
        table = Table(show_header=False, border_style="black", title=f'Balance: {self.balance}', title_justify="center", title_style="green")

        table.add_column(style="blue")
        table.add_column(style="blue")

        table.add_row("[1]", "Transfer")
        table.add_row("[2]", "Loan")
        table.add_row("[3]", "Hotline")
        table.add_row("[4]", "Details")    
        table.add_row("[Q]", "Exit", style="red")
        return table
    
    def loan_print(self, ammount):
        table = Table(show_header=False, border_style="black", title="New loan", title_justify="center", title_style="green")

        table.add_column(style="blue")
        table.add_column(style="blue")

        table.add_row("Initial balane: ", str(self.balance))
        table.add_row("Loan ammount: ", str(ammount))
        table.add_row("Initial balance + Loan: ", str(self.balance + ammount))
        return table
    
    def transfer_print(self, ammount, pin):
        table = Table(show_header=False, border_style="black", title="Transfer menu", title_justify="center", title_style="green")

        table.add_column(style="red")
        table.add_column(style="red")
        table.add_column(style="blue")
        table.add_column(style="blue")

        table.add_row("Initial balane: ", str(self.balance), "Recivers pin", pin)
        table.add_row("Transfer ammount: ", str(ammount))
        table.add_row("Initial balance - transfer: ", str(self.balance - ammount))
        return table
    
    def details_print(self):
        table = Table(show_header=False, border_style="black", title="Details", title_justify="center", title_style="green")

        table.add_column(style="green")
        table.add_column(style="green")

        table.add_row("PIN: ", str(self.pin))
        table.add_row("Name: ", self.name)
        table.add_row("Surname: ", self.surname)
        return table
    
def register_print(name, surname, pin):
    table = Table(show_header=False, border_style="black", title="You're new account", title_justify="center", title_style="green")

    table.add_column(style="blue")
    table.add_column(style="green")

    table.add_row("Name: ", name)
    table.add_row("Surname: ", surname)
    table.add_row("Pin: ", pin)
    return table

def login_print():
    table = Table(show_header=False, border_style="black", title="Login Menu", title_justify="center", title_style="green")

    table.add_column(style="blue")
    table.add_column(justify="center", style="green")

    table.add_row("[1]", "Login")
    table.add_row("[2]", "Sing in")
    table.add_row("[3]", "Hotline")
    table.add_row("[Q]", "Exit", style="red")
    return table
