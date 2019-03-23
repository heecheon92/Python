# -*- coding: utf-8 -*-
import time
import sys

from random import randrange
from multiprocessing import Process
from tqdm import tqdm

strItWorks = """
#     ___     _             __      __                 _                _
#    |_ _|   | |_      o O O\ \    / /  ___      _ _   | |__    ___     | |
#     | |    |  _|    o      \ \/\/ /  / _ \    | '_|  | / /   (_-<     |_|
#    |___|   _\__|   TS__[O]  \_/\_/   \___/   _|_|_   |_\_\   /__/_   _(_)_
#  _|=====|_|=====| {======|_|=======|_|===|__|======|_|=====|_|====|_|=====|
#  "`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'" `-0-0-' """

listItWorks = strItWorks.split("\n")

def bannerMaker(aString):
    textString = aString
    textList = list(textString)
    #cursorBlock = chr(9608) * len(textList)
    outputString = ""

    for i in range(len(textList)):

        if i < len(textList)-1:
            textList[i] = textList[i].upper()
            textList[i-1] = textList[i-1].lower()
            outputString = "".join(textList)

        else:
            outputString = outputString.title()
        sys.stdout.write("\r"+outputString)
        #sys.stdout.write("\r\n"+blockList[i])
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")
    sys.stdout.flush()

def bannerCountdown(aNum):
    for i in range(aNum, -1, -1):
        sys.stdout.write("\r This program will close in: %d seconds" %(i))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")
    sys.stdout.flush()

def println(something):
    print(something)

def binDecorator(asciiTxtGenerator):
    print("\033[2J")
    def binDecorated():
        print(strItWorks)
        binString = "$echo This is useful. 1> /dev/null"
        binList = list(binString)
        print("\n\n")
        bannerMaker(binString)
        asciiTxtGenerator()
        print("\n")

        ct = 0
        for i in binList:
            print(i, end='')
    time.sleep(3)
    return binDecorated()

@binDecorator
def asciiTxtGenerator():
    asciiText = """
    .__________________________.
    | .___________________. |==|              p1 = multiprocessing(target = P)
    | | ................. | |  | 0            p.start()      1       0       1       10             0x3AD         1        1011
    | | ::::Apple ][::::: | |  |    1 0         1    0      1       1      111       1       1
    | | MacOS High Sierra | |  |
    | | ::::::::::::::::: | |  |\t\t  ██╗ ██╗ ██╗    ██╗██████╗ ██╗███╗   ██╗    ██╗██████╗  █████╗ ███████╗██╗  ██╗   0   1
    | | ::::::::::::::::: | |  |\t\t ████████╗██║   ██╔╝██╔══██╗██║████╗  ██║   ██╔╝██╔══██╗██╔══██╗██╔════╝██║  ██║
    | | ::::::::::::::::: | |  |\t\t ╚██╔═██╔╝██║  ██╔╝ ██████╔╝██║██╔██╗ ██║  ██╔╝ ██████╔╝███████║███████╗███████║   1
    | | @Heecheon Park    | | ,|\t\t ████████╗╚═╝ ██╔╝  ██╔══██╗██║██║╚██╗██║ ██╔╝  ██╔══██╗██╔══██║╚════██║██╔══██║   0
    | | █ █ █ █ █ █ | █ █ | |  |\t\t ╚██╔═██╔╝██╗██╔╝   ██████╔╝██║██║ ╚████║██╔╝   ██████╔╝██║  ██║███████║██║  ██║   0
    | !___________________! |(c|\t\t  ╚═╝ ╚═╝ ╚═╝╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    !_______________________!__!
   /  ` 1 2 3 4 5 6 7 8 9 0 - = \\                *                    cat $ifconfig |grep "inet " > UrIpAddress.txt
  /  q w e r t y u i o p [ ] <== \\        10 10  1  1          10           0       0 1       11           1      0       1
 /  a s d f g h j k l ; \\  Enter  \\      0  01             1        0            1
/   z x c v b n m , . / ?  Shift   \\                                    TEEMO ^오^
(  [][][][][____________][][][][]  )            1           0 0      00    0 1            1             1          1     0
 \ ------------------------------ /       while (fingerprint != True):
  \______________________________/            tp = sendAmail(MY@EMAIL.COM)"""

    asciiList = asciiText.split("\n")

    for char in asciiList:
        print(char)
        time.sleep(0.1)

