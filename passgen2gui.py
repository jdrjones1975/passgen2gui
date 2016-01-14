from tkinter import *
import random
import os
import string

charset = string.punctuation + string.ascii_letters #string of characters for random password generation

bestDice = 6 #initialize random slider to this value
bestRandom = 16 #initialize diceware wordlength slider to this valu

ver = 0.031 #ver 0.03 is the first GUI version, 031 added Maori dic, some code cleanup
    
def diceware(length):
    dic = {} #creates empty dictionary for key/values from dicewaremaster.txt
    f = open('dicewaremaster.txt', 'r') #opens dicewaremaster file
    for l in f:
        k, v = l.split()
        if k in dic:
            dic[k].extend(v)
        else:
            dic[k] = [v]
    f.close() #closes txt file
    global password
    password = []
    for i in range(0,length):
        ones = (random.randint(1,6))
        tens = 10 * (random.randint(1,6))
        huns = 100 * (random.randint(1,6))
        thous = 1000 * (random.randint(1,6))
        tenthous = 10000 * (random.randint(1,6))
        rawRoll = tenthous + thous + huns + tens + ones
        rawRoll = str(rawRoll)
        password.append(dic[rawRoll])

    flatPass = list(flatten(password))
    password = ' '.join(flatPass)
    dic = {}
    passlabel.configure(text = password)

def dicewareMaori(length):
    dic = {} #creates empty dictionary for key/values from dicewaremaster.txt
    f = open('dicewaremaori.txt', 'r') #opens dicewaremaster file
    for l in f:
        k, v = l.split()
        if k in dic:
            dic[k].extend(v)
        else:
            dic[k] = [v]
    f.close() #closes txt file
    global password
    password = []
    for i in range(0,length):
        ones = (random.randint(1,6))
        tens = 10 * (random.randint(1,6))
        huns = 100 * (random.randint(1,6))
        thous = 1000 * (random.randint(1,6))
        tenthous = 10000 * (random.randint(1,6))
        rawRoll = tenthous + thous + huns + tens + ones
        rawRoll = str(rawRoll)
        password.append(dic[rawRoll])

    flatPass = list(flatten(password))
    password = ' '.join(flatPass)
    dic = {}
    passlabel.configure(text = password)


def flatten(lst):
    for elem in lst:
        if type(elem) in (tuple, list):
            for i in flatten(elem):
                yield i
        else:
            yield elem

def randomPassword(length):
    global password
    password = ''.join(random.choice(charset) for k in range(length))
    passlabel.configure(text = password)

def copyToClip(element):
    os.system("echo '%s' | pbcopy" % element)
    print (element, "is in the clipboard")

def clearClip():
    trash = ''
    os.system("echo '%s' | pbcopy" % trash)
    reset()

def reset():
    global password
    password = 'password1'
    passlabel.configure(text = password)

window = Tk()
window.title("PassGen Gui")

password = 'password1'

frame1 = Frame(window)

randomScale = Scale(frame1, from_=1, to=64, orient=HORIZONTAL)
randomScale.set(bestRandom)

dicewareScale = Scale(frame1, from_=1, to=10, orient=HORIZONTAL)
dicewareScale.set(bestDice)

randomScale.grid(row=0, column=0, pady = 5)
dicewareScale.grid(row=0, column=1, pady = 5)

genRandom = Button(frame1, text = "Random Password")
genRandom.configure(command = lambda : randomPassword(randomScale.get()))

genDice = Button(frame1, text = "Diceware English")
genDice.configure(command = lambda : diceware(dicewareScale.get()))

genMaori = Button(frame1, text = "Diceware Maori")
genMaori.configure(command = lambda : dicewareMaori(dicewareScale.get()))

genRandom.grid(row = 1, column = 0)
genDice.grid(row = 1, column = 1)
genMaori.grid(row = 2, column = 1)

passlabel = Label(window, text = password)
passlabel.pack(pady = 10)
frame1.pack()

copy = Button(window, text = "Copy Password")
copy.configure(command = lambda : copyToClip(password))
copy.pack()

clear = Button(window, text = "Clear Clipboard")
clear.configure(command = clearClip)
clear.pack()


