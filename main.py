from rich.console import Console
from rich.table import Table
from rich.live import Live
from bank import *
import os, time, pwinput, sqlite3, hashlib

clear = lambda: os.system('cls')

db = sqlite3.connect("accounts.db")
cur = db.cursor()

con = Console()

def login_menu():
    while True:
        clear()
        con.print(login_print())
        n = input("Input: ")
        if n == '1':
            login()

        elif n =='2':
            register()

        elif n =='3':
            clear()
            con.print("\n Transfering... \n plese hold...")
            time.sleep(2)  

        elif n.lower() =='q':
            clear()
            exit()

        else:
            clear()
            con.print("Unnknown command.")
            time.sleep(2)

def login():
    clear()

    con.print("PIN", style="green")
    pin = input(": ")

    con.print("Password", style="green")
    password = pwinput.pwinput(mask='*', prompt=": ")
    password = hashlib.sha384(password.encode("utf-8")).hexdigest()

    clear()

    cur.execute("SELECT * FROM accounts WHERE pin = ?", (pin,))
    reg = cur.fetchone()

    if not reg:
        input("Failed! \nPress Enter to continue: ")
    elif reg[1] == password:
        global acc
        acc = Account(reg[0], reg[2], reg[3], reg[4])
        interface()
    else:
        input("Failed! \nPress Enter to continue: ")

def register():
    clear()

    con.print("Name", style="green")
    name = input(": ")

    con.print("Surname", style="green")
    surname = input(": ")

    x = True
    while x:
        clear()

        con.print("Password", style="green")
        password = pwinput.pwinput(mask='*', prompt=": ")

        con.print("Confirm password", style="green")
        passwordC = pwinput.pwinput(mask='*', prompt=": ")

        if password == passwordC:

            x = False

            password = hashlib.sha384(password.encode("utf-8")).hexdigest()

            cur.execute("SELECT seq FROM sqlite_sequence")
            pin = cur.fetchone()
            pin = str(int(pin[0]) + 1)

            clear()

            con.print(register_print(name, surname, pin))
            input("To continue press Enter: ")
        else:
            con.print("Plese try again")
            time.sleep(3)

    cur.execute("""INSERT INTO accounts (Pass, Name, Surname, Balance)
                   VALUES ((?), (?), (?), (?))""",
                   (password, name, surname, 0))
    
    db.commit()

def interface():
    clear()

    while True:
        clear()
        with Live(acc.interface_print(), console=con, refresh_per_second=1) as live:
            live.update(acc.interface_print(), refresh=True)
        n = input("Input: ")
        if n=='1':
            transfer()

        elif n=='2':
            loan()

        elif n=='3':
            clear()
            con.print("\n Transfering... \n plese hold...")
            time.sleep(2)

        elif n=='4':
            details()
            
        elif n.lower()=='q':
            clear()
            exit()

        else:
            clear()
            con.print("Unnknown command.")
            time.sleep(2)

def transfer():
    clear()
    con.print("Ammount", style="green")
    ammount = int(input(": "))

    con.print("Recivers pin", style="green")
    pinRx = input(": ")

    clear()

    con.print(acc.transfer_print(ammount, pinRx))

    while True:
        pin = input(f"Confirm with PIN ({acc.pin}): ")
        if int(pin) == acc.pin:
            acc.balance -= ammount
            cur.execute("SELECT * FROM accounts WHERE pin = ?", (int(pinRx), ))
            rx = cur.fetchone()
            balanceRx = int(rx[4])
            balanceRx += ammount
            cur.execute("""UPDATE accounts
                            SET Balance = (?)
                            WHERE PIN = (?)""", 
                            (acc.balance, acc.pin))
            cur.execute("""UPDATE accounts
                            SET Balance = (?)
                            WHERE PIN = (?)""", 
                            (balanceRx, int(pinRx)))
            db.commit()
            
            break
        else:
            con.print("Wrong PIN. Try again\n")

def loan():
    clear()

    con.print("Ammount", style="green")
    ammount = int(input(": "))

    clear()

    con.print(acc.loan_print(ammount))

    while True:
        pin = input(f"Confirm with PIN ({acc.pin}): ")
        if int(pin) == acc.pin:
            acc.balance += ammount
            cur.execute("""UPDATE accounts
                            SET Balance = (?)
                            WHERE PIN = (?)""", 
                            (acc.balance, acc.pin))
            db.commit()
            
            break
        else:
            con.print("Wrong PIN. Try again\n")

def details():
    clear()

    con.print(acc.details_print())
    input("Go back with Enter: ")

login_menu()