import Inventory
import Main

def store(shpp, lhpp, smpp, lmpp, cash):
    print("Small health Potions: restores 10 health.\n Price:", shpp, "gold")
    print("Large health Potions: restores 25 health.\n Price:", lhpp, "gold")
    print("Small mp Potion: restores 10 magic. \n Price:",smpp ,"gold")
    print("Large mp Potions: restores 20 health.\n Price",lmpp ,"gold")
    dec = input("")
    while dec != "exit":
        
        if (dec == "small health potion") or (dec == "large health potion") or (dec == "small mp potion") or (dec == "Large mp potion"):

            print("You are purchasing a", dec, "? (yes or no)")
            sure = input("")

            if sure == "yes":
                print("You purchased a", dec, "!")
                Inventory.add(dec)
                store(10, 10, 10, 10)
                
            if sure == "no":
                store(10, 10, 10, 10)
                
    


"""
def Ostham():
    slwprnt("Welcome to the Town of Ostham! We specialize in black smithing", 0.02)
    slwprnt("What will you be doing?:")
    print("We have an STORE, a BAR, and of course, the BLACKSMITH")
    dng = input("")
    if dng == "store":
        print("Welcome to my store! Ho may I help you?:")
        store(20, 50, 15, 30)
        
    

def Brightmere():


def Coldedge():
    slwprnt("Welcome to the Northern Town of Coldedge!", 0.02)


def Dorkeep():
    slwprnt("")


def Esterfall():


def Aelwynne():


def Fontaine():
"""
store(10, 10, 10, 10)
