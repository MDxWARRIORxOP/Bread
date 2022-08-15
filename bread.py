import sys
import time

def start(b):
    if not(b):      
        timeToSleep = 1
        print("Welcome to the BREAD")
        time.sleep(timeToSleep)
        print("as we all know, Bread is awesome, very cool and tasty")
        time.sleep(timeToSleep)
        print("So i decided to create a game about it!")
        time.sleep(timeToSleep)
        mode = input("So what do you want to do today? (eat/bake)> ")
        startGame(mode)
    else:
        mode = input("So what do you want to do today? (eat/bake)> ")
        startGame(mode)
        

def startGame(mode):
    if mode == "eat":
        # you wanna eat bread
        while(True):
            type = input("Which Bread Would You Like To Eat?\n(q to quit, p to go to previous section)>\n").lower()
            if type == "q" or type == "quit":
                sys.exit()
            if type == "p" or type == "previous":
                start(True)
                
            eat(type)
            
    elif mode == "bake":
        # you wanna bake some bread
        while(True):
            type = input("Which Bread Would You Like To Bake?\n(q to quit, p to go to previous section)>\n").lower()
            
            if type == "q" or type == "quit":
                sys.exit()
            if type == "p" or type == "previous":
                start(True)
                
            bake(type)
    else:
        print("Invalid Mode!")
        return sys.exit()
    

def eat(type):
    aOrAn = aOrAnFinder(type)
            
    print(f"You ate {aOrAn} {type}")
    return None

def bake(type):
    aOrAn = aOrAnFinder(type)
            
    print(f"You baked {aOrAn} {type}")

def aOrAnFinder(type):
    if type.startswith("a") or type.startswith("e") or type.startswith("i") or  type.startswith("o") or type.startswith("u"):
            aOrAn = "an"
    else:
            aOrAn = "a"
            
    return aOrAn

if __name__=="__main__":
    start(False)