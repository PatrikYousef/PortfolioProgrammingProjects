import random
import bcrypt
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    lastname: str
    username: str
    password: bytes 


@dataclass
class Customer:
    name: str
    lastname: str
    account_number: str
    ccv: str
    pin: str
    balance: float = 0.0


def PasswordSystem():
    letters = "abcdefghijklmnopqrstuvwxyz"
    newpassword = ""

    for i in range(10):
        newpassword += random.choice(letters)
    
    return newpassword

#def AddLogin(LoginInfo):
    name = input("Name: ")
    lastname = input("LastName: ")
    username = input("Username: ")
    password = PasswordSystem() 
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # Hasha lösenordet

    try:
        # Kontrollera om användarnamn redan finns
        for user in LoginInfo:
            if user.username == username:
                print("There is already a user with that username :)")
                return
        
        user = User(name, lastname, username, hashed_password)
        LoginInfo.append(user)
        print("Append login info successful :)")
        print("Generated password:", password)  # Visa användaren deras lösenord

    except ValueError:
        print("Invalid input. Please enter correct values.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


#def Login(LoginInfo):
    username = input("Username: ")
    password = input("Password: ")

    try:
        for user in LoginInfo:
            if user.username == username and user.password == password:
                print("Login successful :)")
                return
        
        print("cant find the username or password :(")

    except ValueError:
        print("Invalid input. Please enter correct values.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

#def ShowLogin(LoginInfo):
    if not LoginInfo:
        print("No customers found.")
        return

 
    print(f"{'Name':<15}{'Lastname':<15}{'Username':<25}{'Password':<10}")
    

    for workers in LoginInfo:
        print(f"{workers.name:<15}"
              f"{workers.lastname:<15}"
              f"{workers.username:<25}"
              f"{workers.password:<10}"
              
              )

#def LoginMenu(LoginInfo):
    while True:
        print("\nLogin System Menu")
        print("1. Create new login")
        print("2. Login")

        choice = input("Choose an option: ")

        if choice == "1":
            AddLogin(LoginInfo)
        elif choice == "2":
            Login(LoginInfo)
        elif choice == "3":
            ShowLogin(LoginInfo)

def AccountNumber():
    letters = "1234567890"
    NewAccountNumber = ""

    for i in range(16):
        NewAccountNumber += random.choice(letters)
    
    return NewAccountNumber

def CCV():
    letters = "1234567890"
    CCVNumber = ""

    for i in range(3):
        CCVNumber += random.choice(letters)
    
    return CCVNumber

def Pin():
    letters = "1234567890"
    PinCode = ""

    for i in range(4):
        PinCode += random.choice(letters)
    
    return PinCode

def AddCustomers(CostumerInformation):
    try:
        Name = input("Enter Name: ")
        LastName=input("Enter Lastname: ")
        NewAccountNumber=AccountNumber()
        NewCCV = CCV()
        NewPin= Pin()
        create_customer_info=Customer(Name, LastName, NewAccountNumber, NewCCV, NewPin)
        for info in CostumerInformation:
            if (info.account_number == NewAccountNumber):
                print("There is already the same info please try again :)")
                return
        CostumerInformation.append(create_customer_info)
        print("You have added")
        print(f"{'Name':<15}{'Lastname':<15}{'Account':<25}{'CCV':<10}{'PIN':<10}")
        print(f"{Name:<15}{LastName:<15}{NewAccountNumber:<25}{NewCCV:<10}{NewPin:<10}")

    except ValueError:
        print("Error with Value")

def RemoveCustomer(CostumerInformation):
    account_number = input("Enter the AccountNumber to remove: ").strip()

    for customer in CostumerInformation:
        if customer.accountnumbers == account_number:
            CostumerInformation.remove(customer)
            print("Account removed successfully.")
            return

    print("AccountNumber not found.")

def SearchForCustomer(CostumerInformation):
    account_numbers = input("Enter the AccountNumber: ").strip()

    for customer in CostumerInformation:
        if customer.account_number == account_numbers:
            print("\nCustomer Found:")
            print(f"Name: {customer.name}")
            print(f"LastName: {customer.lastname}")
            print(f"AccountNumber: {customer.account_number}")
            print(f"CCV: {customer.ccv}")
            print(f"PIN: {customer.pin}")
            print(f"Balance: {customer.balance}")
            return

    print("Customer not found.")

def AddMoney(CostumerInformation):
    AccountNumber = input("Enter AccountNumber: ").strip()
    for customer in CostumerInformation:
        if customer.account_number ==AccountNumber:
            AddMoney = float(input("How much Money do you wanna add: "))
            customer.balance +=AddMoney
            print(f"Name: {customer.name}")
            print(f"LastName: {customer.lastname}")
            print(f"AccountNumber: {customer.account_number}")
            print(f"CCV: {customer.ccv}")
            print(f"PIN: {customer.pin}")
            print(f"Balance: {customer.balance}")


def WithDrawMoney(CostumerInformation):
    AccountNumber= input("Enter AccountNumber: ")
    for customer in CostumerInformation:
        if customer.account_number ==AccountNumber:
            AddMoney = float(input("How much Money do you wanna withDraw: "))
            if customer.balance < AddMoney:
                print("You dont have enough money to withdraw the,{Addmoney}")
            else:
                customer.balance-=AddMoney
                print(f"Name: {customer.name}")
                print(f"LastName: {customer.lastname}")
                print(f"AccountNumber: {customer.account_number}")
                print(f"CCV: {customer.ccv}")
                print(f"PIN: {customer.pin}")
                print(f"Balance: {customer.balance}")



def ShowCustomers(CostumerInformation):
    if not CostumerInformation:
        print("No customers found.")
        return

 
    print(f"{'Name':<15}{'Lastname':<15}{'Account#':<25}{'CCV':<10}{'PIN':<10}{'Money':<10}")

    for customer in CostumerInformation:
        print(f"{customer.name:<15}"
              f"{customer.lastname:<15}"
              f"{customer.account_number:<25}"
              f"{customer.ccv:<10}"
              f"{customer.pin:<10}"
              f"{customer.balance:<10}") 
        

def main_menu():
    LoginInfo = []
    #LoginMenu(LoginInfo)
    CostumerInformation=[]
    while True:
        print("\n--- MAIN MENU ---\n")
        print("1. Add Customer\n")
        print("2. Remove Customer\n")
        print("3. Search for Customer by Account Number\n")
        print("4. Show All Customers\n")
        print("5. AddMoney To Account\n")
        print("6. WithDraw Money\n")
        print("0. Exit\n")

        choice = input("Enter choice: ")
        if choice == "1":
            AddCustomers(CostumerInformation)
    
        elif choice == "2":
            RemoveCustomer(CostumerInformation)
      
        elif choice == "3":
            SearchForCustomer(CostumerInformation)
        
        elif choice == "4":
            ShowCustomers(CostumerInformation)
       
        elif choice == "5":
            AddMoney(CostumerInformation)

        elif choice == "6":
            WithDrawMoney(CostumerInformation)

        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
main_menu()