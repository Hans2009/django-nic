import os
import sys
#sys.path.insert(0, '/hans/autotest/autotest/dev_jason/emulex/')
#import emulex_entry


def welcome_message():
    print(" ------------------------------------------------------------------------------")
    print(" Welcome to Use the Lenovo IO test utility tool. please do not distribute it.") 
    print("Any questions, please contact with meils1@lenovo.com.")
    print(" ------------------------------------------------------------------------------")
    print("Please choose the vendor.")
    print("     1: emulex")
    print("     2: qlogic")
    print("     3: intel")
    print("     4: mellanox")
    print("     5: broadcom")
    return "Hello, this is from main.py"


if __name__ == '__main__': 
    welcome_message()
    vendor = raw_input("please choose(1/2/3/4/5):")
    if vendor == "1":
        print("Emulex IO options")
    elif vendor == "2":

        print("QLogic IO options")
    elif vendor == "3":

        print("Intel IO options")
    elif vendor == "4":

        print("Mellanox IO options")
    elif vendor == "5":

        print("Broadcom IO options")
    else:
        print(" Error: does not support and wrong parameter")

    
    

