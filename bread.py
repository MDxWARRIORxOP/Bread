import json
import sys
import os
import time
import requests
from pypresence import Presence

client_id = '1013449949364617307'
RPC = Presence(client_id)
RPC.connect()
currentTime = time.time()

RPC.update(state="The Awesome Bread Game", details="In love with the bread!!", buttons=[{"label": "Discord", "url": "https://discord.gg/tEk5eSXU7k"}, {"label": "Github Repo", "url": "https://github.com/MDxWARRIORxOP/Bread"}],large_image="nicebread", large_text="French Bread",small_image="smallbutnicebread", small_text="Cool Bread", start=currentTime)

baked = []

def start(b):
    # start game
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
    elif mode == "q" or mode == "quit":
        sys.exit()
    else:
        print("Invalid Mode!")
        start(True)
    

def eat(type):
    aOrAn = aOrAnFinder(type)

    if any(type == string for string in baked):
        print(f"You ate {aOrAn} {type}")
        baked.remove(type)
    else:
        print(f"You dont have {aOrAn} {type}! you have to bake {aOrAn} {type} to eat it!")

def bake(type):
    aOrAn = aOrAnFinder(type)
    if len(baked) == 4:
        str = ""
        for i in baked:
            if baked[-1] == i:
                str = str + i
            else: 
                str =  str + i + ", "
        print(f"You dont have enough space to bake!\nYou currently have {str}!")
    else:    
        baked.append(type)        
        print(f"You baked {aOrAn} {type}")


def aOrAnFinder(type):
    if type.startswith("a") or type.startswith("e") or type.startswith("i") or  type.startswith("o") or type.startswith("u"):
            aOrAn = "an"
    else:
            aOrAn = "a"
            
    return aOrAn

if __name__=="__main__":
    start(False)

while True:  
    time.sleep(15) 