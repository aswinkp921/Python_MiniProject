class User:
    def __init__(self, username, password, name, age, gender, email, phone):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone

    def show(self):
        print("--------------------------------------------------------------------------")
        print("                         PERSONAL DETAILS")
        print("--------------------------------------------------------------------------")
        print(f"User name: {self.username}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")
        print(f"Phone number: {self.phone}")


class Bank(User):
    def __init__(self, username, password, name, age, gender, email, phone):
        super().__init__(username, password, name, age, gender, email, phone)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited is: RS {amount}\nCurrent balance: RS {self.balance}\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn amount is: RS {amount}\nCurrent balance: RS {self.balance}\n")
        else:
            print("Insufficient Balance!!!\n")

    def view_balance(self):
        print(f"Account balance: RS {self.balance}")

    def personal_details(self):
        self.show()

    @staticmethod
    def login(users):
        print("**************************************************************************")
        print("                          LOGIN PAGE")
        print("**************************************************************************")
        username = input("Enter your user name: ")
        password = input("Enter your PIN: ")
        return username, password


def main():

    users = {
        "aswin": {"password": "1234", "name": "Aswin", "age": "28", "gender": "Male",
                  "email": "aswin123@gmail.com", "phone": "9886826262"},
        "virat": {"password": "5678", "name": "Virat", "age": "34", "gender": "Male",
                  "email": "virat123@gmail.com", "phone": "9886826262"},
        "smriti": {"password": "1111", "name": "Smriti", "age": "26", "gender": "Female",
                   "email": "smriti123@gmail.com", "phone": "9886826262"}
    }

    while True:
        print("---------------------------------------------------------------------------")
        print("                     WELCOME TO OUR BANKING SERVICE")
        print("---------------------------------------------------------------------------\n")
        print("                     MAIN MENU\n")
        print("\t\t1. Login\n\t\t2. Exit\n")

        try:
            choice = int(input("Enter your choice 1 or 2: "))
            if choice == 1:
                username, password = Bank.login(users)

                if username in users and password == users[username]["password"]:
                    user_details = users[username]
                    print(f"\nLogin successful! Welcome, {user_details['name']}")

                    user = Bank(username, password, user_details["name"], user_details["age"],
                                user_details["gender"], user_details["email"], user_details["phone"])

                    while True:
                        print("----------------------------------------------------------------------")
                        print("                         BANK MENU")
                        print("----------------------------------------------------------------------\n")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Personal Details")
                        print("5. Exit")

                        try:
                            ch = int(input("Enter your choice 1-5: "))
                            if ch == 1:
                                amount = float(input("Enter the amount to deposit: "))
                                user.deposit(amount)
                            elif ch == 2:
                                amount = float(input("Enter the amount to be withdrawn: "))
                                user.withdraw(amount)
                            elif ch == 3:
                                user.view_balance()
                            elif ch == 4:
                                user.personal_details()
                            elif ch == 5:
                                print("Thank you... Have a good day!!")
                                break
                            else:
                                print("Invalid choice. Please enter a number between 1 to 5")
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 to 5")

                else:
                    print("Login Failed... Please enter correct User name and PIN")

            elif choice == 2:
                print("Thank you... Have a good day!!\n")
                break
            else:
                print("Invalid choice. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Please enter 1 or 2")


if __name__ == "__main__":
    main()