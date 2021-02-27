granted = False
def grant():
    global granted
    granted = True
def login(name,password): #step1
    #pass #to show what happens print("logged in"), make sure access(option) at the bottom
    #print("logged in")
    success = False
    file = open("user_details.txt", "r")  # r= read mode
    for i in file:  # step5
        #print(i)  # on the console we check if we can split using (",")= ['a','b']
        a, b = i.split(",")  # removes comma
        b = b.strip()  # removes new line character
        print(a, b)
        if (a == name and b == password):
            success = True
            break  # so that it wont keep on running
    file.close()
    if (success):
        print("Login successful")
        grant()
    else:
        print("Wrong username and password")

def register(name,password):
    #pass
    #print("registered")
    file = open("user_details.txt", "a") #'a'= add elements to file, dont put write mode
    file.write("\n"+name+","+password) #step4
    file.close()
    grant()
def access(option):
    global name #step3
    if(option == "login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)

def begin():
    global option #step2. if no global, there will be error on execute print(option)
    print("Welcome to Atikah's Programming input")
    option = input("Login or Register (login, reg): ")
    if(option != "login" and option != "reg"):
        begin()
begin()
access(option)
if (granted):
    print("Welcome to Atikah's Programming input")
    print("## User Details ###")
    print("Username: ", name)