def progressBar(scale):
    for i in tqdm(range(scale)):
        time.sleep(0.001)
        pass


def main():

    bannerMaker("This is my custom screen saver! It's pretty cool ain't it?")
    bannerMaker("If you miss the password or fingerprint, your picture will be sent to => my@email.com")
    progressBar(1312)
    progressBar(343)
    progressBar(2781)
    progressBar(899)
    print("\033[2J")
    emptyLine30 = "\n"*30
    emptyLine15 = "\n"*15
    time.sleep(3)
    StrGoodbye = """
\t\t#
\t\t#
\t\t#          GGGGGGGGGGGGG     OOOOOOOOO          OOOOOOOOO     DDDDDDDDDDDDD             BBBBBBBBBBBBBBBBB   YYYYYYY       YYYYYYYEEEEEEEEEEEEEEEEEEEEEE
\t\t#       GGG::::::::::::G   OO:::::::::OO      OO:::::::::OO   D::::::::::::DDD          B::::::::::::::::B  Y:::::Y       Y:::::YE::::::::::::::::::::E
\t\t#     GG:::::::::::::::G OO:::::::::::::OO  OO:::::::::::::OO D:::::::::::::::DD        B::::::BBBBBB:::::B Y:::::Y       Y:::::YE::::::::::::::::::::E
\t\t#    G:::::GGGGGGGG::::GO:::::::OOO:::::::OO:::::::OOO:::::::ODDD:::::DDDDD:::::D       BB:::::B     B:::::BY::::::Y     Y::::::YEE::::::EEEEEEEEE::::E
\t\t#   G:::::G       GGGGGGO::::::O   O::::::OO::::::O   O::::::O  D:::::D    D:::::D        B::::B     B:::::BYYY:::::Y   Y:::::YYY  E:::::E       EEEEEE
\t\t#  G:::::G              O:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B::::B     B:::::B   Y:::::Y Y:::::Y     E:::::E
\t\t#  G:::::G              O:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B::::BBBBBB:::::B     Y:::::Y:::::Y      E::::::EEEEEEEEEE
\t\t#  G:::::G    GGGGGGGGGGO:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B:::::::::::::BB       Y:::::::::Y       E:::::::::::::::E
\t\t#  G:::::G    G::::::::GO:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B::::BBBBBB:::::B       Y:::::::Y        E:::::::::::::::E
\t\t#  G:::::G    GGGGG::::GO:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B::::B     B:::::B       Y:::::Y         E::::::EEEEEEEEEE
\t\t#  G:::::G        G::::GO:::::O     O:::::OO:::::O     O:::::O  D:::::D     D:::::D       B::::B     B:::::B       Y:::::Y         E:::::E
\t\t#   G:::::G       G::::GO::::::O   O::::::OO::::::O   O::::::O  D:::::D    D:::::D        B::::B     B:::::B       Y:::::Y         E:::::E       EEEEEE
\t\t#    G:::::GGGGGGGG::::GO:::::::OOO:::::::OO:::::::OOO:::::::ODDD:::::DDDDD:::::D       BB:::::BBBBBB::::::B       Y:::::Y       EE::::::EEEEEEEE:::::E
\t\t#     GG:::::::::::::::G OO:::::::::::::OO  OO:::::::::::::OO D:::::::::::::::DD        B:::::::::::::::::B     YYYY:::::YYYY    E::::::::::::::::::::E
\t\t#       GGG::::::GGG:::G   OO:::::::::OO      OO:::::::::OO   D::::::::::::DDD          B::::::::::::::::B      Y:::::::::::Y    E::::::::::::::::::::E
\t\t#          GGGGGG   GGGG     OOOOOOOOO          OOOOOOOOO     DDDDDDDDDDDDD             BBBBBBBBBBBBBBBBB       YYYYYYYYYYYYY    EEEEEEEEEEEEEEEEEEEEEE
\t\t#
\t\t#"""
    sys.stdout.write(StrGoodbye)
    print(emptyLine15)
    time.sleep(0.1)
    bannerCountdown(5)
    time.sleep(1)
    print("\033[2J")
    time.sleep(5)



if __name__ == "__main__":


    main()
