
import random
import string
import os

ERRORS = 3

clear = False


#made by copiolet
def checkCSVexist(file):
    directoryFiles = os.listdir(".")
    if file in directoryFiles:
        return True
    else:
        return False






def login():
    global clear
    global ERRORS
    e = ERRORS
    np = False
    currentUser = ""
    while np == False or e >0:        
        user = input("what is your Name")
        password = input("what is your password")
        #found casefold from copiolet (used to check caps precisly)
        file = (f"{user}.csv")
        if checkCSVexist(file):
            with open(f"{user}.csv","r") as file:
                personalpassword = []
                for eachline in file:
                    words = eachline.rstrip().split(", ")
                    personalpassword.append(words[0])
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
        elif not checkCSVexist(file):
            e -= 1
            print("Incorrect password or username try again")
            print(f"{e} more chances to try again")
        if e == 0:
            print("attempts are gone. goodbye.")
            #from copiolet
            exit()
            
    
    return clear, currentUser



def signUp():
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
    global currentUser
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




def checkPassword(password):
    global currentUser
    with open(f"{currentUser}.csv","r") as file:
        personalpassword = []
        for eachline in file:
            words = eachline.rstrip().split(", ")
            personalpassword.append(words[0])
        if password == personalpassword[0]:
            return True
        else:
            print("error wrong password")
            return False




#copiolet
def onlySpaces(item):
    return item.isspace() or len(item) == 0


def newItem():
    global currentUser
    catOrItem = input("would you like to add 1.Catagory or 2.item")
    print(catOrItem)
    #while catOrItem != "1" or catOrItem != "2":
    #    catOrItem = input("error incorrect input please try again 1.catagory or 2.item")
    if catOrItem == "1":
        catname = input("what name will your catagory have? (required) ")
        itemName = input(f"what item would you like to add to category {catname}? (required) ")
        userName = input(f"what is the username for {itemName}? (required) ")
        id = input(f"what is the identity number of this item? (required) ")
        description = input(f"what description will you have for this item? ")
        if onlySpaces(catname) or onlySpaces(itemName) or onlySpaces(userName) or onlySpaces(id):
            print("error not all required paramiters are filld in properly")
            pass
        else:
            if onlySpaces(description):
                with open(f"{currentUser}.csv","a") as file:
                    lineToWrite = f"{catname},{itemName},{userName},{id}"
                    file.write(lineToWrite + "\n")
            else:
                with open(f"{currentUser}.csv","a") as file:
                    lineToWrite = f"{catname},{itemName},{userName},{id},{description}"
                    file.write(lineToWrite + "\n")
            
            
            
            
    elif catOrItem == "2":
        choice = input("are you adding 1.description or 2.no? ")
        if choice =="1":
            descrip = input("what will your description be? ")
            catname = input("what is the catagory? ")
            itemname = input("what is the item? ")
            username = input("what is the user name? ")
            idnumber = input("what is your id? ")
            with open(f"{currentUser}.csv","r")as file:
                lines = file.readlines()
            for i in range(1,len(lines)):
                try:
                    catagory,item,user,id = lines[i].strip().split(",")
                except:
                    catagory,item,user,id,des = lines[i].strip().split(",")
                if  idnumber == id and catname == catagory and itemname == item and username == user:
                    lineToWrite = (f"{catagory},{item},{user},{id},{descrip}" + "\n")
                    lines[i] = lineToWrite
                with open(f"{currentUser}.csv","w")as file:
                    for eachline in lines:
                        file.write(eachline)
        elif choice == "2":
            pass

 
    
            
            


def deleteItems():
    global currentUser
    catOrItem = input("would you like to delete 1.full item or 2.part of one")
    if catOrItem == "1":
        catname = input("what is the name of the category of the item you want to delete? ")
        #geekforgeek
        with open(f"{currentUser}.csv",'r') as read:
            lines = read.readlines()
            with open(f"{currentUser}.csv",'w') as file:
                for line in lines:
                    if not f'{catname}' in line.strip().split(","):
                        file.write(line)

    elif catOrItem == "2":
        itemName = input(f"what item would you like to delete? ")
        catname = input(f"what category would you like to delete {itemName} from? ")
        with open(f"{currentUser}.csv","r") as file:
            lines = file.readlines()
        for i in range(1,len(lines)):
            try:
                catagory,item,user,id,des = lines[i].strip().split(",")
            except:
                catagory,item,user,id = lines[i].strip().split(",")
            if catname in catagory:
                if itemName in catagory:
                    password = input("warning data will be deleted without this component password is required: ")
                    if checkPassword(password):
                        lines[i] = ""
                    else:
                        pass
                elif itemName in item:
                    password = input("warning data will be deleted without this component password is required: ")
                    if checkPassword(password):
                        lines[i] = ""
                    else:
                        pass
                elif itemName in user:
                    password = input("warning data will be deleted without this component password is required: ")
                    if checkPassword(password):
                        lines[i] = ""
                    else:
                        pass
                elif itemName in id:
                    password = input("warning data will be deleted without this component password is required: ")
                    if checkPassword(password):
                        lines[i] = ""
                    else:
                        pass
                elif itemName in des:
                    lineToWrite = (f"{catname},{item}{user},{id}" + "\n")
                    lines[i] = lineToWrite
            with open(f"{currentUser}.csv","w") as file:
                for eachline in lines:
                    file.write(eachline)








 


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
    print("2. Add Items")
    print("3. delete Items")
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










