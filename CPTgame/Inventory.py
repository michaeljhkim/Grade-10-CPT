
#for i in items:

items = open("stuff.txt", "r")

def Bag(items, cmd):
    #will show users contents of their stuff
    f = open("stuff.txt", "r")
    
    if items ==  "" and cmd == "view":
        print("Your bag is empty.")
        
    elif items != "" and cmd  == "view":
        print("You have:")
        print(f.read())

def add(toadd):
    # toadd will be the user input
    #this code will ad stuff to the bag
    f = open("stuff.txt", "a+") 
    f.write(toadd)

with open("yourfile.txt", "r") as f:
    lines = f.readlines()
with open("yourfile.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "nickname_to_delete":
            f.write(line)


