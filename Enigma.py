#!/usr/bin/python3

#Author: Jonathon Bryant
#This program will simulate that Enigma machince.

import re

#Substitution ciphers
alpha =     "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
RotorI =    "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
RotorII =   "AJDKSIRUXBLHWTMCQGZNPYFVOE"
RotorIII =  "BDFHJLCPRTXVZNYEIWGAKMUSQO"
Reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

#Dictionary for the corresponding number to the letter
#New thought probably could have done away with the dict and used alpha for letter to numbers
LtN = {'A':0,
       'B':1,
       'C':2,
       'D':3,
       'E':4,
       'F':5,
       'G':6,
       'H':7,
       'I':8,
       'J':9,
       'K':10,
       'L':11,
       'M':12,
       'N':13,
       'O':14,
       'P':15,
       'Q':16,
       'R':17,
       'S':18,
       'T':19,
       'U':20,
       'V':21,
       'W':22,
       'X':23,
       'Y':24,
       'Z':25}

#Holds the plugboard in a dict
PlugBd = {'A':'',
       'B':'',
       'C':'',
       'D':'',
       'E':'',
       'F':'',
       'G':'',
       'H':'',
       'I':'',
       'J':'',
       'K':'',
       'L':'',
       'M':'',
       'N':'',
       'O':'',
       'P':'',
       'Q':'',
       'R':'',
       'S':'',
       'T':'',
       'U':'',
       'V':'',
       'W':'',
       'X':'',
       'Y':'',
       'Z':''}

#Class for rotors
class rotors:
    rI = ""
    rII = ""
    rIII = ""

#Holds the plaintext and ciphertext
class text:
    pt = ""
    ct = ""

#Converts the plaintext to a string of just uppercase letters
def ConvertPt(pt):
    text.pt = text.pt.replace(" ", "")
    regex = re.compile('[^a-zA-Z]')
    text.pt = regex.sub('', text.pt)
    text.pt = text.pt.upper()

#Function for finding the correct Substitution on plugboard at beggining
def PboardFirst(pt):
    for key, value in PlugBd.items():
        if pt == key:
            pt = value
            return pt

    #Error code and just return something that makes no sense
    print("ERROR: PboardFirst")
    return 1

#Function for finding the correct Substitution on plugboard at end
def PboardLast(pt):
    for key, value in PlugBd.items():
        if pt == value:
            pt = key
            return pt

    #Error code and just return something that makes no sense
    print("ERROR: PboardLast")
    return 1

#Does all the substitutions and placement of the rotors
def EnD(RotorI, RotorII, RotorIII):
    r2count = 0

    for x in range(0,len(text.pt)):

        rotors.rIII = (rotors.rIII + 1) % 26

        if x % 26 == 0 and x != 0:
            rotors.rII = (rotors.rII + 1) % 26
            r2count = r2count + 1

        if r2count % 26 == 0 and r2count != 0:
            rotors.rI = (rotors.rI + 1) % 26

        Ptemp = PboardFirst(text.pt[x])
        temp = RotorIII[(LtN[Ptemp] + rotors.rIII) % 26]
        temp = RotorII[(LtN[temp] + rotors.rII) % 26]
        temp = RotorI[(LtN[temp] + rotors.rI) % 26]

        temp = Reflector[LtN[temp]]

        inv = RotorI.index(temp)
        temp = alpha[(inv - rotors.rI) % 26]
        inv = RotorII.index(temp)
        temp = alpha[(inv - rotors.rII) % 26]
        inv = RotorIII.index(temp)
        temp = alpha[(inv - rotors.rIII) % 26]
        Ptemp = PboardLast(temp)
        text.ct = text.ct + Ptemp

#Gets the starting position of rotors
def StartingPos():
    print("What is start position for RotorI?")
    rotors.rI = input()
    rotors.rI = rotors.rI.upper()
    rotors.rI = alpha.index(rotors.rI)
    print("What is start position for RotorII?")
    rotors.rII = input()
    rotors.rII = rotors.rII.upper()
    rotors.rII = alpha.index(rotors.rII)
    print("What is start position for RotorIII?")
    rotors.rIII = input()
    rotors.rIII = rotors.rIII.upper()
    rotors.rIII = alpha.index(rotors.rIII)

#Gets the plugboard settings
def PlugBoard():
    print("What letter do you want switched? 1 to end")

    choices = ''

    while choices != '1':
        print("What character? / Need 13 inputs with no two letters the same")
        choices = input()
        if choices != '1':
            choices = choices.upper()
            print("Change it to?")
            ch2 = input()
            ch2 = ch2.upper()
            PlugBd[choices] = ch2
            PlugBd[ch2] = choices

    for key, value in PlugBd.items():
        if value == '':
            PlugBd[key] = key

    print(PlugBd)

#Gets the plaintext to be encrypted
def GetPt():
    print("What is the plaintext?")
    text.pt = input()
    ConvertPt(text.pt)

#Determines the order of the rotors
def RottorOrder():
    print("What is the order of the rotors?")
    order = input()
    order = list(order)
    Rlist = []
    Rlist.append(RotorI)
    Rlist.append(RotorII)
    Rlist.append(RotorIII)
    EnD(Rlist[int(order[0]) - 1], Rlist[int(order[1]) - 1], Rlist[int(order[2]) - 1])

#Prints out the end result
def PrintCt():
    for x in range(0,len(text.ct)):
        if x % 50 == 0 and x > 0:
            print("")

        if x % 5 == 0 and x > 0:
            print(" ", end="")

        print(text.ct[x], end="")

    print("")

#Main function
def main():
    StartingPos()
    PlugBoard()
    GetPt()
    RottorOrder()
    PrintCt()

if __name__ == '__main__':
    main()
