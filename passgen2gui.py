from tkinter import *
import random
import os

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'
specChars = '!@#$%^&*()-=_+,.<>?/\| '
charset = lowerCase + upperCase + digits + specChars

bestDice = 6
bestRandom = 16

dic = {} #creates empty dictionary for key/values from dicewaremaster.txt
    
f = open('dicewaremaster.txt', 'r') #opens dicewaremaster file
for l in f:
    '''
    writes diceware dictionary to dic
    '''
    k, v = l.split()
    if k in dic:
        dic[k].extend(v)
    else:
        dic[k] = [v]
f.close() #closes txt file

def diceware(length):
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
    global password
    password = ''
    os.system("echo '%s' | pbcopy" % password)
    reset()
    print (password, "is in the clipboard")

def reset():
    global password
    password = ''
    passlabel.configure(text = password)

window = Tk()

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

genDice = Button(frame1, text = "Diceware Password")
genDice.configure(command = lambda : diceware(dicewareScale.get()))

genRandom.grid(row = 1, column = 0)
genDice.grid(row = 1, column = 1)

passlabel = Label(window, text = password)
passlabel.pack(pady = 10)
frame1.pack()

copy = Button(window, text = "Copy Password")
copy.configure(command = lambda : copyToClip(password))
copy.pack()

clear = Button(window, text = "Clear Clipboard")
clear.configure(command = clearClip)
clear.pack()


