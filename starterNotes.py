#import

#global var

'''
    mode is what are you doing with the file?
    r - reading
    w- writeing
    a - appending
    w+ - create and write
'''

#f(x)
#csv- comma seperated values(data seperated by commas)
def display_list():
    print()
    # read in the text file
    #with opentool(filename,mode) as alias
    with open("TheList.csv","r") as file:
    #output to the terminal the data
        for eachLine in file:
            #print each line without \n on right end
            print(eachLine.rstrip())
#print out how many coal and toys we need
def count_items():
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
    print("\n--- Santa's Nice and Naughty List ---")
    print("1. Display the list")
    print("2. Add a person to the list")
    print("3. Count toys and coal")
    print("4. Change the name")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        display_list()
    elif choice == "2":
        add_to_list()
    elif choice == "3":
        count_items()
    elif choice == "4":
        change_name()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
