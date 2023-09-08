import random

user_dict = {}       # dictionary to store user details
deposit_dict = {}    # dictionary to store deposit amounts
password_dict = {}   # dictionary to store passwords


# Dictionary containing sample responses for banking queries
sample_responses = {
    "balance": "Sure Sir, but ",
    "transfer": "Sir, we dont have money transfer services on chatbot",
    "help": "How can I assist you today?",
    "fallback": "I'm sorry, I didn't understand that. Could you please rephrase?",
    "create account":"Sure, Sir As You Wish",
    "create bank account":"Roger Sir, Here We Go",
    "hello":"hi",
    "hi":"hello, how can i help you?",
    "banking portal":"Ready At Your Service",
    "main menu": "Ready At Your Service",
    "how are you":"i am fine, how are you boss?",
    "fine":"That's Good, How can i help you ?",
    "gender":"I am Ai-based model and varun creted me on very beautiful day "
}


# function to add more details about the user
def add_details_users():
    accNo = int(input("Enter Account No : "))
    mobile_no = int(input("Enter Mobile No : "))
    email_ID = input("Enter EMAIL : ")
    father_name = str(input("Enter Father Name : "))
    password_dict.update({accNo: {mobile_no, email_ID, father_name}})
    home_page()

# creating account
def create_account():
    password__()

# creating password whilew creating account
def password__():
    print("\nInstruction : \nBank Account Number Must be Equal to 10 Digits")
    print("Password Should be Equal Or Greater Than 6 Digits*")
    account_no = int(input("\nPayBot : Enter Account No\nUser : "))
    name = str(input("\nPayBot : Enter Name\nUser : "))
    print("\nPayBot : Create Password (digits only)\nUser : ")
    password = int(input("\nEnter Password : "))
    print("\nPayBot : Enter Confirm Password : ")
    c_password = int(input("User : "))
    if password == c_password:
        if len(str(password)) >= 6:
            a = str(password)
            b = str(account_no)
            user_dict.update({b: a})
            print("\nPayBot : Please Make A Login To Add Minimum Deposit To Bank Account,\n")
            print("Thank You!, For Creating Bank Account")
            login_0()
        else:
            print(
                "\nPayBot : Dear Sir, Please Make A Password Of More Than 6 Characters.\nBot : Please Re-Input Credentials.\n\n")
            password__()
    else:
        print("\nPayBot : Password Un-Matched!, Re-Enter Credits\n")
        password__()

# login to ur account
def login():
    ser = int(input("\nEnter Account No : "))
    try:
        if len(str(ser)) >= 10 or len(str(ser)) <= 12:
            print("\nPayBot : Enter Password : ")
            pas = input("\nUser : ")
            c = str(ser)
            d = str(pas)
            if dict[c] == d:
                print("\nPayBot : Credits Matched!, Welcome, To Your Banking Portal Space")
                home_page(ser)
            else:
                print("\nPayBot : Login Credentials Un-Matched, Try-Again")
                homepage(ser)
    except:
        print(
            "\nPayBot : Dear Sir, You have entered invalid account number Or There is no account exists for entered credentials.")
        homepage()

#login for initial deposit
def login_0():
    print("\nPayBot : Enter Account No")
    ser = int(input("User : "))
    print("\nPayBot : Enter Password : ")
    password = input("\nUser : ")
    c = str(ser)
    d = str(password)
    if dict[c] == d:
        print("\nPayBot : Credits Matched!, Welcome, Sir",)
        first_deposit(ser)
    else:
        print("\nPayBot : Login Credentials Un-Matched, Try-Again")
        homepage(ser)

#
def first_deposit(_a):
    print("\nInstruction : Input Deposit Amount { Minimum Rs 500 }")
    print("\nPayBot : Enter Amount To Deposit: ")
    move_depo = int(input("\nUser : "))
    try:
        if move_depo < 500:
            print("\nPayBot : First Deposit Should Be More Than Rs.500")
            first_deposit(_a)
        else:
            print("\n")
            e = str(_a)
            f = str(move_depo)
            deposit_dict.update({e: f})
            homepage()
    except:
        print("\nPayBot : Dear Holder, Enter Valid Amount In (Int), Try Again")
        first_deposit(_a)

#function to deposit money
def deposit_money(ser):
    print("\nPayBot : Input Amount To Deposit Rs.")
    depo = int(input("\nUser : "))
    i = str(ser)
    j = int(bool(deposit_dict.get(i)))
    if j == 1:
        k = int(deposit_dict.get(i))
        depo = depo+k
        deposit_dict.update({i: depo})
        home_page(ser)
    else:
        print("\nPayBot : You Do Not Have A Account In This Bank Please Create Account To Make Deposit. or Try Again")
        print("1. Re-Try\n2. Frontpage")
        choice = int(input("\nUser : "))
        if choice == 1:
            deposit_money(ser)
        elif choice == 2:
            home_page(ser)


