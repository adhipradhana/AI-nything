import os

def parser(filename):
    result=[]
    file = open(filename, "r")
    for line in file:
        result.append(line.splitlines()[0].split(" "))
    return result

def get_terminal_width():
    columns = int(os.popen('stty size', 'r').read().split()[1])
    return columns

def clear():
    _ = os.system('cls' if os.name == ' nt' else 'clear')

class TerminalColor:
   END = '\033[0m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   UNDERLINE = '\033[4m'
   BLINKING = '\033[5m'
   DARKCYAN = '\033[36m'
   RED = '\033[91m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   BLUE = '\033[94m'
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   BACK_RED = '\033[41m'
   BACK_GREEN = '\033[42m'
   BACK_YELLOW = '\033[43m'
   BACK_BLUE = '\033[44m'
   BACK_PURPLE = '\033[45m'
   BACK_CYAN = '\033[46m'
   BACK_GREY = '\033[47m'