# מטרת הפרויקט:
# לבנות תוכנת כספומט שמבצעת פעולות: הפקדה, משיכה, בדיקת יתרה ויציאה, 
# עם אפשרות להחלפת קוד סודי והפקת קבלה.
# כל פונקציה מייצגת פעולה נפרדת.

import datetime

# שמירת לקוחות קיימים במערכת
customers = [
    {"name": "Avi Cohen", "pin": "1234", "balance": 1000},
    {"name": "Yossi Cohen", "pin": "6543", "balance": 500},
    {"name": "Yuri Levi", "pin": "5852", "balance": 800}
]
# פונקציה להתחברות משתמש:
# מבקשת מהמשתמש להזין שם מלא (שם פרטי ושם משפחה)
# בודקת אם המשתמש קיים במערכת
# אם כן - מבקשת קוד PIN ובודקת אם נכון
# מחזירה את פרטי המשתמש אם הצליח, אחרת None

def login(customers):
  name = input("Please enter your full name:")
  for customer in customers:
    if customer["name"].lower() == name.lower():
       print(f"Welcome {customer['name']}!")

       pin = input("Plase enter your PIN code:")
       if customer["pin"]== pin:
         print("Login successfull")
         return customer
       else:
         print("Incorrect PIN")
         return None
       
  print("User not found.")
  return None

# פונקציה להפקדה
def deposit(customer):
    try:
        amount = int(input("How much would you like to deposit? "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        if amount % 20 == 0 or amount % 50 == 0 or amount % 100 == 0:
            customer['balance'] += amount
            print(f"Deposit successful! Your new balance is {customer['balance']} NIS.")
        else:
            print("Invalid amount. You can only deposit multiples of 20, 50, or 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.You can only deposit multiples of 20, 50, or 100.")

# פונקציה למשיכה
def withdraw(customer):
    print("\nWithdraw Menu:")
    print("1 - 50 NIS")
    print("2 - 100 NIS")
    print("3 - 150 NIS")
    print("4 - 300 NIS")
    print("5 - Other amount")

    choice = input("Please choose an option (1-5): ")

    if choice == '1':
        amount = 50
    elif choice == '2':
        amount = 100
    elif choice == '3':
        amount = 150
    elif choice == '4':
        amount = 300
    elif choice == '5':
        try:
            amount = int(input("Enter the amount you wish to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    else:
        print("Invalid choice.")
        return

    if amount > customer['balance']:
        print("Sorry, operation could not happen. You don't have enough balance.")
    else:
        customer['balance'] -= amount
        print(f"Withdrawal successful! Your new balance is {customer['balance']} NIS.")

# פונקציה לבדיקה יתרה
def check_balance(customer):
    print(f"Your current balance is {customer['balance']} NIS.")

# שינוי סיסמא 
def change_pin(customer):
    new_pin = input("Enter your new 4-digit PIN code: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        customer['pin'] = new_pin
        print("PIN code changed successfully!")
    else:
        print("Invalid PIN. Please make sure it is exactly 4 digits.")

# פונקציה לקבלה
def print_receipt(customer):
    now = datetime.datetime.now()
    print("\n--- ATM RECEIPT ---")
    print(f"Hello {customer['name']},")
    print(f"Date and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Your current balance is: {customer['balance']} NIS")
    print("Thank you for using our ATM!")
    print("----------------------")


# יצירת התפריט 
def atm_menu(customer):
    while True:
        print("\nATM MENU:")
        print("Press 'd' to Deposit Money")
        print("Press 'w' to Withdraw Money")
        print("Press 'c' to Check your Balance")
        print("Press 'p' to Change your PIN code")
        print("Press 'r' to Print a Receipt")
        print("Press 'q' to Quit")

        choice = input("Please enter your choice: ").lower()

        if choice == 'd':
            deposit(customer)
        elif choice == 'w':
            withdraw(customer)
        elif choice == 'c':
            check_balance(customer)
        elif choice == 'p':
            change_pin(customer)
        elif choice == 'r':
            print_receipt(customer) 
        elif choice == 'q':
            print(f"GOODBYE {customer['name']}, HAVE A NICE DAY!")
            break
        else:
            print("Invalid choice. Please try again.")

#בדיקה שמריצה את הפונקציה
if __name__ == "__main__":
    logged_in_customer = login(customers)
    if logged_in_customer:
        atm_menu(logged_in_customer)
    else:
        print("Failed to login.")




   