def withdraw_money(ser):
    print("\nPayBot : Enter amount to withdraw Rs.")
    with_draw = int(input("\nUser : "))
    g = str(ser)
    h = int(deposit_dict.get(g))
    k = int(bool(deposit_dict.get(g)))
    print(h)
    if k == 1:
        if h >= with_draw:
            w_d = (h - with_draw)
            print("\nPayBot : You Bank Balance Left With Is Rs.", w_d)
            deposit_dict.update({g: w_d})
            home_page(ser)
        elif h < with_draw:
            print("\nPayBot : Inputed Amount Is Greater Than Bank Amount Balance.")
            print("User You Have Only Rs", h,"In Your Bank Account, Kindly Re-Enter The Amount.")
            withdraw_money(ser)
        elif h == 0:
            print("\nBot : You Have Null Amount In Bank Account.")
            home_page(ser)
    else:
        print("\nPayBot : You Do Not Have A Account In This Bank Please Create Account To Make Withdraw. or Try Again")
        print("1. Re-Try\n2. Frontpage")
        try:
            choice_1 = int(input("\nUser : "))
            if choice_1 == 1:
                withdraw_money(ser)
            elif choice_1 == 2:
                home_page(ser)
            elif choice_1 < 1 or choice_1 > 2:
                print(
                    "\nPayBot : Mr Account Holder, You Have Selected Incorrect Option, Please Try-Again")
        except:
            print("\nPayBot : Mr Account Holder, Select Options in (Int)* Only")
            home_page()

# function for
def homepage():
    print(
        "\nPayBot : \n1. Create Account\n2. Login\n0. Exit")
    try:
        ch = int(input("\nUser : "))
        if ch == 1:
            create_account()
        elif ch == 2:
            try:
                login()
            except:
                print("\nPayBot : Dear Sir, There Is No Account For Inputted Credentials, In Order To Continue Please Create Account.\n\t\t\tThank You\n\n")
                homepage()
        elif ch == 0:
            quit()
        elif ch > 2 or ch < 0:
            print(
                "\nPayBot : Mr Account Holder, You Have Selected Incorrect Option, Please Try-Again\n")
            homepage()
    except:
        print("\nPayBot : Mr Account Holder, Select Options in (Int)* Only\n\n")
        homepage()


# function to update/change password
def password_update(ser):
    print("\nEnter New Password : ")
    password = int(input("\nUser : "))
    print("\nEnter Confirm New Password : ")
    newPassword = int(input("\nUser : "))
    y = str(password)
    x = str(ser)
    if password == newPassword:
        print("\nPayBot : Credentials matched!, Password Changed-Successfully!")
        user_dict.update({x: y})
        home_page(ser)
    else:
        print("\nPayBot : Credentials Not Matched")
        password_update(ser)

# function to check balance info
def check_balance(ser):
    z = str(ser)
    x = password_dict.get(z)
    y = int(bool(deposit_dict.get(z)))
    s = deposit_dict.get(z)
    if y == 1:
        print("\nPayBot : Your Account Balance : Rs", s, "\n")
        home_page(ser)
    else:
        print("\nPayBot : Dear, Sir/Madam You Do Not Have A Account In This Bank.\n")
        homepage()


# function for the home page
def home_page(ser):
    print("\nPayBot : \n1. Withdraw Money\n2. Deposit Money\n3. Add User \n4. Check Balance Info\n5. Change PasswordDetails \n6. Log Out\n\n")
    try:
        ch = int(input("\nSelect Service : "))
        if ch == 1:
            withdraw_money(ser)
        elif ch == 2:
            deposit_money(ser)
        elif ch == 3:
            add_details_users()
        elif ch == 4:
            check_balance(ser)
        elif ch == 5:
            password_update(ser)
        elif ch == 6:
            home_page()

    except:
        print("\n\t\t\tPayBot : Enter List Options in Integer Only")
        home_page(ser)


# this function is for chats with the banking bot
def chat_with_bot(message):
    message = message.lower()

    if "balance" in message:
        return sample_responses["balance"]
    elif "transfer" in message:
        return sample_responses["transfer"]
    elif "transaction" in message:
        return sample_responses["transactions"]
    elif "help" in message:
        return sample_responses["help"]
    elif "create account" in message:
        # return sample_responses["create account"]
        homepage()
    elif "banking portal" in message:
        return sample_responses["banking portal"]
        homepage()
    elif "home page" in message:
        return sample_responses["banking portal"]
        homepage()
    elif "hi" in message:
        return sample_responses["hi"]
    elif "hello" in message:
        return sample_responses["hello"]
    elif "hi" in message:
        return sample_responses["hi"]
    elif "how are you" in message:
        return sample_responses["how are you"]
    elif "hi" in message:
        return sample_responses["hi"]
    elif "main menu" in message:
        homepage()
    elif "gender" in message:
        return sample_responses["gender"]
    elif "bye" in message:
        return "Bye! Thanks for visiting"
    else:
        return sample_responses["fallback"]


# here chatbot introduces itself
print("Hi, I'm PayBot, Your Banking ChatBot")
print("How can I assist you today?")

while True:
    # user give his/her query
    user_input = input("You: ")
    bot_response = chat_with_bot(user_input)
    print("PayBot:", bot_response)
    if bot_response == 'Bye! Thanks for visiting':
      break