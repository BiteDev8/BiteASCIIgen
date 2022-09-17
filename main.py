from colorama import Fore, Back, Style, init
import pyfiglet

T = "BiteASCII"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

print(Fore.GREEN+"")
while True :
    x = str(input("insert c'que t'veux :"))
    print("[1]normal ")
    print("[2]Texte en police oblique ")
    print("[3]Texte en police 3D ")
    print("[4]Texte en police doh ")
    print("[5]Texte en police isométrique1 ")
    print("[6]Texte en police bubblehead ")
    print("[7]Texte en police numérique ")
    print("[8]Texte en police alligator ")
    print("[9]Texte en police banner3-D ")
    a = "q978Dctgqç2zdQ978Dctg978Dctgqç2qç978Dctgqç22DF4d"
    font = input()
    if font == "2" :
        a = "slant"
    elif font == "3" :
        a = "3-d"
    elif font == "4" :
        a = "doh"
    elif font == "5" :
        a = "isometric1"
    elif font == "6" :
        a = "bulbhead"
    elif font == "7" :
        a = "digital"
    elif font == "8" :
        a = "alligator"
    elif font == "9" :
        a = "banner3-D"
    elif font == "1" :
        ASCII_art_2 = pyfiglet.figlet_format(x)
    else :
        print("error")
        print("error")
        ASCII_art_2 = pyfiglet.figlet_format(x)
        print("error")
        print("error")
  
    if a != "q978Dctgqç2zdQ978Dctg978Dctgqç2qç978Dctgqç22DF4d" :
        ASCII_art_2 = pyfiglet.figlet_format(x, font = a)
    print(ASCII_art_2)

    
