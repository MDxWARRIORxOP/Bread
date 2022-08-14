import time

def start():
    timeToSleep = 1
    print("Welcome to the BREAD")
    time.sleep(timeToSleep)
    print("as we all know, Bread is awesome and very cool")
    time.sleep(timeToSleep)
    print("So i decided to create a game about it!")
    time.sleep(timeToSleep)
    print("this game will let you bake bread in different forms!")
    time.sleep(timeToSleep)
    print("So lets bake some bread!")
    time.sleep(timeToSleep)

def bake():
    while(True):
        type = input("Which form do you want to bake your bread in? (q to quit)> ")
        
        if type == "q" or type == "quit":
            print("Dont forget Bread is awesome! Bye!")
            break
        
        if type.startswith("a") or type.startswith("e") or type.startswith("i") or type.startswith("o") or type.startswith("u"):
            aOrAn = "an"
        else:
            aOrAn = "a"
            
        print(f"You baked {aOrAn} {type}")
    quit()

if __name__=="__main__":
    start()
    bake()