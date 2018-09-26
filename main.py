from src.chessboard import ChessBoard
from src.chesspiece import Color
from src.util import parser
from src.algorithms import simulated_annealing
from src.algorithms import hill_climbing
from src.algorithms import genetic_algorithm
import sys, termios, tty, os, time
from src.util import TerminalColor, get_terminal_width, clear
import datetime

magnus_image = """
:::,,:::~~:~~~~::,,~DODNNDNDN888O=+???I?+:::,=.,~+7I????IIII
:::~::::=~::,,::,?ON8DNDDNNNDDNNDDOO??I?+,,:,~..~+$?=+++?II7
~:::=~::,,,,,::,+D8DMNNNMNNDDDDDNDMNZ7I?+,,,,~..:+$+===++++?
++~:,,,,,,,,,,,,ZDNDNNNND8DMNMD88D8DN8I?+,,,,~..:=7+=====+++
:,,,,,,,,,,,,,,~ODDDNNNDNNNM8NMMNNN8N8Z?+,,,,:..:=7=~====+++
,,,....,,,,,,,:$ONNNNDND8DODDNDDMND88DZ?+,,,,:..:=7=~~====++
,,........,,:::7ON88NDDOOZZ8Z$ZZ$Z=~=I$+=,,,,:..:~I=~~===+??
,.......,::::::~8DDDND8$777II+++=~~~~~8::,,,,,..,,,,.,:=++++
,,...,::::::::::NNNNNNO$7II??++=~~~~~~O::,,,,,...,,.... ....
::::::::::::::::$DNNN8$777Z8DD87=~=8=++==,,,,....,,.,,,,,,,.
:::,,,,:::::::::$IDND$7I$$ONO=$$+=D:$=I?7,..,...,,+=~~::::::
,,,,,,,,,:::::::7$$OD77III????7I?~~~~~?I7,..,...,,?====+++??
,,,,,,,,,,:::::::7I7Z77I??+=+?7$I=~~~~~?$,..,...,,?=~~~~==++
:,,,,,,,,,:::::::ZZZ77$7I??+=?ZII?~=~:+?$,..,....,I=~~~~====
:::,,,,::::::::::II7I7777I?+==?I?+=~::I?$,..:....,I=~~~=====
::::::::::::::::::?77$$$7I?+I??II7+?~:I?$,..:....,I======+++
::::::::::::::::::~7I$$$$77I++77I+=~:?II$,..:....,I======+++
::::::::::::::::DN8~~7OZZ$77??????=~~:::,,,.......,~~~====++
,,,,,,,,,::::::+NNMMN:~+OOO$$III?+=~~:::,,,..............,:=
,,,,,,,,,,,:::~NNMMMNMM:::=OZZZ$I?+~::::,,,.......,.........
,,,,,,,,,,:::DNNNNMMMNNN~,,,,=~~~=I???777........,~,,,..,,,,
"""

magnus_name = """
 __  __                                _____           _                
|  \/  |                              / ____|         | |               
| \  / | __ _  __ _ _ __  _   _ ___  | |     __ _ _ __| |___  ___ _ __  
| |\/| |/ _` |/ _` | '_ \| | | / __| | |    / _` | '__| / __// _ \ '_ \ 
| |  | | (_| | (_| | | | | |_| \__ \ | |___| (_| | |  | \__ \  __/ | | |
|_|  |_|\__,_|\__, |_| |_|\__,_|___/  \_____\__,_|_|  |_|___/\___|_| |_|
               __/ |                                                    
              |___/                                                      
"""

logo = """
          _____                  _   _     _             
    /\   |_   _|                | | | |   (_)            
   /  \    | |______ _ __  _   _| |_| |__  _ _ __   __ _ 
  / /\ \   | |______| '_ \| | | | __| '_ \| | '_ \ / _` |
 / ____ \ _| |_     | | | | |_| | |_| | | | | | | | (_| |
/_/    \_\_____|    |_| |_|\__, |\__|_| |_|_|_| |_|\__, |
                            __/ |                   __/ |
                           |___/                   |___/ 
"""

 
message = ["Load file success", "No files found", "Print chess success"]

options = ["Input File", "Hill Climbing", "Simulated Annealing", "Genetic Algorithm", "Print Chessboard", "Exit"]
option = 0
os.system('setterm -cursor off')
os.system('clear')

c = ChessBoard()
init = False
print_chess = False
last_msg = None
last_log = ""

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_message():
    if last_msg != None:
        print(str(last_log) + ": " + message[last_msg])
def print_menu():
    print(logo)
    if print_chess:
        c.print()
    print("Menu :")
    for i in range(len(options)):
        if i == option:
            print(TerminalColor.DARKCYAN + '➜' + TerminalColor.END + " " + str(i+1) + ". " + options[i])
        else:
            print("  " + str(i+1) + ". " + options[i])
def welcome_message():
    print(magnus_image)
    print(magnus_name)
    input(TerminalColor.BOLD + TerminalColor.ITALIC + TerminalColor.DARKCYAN + "Press Enter to continue...  " + TerminalColor.END)
    os.system('clear')

welcome_message()
while True:
    try:
        print_menu()
        print_message()
        char = getch()
        if (ord(char) == 66):
            os.system('clear')
            if option + 1 < len(options):
                option +=1
        elif (ord(char) == 65):
            os.system('clear')
            if option - 1 >= 0:
                option -=1
        elif (char == "p"):
            os.system('setterm -cursor on')
            print("Stop!")
            exit(0)
        elif (ord(char) == 13):
            last_log = datetime.datetime.now()
            os.system('clear')
            print_menu()
            if option == 0:
                os.system('setterm -cursor on')
                try:
                    print("File name : ")
                    filename = input(TerminalColor.DARKCYAN + '➜' + TerminalColor.END + " ")
                    c.init_map(filename)
                    last_msg = 0
                    init = True
                except:
                    last_msg = 1
                os.system('setterm -cursor off')
                os.system('clear')
            elif option == 1:
                if init:
                    os.system('setterm -cursor on')
                    hill_climbing(c)
                    print_chess = False
                    os.system('setterm -cursor off')
                os.system('clear')
            elif option == 2:
                if init:
                    os.system('setterm -cursor on')
                    simulated_annealing(c)
                    print_chess = False
                    os.system('setterm -cursor off')
                os.system('clear')
            elif option == 3:
                if init:
                    os.system('setterm -cursor on')
                    genetic_algorithm(c)
                    print_chess = False
                    os.system('setterm -cursor off')
                os.system('clear')
            elif option == 4:
                os.system('clear')
                if init:
                    print_chess = True
                    last_msg = 2
            elif option == 5:
                print("Thank you!!")
                os.system('setterm -cursor on')
                exit()     
        else:
            os.system('clear')   
    except:
        os.system('setterm -cursor on')
        exit()
