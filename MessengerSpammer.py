from keyboard import press
import time as time
from tqdm import tqdm

class messageSender():
    word = None
    numberOfMessage = None
    speedLevel = None
    logo ='\x1b[33m' + '''
   __  ___                                                             
  /  |/  /__ ___ ___ ___ ____ ____   ___ ___  ___ ___ _  __ _  ___ ____
 / /|_/ / -_|_-<(_-</ _ `/ _ `/ -_) (_-</ _ \/ _ `/  ' \/  ' \/ -_) __/
/_/  /_/\__/___/___/\_,_/\_, /\__/ /___/ .__/\_,_/_/_/_/_/_/_/\__/_/   
                        /___/         /_/                                                  
    '''+'\x1b[39m'

    warningtext = '''
    \x1b[31m!!warning!!\x1b[39m
    this program might crash you device. 
    please be careful and check your textbox before start.
    this program only support Alphabet
    created by binbutsa21
    '''
    def __init__(self):
        self.__getInput()
    def __getInput(self):
        print(self.logo)
        print(self.warningtext)
        self.word = str(input("Enter the word that you want to say : "))
        self.numberOfMessage = input("How many messages that you want (only number) : ")
        print('''
                    Speed Select
            1.normal (1 messages per second)
            2.fast (10 messages per second)
            3.\x1b[31mBarry\x1b[33;1m Allen \x1b[39;1m(100 messages per second)
            Barry Allen might harm your device.
        ''')
        self.speedLevel = int(input("Input the speed level : "))
        self.__warnMessage()
    def __warnMessage(self):

        if(self.numberOfMessage!=None and self.word!=None and self.speedLevel!=None
         and self.numberOfMessage.isdigit()):
            print("You have 10 seconds to click at the message box of the chat")
            time.sleep(2)
            processBar = tqdm(total=100)
            for i in range(10):
                time.sleep(1)
                processBar.update(10)
            processBar.close()
            print("FIRE!!!")
            self.__activeBot()
        else:
            print("Error: there is something wrong. please enter again")
            time.sleep(3)
            self.__getInput()

    def __activeBot(self):
        speed = None

        if(self.speedLevel == 1):speed=1
        elif(self.speedLevel==2):speed=0.1
        elif(self.speedLevel==3):speed=0.01
        else:
            print("Speed input error!!!")
            self.__getInput()
        for i in range(int(self.numberOfMessage)):
            for char in self.word:
                press(char)
                time.sleep(0.001)
            press('Enter')
            time.sleep(speed)
        print(f"Finished. {self.numberOfMessage} messages send")

bot = messageSender()

