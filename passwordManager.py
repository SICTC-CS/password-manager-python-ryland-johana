
import random
import string
import os

ERRORS = 3

clear = False




def login():
    global password
    global clear
    
    global ERRORS
    e = ERRORS
    np = False
    currentUser = ""
    while np == False or e >0:        
        user = input("what is your Name")
        password = input("what is your password")
        file = (f"{user}.csv")
        if os.path.isfile(file):
            with open(f"{user}.csv","r") as file:
                personalpassword = []
                for eachline in file:
                    words = eachline.rstrip().split(", ")
                    personalpassword.append(words[0])
            print(personalpassword)
            if password == personalpassword[0]:
                np = True
            if np == True:
                clear = True
                currentUser = user
                break
            elif np== False:
                e -=1
                print("Incorrect password or username try again")
                print(f"{e} more chances to try again")
            elif e == 0:
                print("attempts are gone. goodbye.")
                clear = False
                break
        elif not os.path.exists(file):
            e -= 1
            print("Incorrect password or username try again")
            print(f"{e} more chances to try again")
        if e == 0:
            print("attempts are gone. goodbye.")
            #from copiolet
            exit()
    currentUser = user
            
    
    return clear, currentUser



def signUp():
    global password
    global email
    global hint
    global clear
    Sgc = False
    while Sgc is False:
        user = input("what is your name")
        email = input("what is your email?")
        sendVerification()
        password = passwordverification()
        hint = input("what hint would you like to find your password?")
        file = (f"{user}.csv")
        if os.path.isfile(file):
            print("there is another user with this name try again")
        else:
            Sgc = True
    with open(f"{user}.csv","w+") as file:
        lineToWrite = f"{password}, {email}, {hint}"  #account name/title
        file.write(lineToWrite)
    clear = True
    currentUser = user
    
    

def showHint():
    global words
    while True:
        username = input("What is your user name.")
        email = input("what is your email? press 3 to go back")
        file = (f"{username}.csv")
        if os.path.isfile(file):
            with open(f"{username}.csv","r") as letter:
                for i in letter:
                    words = i.rstrip().split(", ")
                    print(words)
                if email == words[1]:
                    print(words[2])
                    break
                elif email == "3":
                    break
                    

def passwordCheck(password):
    #geeksforgeeks
    symbol = ['$','@','#','%']
    val = True
    if len(password) < 6 or len(password) > 20:
        val = False
    if not any(char.isdigit() for char in password):
        val = False
    if not any(char.islower() for char in password):
        val = False
    if not any(char.isupper() for char in password):
        val = False
    if not any(char in symbol for char in password):
        val = False
    if val:
        return val








def sendVerification():
    length = 5
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for i in range(length))
    verify = code
    inputVerification = input(f"please insert varification code to identify {code}   ")
    while inputVerification != verify:
        inputVerification = input(f"please insert varification code to identify {code}   ")
        



def passwordverification():
    option1 = input("do you want 1. Random password generator or 2. manual password")
        
    if option1 == "2":
        initialPassword = input("what do you want your password to be")
        passwordCheck(initialPassword)
        verifyPassword = input("please state your password for verification")
        while initialPassword != verifyPassword:
            print("invalid password try again")
            initialPassword = input("what do you want your password to be")
            verifyPassword = input("please state your password for verification")
        item = verifyPassword
    elif option1 == "1":
        satisfied = False
        while satisfied != True:
            length = int(input("how long do you want the password"))
            characters = string.ascii_letters
            password = ''.join(random.choice(characters)for i in range(length))
            print(password)
            justify = input("are you satisfied with the password if so press 1 if not press 2")
            if justify == "1":
                satisfied = True
        item = password
    else:
        option1 = input("invalid choice try again")
    return item





#category = input("what category would you like this account to be? home, work, entertainment, bills, etc")
#item = input("what is it that you are adding to this catagory")
#with open("storage.csv","a") as file:
#    lineToWrite = f"{category} {item}"  #account name/title
#    file.write(lineToWrite)

    
    


#f(x)
#csv- comma seperated values(data seperated by commas)
def display_list():
    print()
    global password
    global hint
    # read in the text file
    #with opentool(filename,mode) as alias
    with open(f"{currentUser}.csv","r") as file:
        userInfo = currentUser.split(", ")
        file = (f"{currentUser}.csv")
        if os.path.isfile(file):
            with open(f"{currentUser}.csv","r") as letter:
                for i in letter:
                    words = i.rstrip().split(", ")
                    print(words)
                if currentUser == words[1]:
                    print(words[2])
    #output to the terminal the data
            #print each line without \n on right en
        print(f'''Password: {password}
Username: {userInfo[0]}
Hint: {words[2]}''')
#print out how many coal and toys we need
#def count_items():
    # toys,coal = 0,0
    #read the text file
    # with open("TheList.csv","r")as file:
        #look at 2nd peice of data
        # for eachLine in file:
            # two var = eachline w/0 \n are split based on ", "
            # name,gift = eachLine.rstrip().split(", ")
            # data = eachLine.rstrip().split(", ")
            # if gift == "toy":
                # toys += 1
            # else:
                # coal +=1
            #puke results to terminal
    #     print(f"""
    # Toys: {toys}
    # Coal: {coal}
    #     """)



def newItem():
    global currentUser
    CatOrItem = input("would you like to add 1.Catagory or 2.item")
    if CatOrItem == "1":
        catname = input("what name will your catagory have? ")
        addItem = input("would you like to add a item to your list 1.yes  2.no")
        if addItem == "1":
            itemName = input(f"what item would you like to add to category {catname}? ")
            with open(f"{currentUser}.csv","a") as file:
                lineToWrite = f"{catname}: {itemName}"
    elif CatOrItem == "2":
        itemName = input(f"what item would you like to add?")
        catname = input(f"what category would you like to add {itemName} to? ")
        with open(f"{currentUser}.csv","a") as file:
            lineToWrite = f"{itemName}"



def deleteItems():
    global currentUser
    CatOrItem = input("would you like to delete 1.Catagory or 2.item")
    if CatOrItem == "1":
        catname = input("what is the name of the category? ")
        #geekforgeek
        with open(f"{currentUser}",'r') as read:
            lines = read.readlines()
            with open(f"{currentUser}",'w') as file:
                for line in lines:
                    if line.strip(" ") != f'{catname}':
                        file.write(line)

    elif CatOrItem == "2":
        itemName = input(f"what item would you like to delete?")
        catname = input(f"what category would you like to delete {itemName} from? ")
        with open(f"{currentUser}.csv","a") as file:
            lineToWrite = f"{itemName}"








 


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
    data=""
    while len(data)==0:
        option = input("1.Login, 2.Sign up 3.hint")
        if option == "1":
            data = login()
            currentUser=data[1]
        elif option == "2":
            signUp()
        elif option =="3":
            showHint()        
    print("1. Display Passwords")
    print("2. Add Account")
    print("3. Login")
    print("4. Change the name or account email")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        display_list()
    elif choice == "2":
        newItem()
    elif choice == "3":
        deleteItems()
    elif choice == "4":
        change_name()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")