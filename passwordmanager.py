
import random
import string



email = input("what is your email")
def sendVerification():
    length = 5
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for i in range(length))
    verify = code
    inputVerification = input(f"please insert varification code to identify {code}")
    while inputVerification != verify:
        inputVerification = input(f"please insert varification code to identify {code}")
        
sendVerification()  
user = input("what is your name")
username = input("what is your username?")
def passwordverification():
    option = input("do you want 1. Random password generator or 2. manual password")
    while option !=1 or option!= 2:
        option = input("invalid choice try again")
    if option == 2:
        initialPassword = input("what do you want your password to be")
        verifyPassword = input("please state your password for verification")
        while initialPassword == verifyPassword:
            print("invalid password try again")
            initialPassword = input("what do you want your password to be")
            verifyPassword = input("please state your password for verification")
        item = verifyPassword
    elif option ==1:
        length = int(input("how long do you want the password"))
        characters = string.ascii_letters
        password = ''.join(random.choice(characters)for i in range(length))
        item = password
    return item
password = passwordverification()
hint = input("what hint would you like incase you forget your password")
category = input("what category would you like this account to be? home, work, entertainment, bills, etc")

with open("storage.csv","a") as file:
    lineToWrite = f"{user}, {username}, {password}, {hint}, {category}"  #account name/title
    file.write(lineToWrite)

    
    
#def login():
    
    user = input("what is your username")
    password = input("what is your password")
    accountName = input("what is your accountName")
    
    return user, password, accountName

#f(x)
#csv- comma seperated values(data seperated by commas)
def display_list():
    print()
    # read in the text file
    #with opentool(filename,mode) as alias
    with open("storage.csv","r") as file:
    #output to the terminal the data
        for eachLine in file:
            #print each line without \n on right end
            print(eachLine.rstrip())
#print out how many coal and toys we need
#def count_items():
    toys,coal = 0,0
    #read the text file
    with open("TheList.csv","r")as file:
        #look at 2nd peice of data
        for eachLine in file:
            #two var = eachline w/0 \n are split based on ", "
            name,gift = eachLine.rstrip().split(", ")
            data = eachLine.rstrip().split(", ")
            if gift == "toy":
                toys += 1
            else:
                coal +=1
            #puke results to terminal
        print(f"""
    Toys: {toys}
    Coal: {coal}
        """)

def add_to_list():
    name = input("Name: ")
    gift = input("toy or coal: ").lower()
    #open the list by appending to it alias is file
    with open("TheList.csv", "a") as file:
        lineToWrite = f"{name}, {gift}\n"
        #file write this string
        file.write(lineToWrite)

def change_name():
    #old and new name
    old = input("Current name: ")
    new = input("New name: ")
    
    #read the data- save the file to the list
    with open("TheList.csv", "r") as file:
        lines = file.readlines() #converst file to list

    #find the old name
    for i in range(len(lines)):
        name,gift = lines[i].strip().split(", ")
        if name == old:
            name = new
            newData = f"{name}, {gift}\n"
            lines[i] = newData
    #reset the old to new name - overide the file
    with open("TheList.csv","w") as file:
        for eachline in lines:
            file.write(eachline)


#main loop
while True:
    print("\n--- Password Manager ---")
    print("1. Display Passwords")
    print("2. Add Account")
    print("3. Login")
    print("4. Change the name or account email")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        display_list()
    elif choice == "2":
        newAccount()
    elif choice == "3":
        count_items()
    elif choice == "4":
        change_name()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")










