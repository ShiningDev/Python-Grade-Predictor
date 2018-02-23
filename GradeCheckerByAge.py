#!/usr/bin/env python
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
#Welcome Message

welcome = """
 _    _      _                          
| |  | |    | |                         
| |  | | ___| | ___ ___  _ __ ___   ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ /
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___/      
  
"""
r1 = "[*] Please use only numbers \n"

printout(welcome, RED)
printout(r1, GREEN)

# Get Age

age = eval(input("What's your age? "))

# If age is 5, you'll go to kindergarten

if (age < 5):
    print("You're still too young n00b")

# Ages 6 though 17 goes to grades 1 through 12
if (age >= 6) and (age <= 17):
    grade = age -6
    if(grade == 0):
        print("You should be in kindergarden")
    else:
        print("You should be on {} grade".format(grade))
# If your age is greater than 17, then go to college
if (age > 17):
    print("Go to college, even if you're {}, it's never too late".format(age))