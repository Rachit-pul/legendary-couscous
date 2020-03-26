card_family=('Spades','Clubs','Hearts','Diamonds')
card_value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Tens':10,'Jacks':10,'Queen':10,'Kings':10,'Ace':11}
card_type=card_value.keys()
card_type=list(card_type)


import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

FileDir=''
File=sorted_alphanumeric(os.listdir('cards/'))
print(File)

class PlayerInfo:
    def __init__(self,chips):
        self.chips=chips
        self.plyrhand=[]
    def addtohand(self,plyrcard):
        self.plyrhand.append(plyrcard)

class DealerInfo:
    def __init__(self,chips=0):
        self.chips=chips
        self.delrhand=[]
    def addtohand(self,delrcard):
        self.delrhand.append(delrcard)

import random
class Deck():
    def __init__(self):
        i=0
        self.cardset=[]
        for x in card_family:
            for y in card_type:
                self.cardset.append(CardInfo(y,x,i))
                i += 1
    def random_select(self):
        abcde = random.choice(self.cardset)
        self.cardset.remove(abcde)
        return abcde

class CardInfo():
    def __init__(self,card_rank,family,number_pic):
        self.card_rank=card_rank
        self.family=family
        self.number_pic=number_pic
    def __str__(self):
        return f'{self.card_rank} of {self.family}'

player=PlayerInfo(1000)
dealer=DealerInfo()
playingdeck=Deck()
height=200


def sum_value(inhand):
    sum_in_hand=0
    for i in range(len(inhand)):
        sum_in_hand+=card_value[inhand[i][0]]
    if sum_in_hand > 21:
        return f'\n\nsum is {sum_in_hand} \n\t BUST!'
    else:
        return sum_in_hand

def hitorstay(choice_hit_stay):
    global height
    if choice_hit_stay.lower()=='hit':
        card_from_deck=playingdeck.random_select()
        a=card_from_deck.number_pic
        card_active=(card_from_deck.card_rank,card_from_deck.family)
        player.addtohand(card_active)
        FileDir = 'cards/' +File[a]
        m.img = img = ImageTk.PhotoImage(Image.open(FileDir))
        cimg = canvas.create_image(0,height,image=img,anchor="nw")
        height+=100
        label=Label(image=img)
        label.image=img
        rules.insert(END,f'\nyour new hand is \n {player.plyrhand}')
        tocheckforbust=sum_value(player.plyrhand)
        if type(tocheckforbust)==int:    
            rules.insert(END,f'\nthe sum now is: {tocheckforbust}')
        else:
            rules.insert(END,tocheckforbust)
            FileDir='cards/' + File[52]
            m.img= img = ImageTk.PhotoImage(Image.open(FileDir))
            cimg=canvas.create_image(250,300,image=img,anchor='nw')
            label=Label(image=img)
            label.image=img
            hitorstay_button.destroy()
    elif choice_hit_stay.lower()=='stay':
        rules.insert(END,'\nyou decided to stay,no change in your hand')
        stay_return= sum_value(player.plyrhand)
        rules.insert(END,f'\nyour sum still is: {stay_return}')
        rules.insert(END,'\nnow the dealer has to PLAY')
        b=sum_value(dealer.delrhand)
        height=200
        if(b>stay_return):
            rules.insert(END,f'\nthe dealer won,try again')
            FileDir='cards/' + File[53]
            m.img= img = ImageTk.PhotoImage(Image.open(FileDir))
            cimg=canvas.create_image(250,300,image=img,anchor='nw')
            label=Label(image=img)
            label.image=img
            hitorstay_button.destroy()
        while(stay_return>=b):
            card_from_deck=playingdeck.random_select()
            a=card_from_deck.number_pic
            FileDir='cards/'+File[a]
            m.img=img=ImageTk.PhotoImage(Image.open(FileDir))
            cimg=canvas.create_image(700,height,image=img,anchor="nw")
            height+=100
            label=Label(image=img)
            label.image=img
            card_active=(card_from_deck.card_rank,card_from_deck.family)
            dealer.addtohand(card_active)
            rules.insert(END,f'\nThe Dealer has {dealer.delrhand}')
            if type(sum_value(dealer.delrhand))==str:
                rules.insert(END,f'\ndealer bust , you won!')
                FileDir='cards/' + File[54]
                m.img= img = ImageTk.PhotoImage(Image.open(FileDir))
                cimg=canvas.create_image(250,300,image=img,anchor='nw')
                label=Label(image=img)
                label.image=img
                hitorstay_button.destroy()
                break
            elif(sum_value(dealer.delrhand)>sum_value(player.plyrhand)):
                rules.insert(END,'\ndealer won , try again!')
                FileDir='cards/' + File[53]
                m.img= img = ImageTk.PhotoImage(Image.open(FileDir))
                cimg=canvas.create_image(250,300,image=img,anchor='nw')
                label=Label(image=img)
                label.image=img
                hitorstay_button.destroy()
                break
    else:
        rules.insert(END,'\nincorrect choice please try again : ')

def takeinput():
	global hitorstay_text
	string=hitorstay_text.get()
	return string





m=tkinter.Tk()
rules=Text(m,height=8)
rules.pack()
rules.insert(END,'1.ace has the value 11 at all times and face cards have value 10\n2.going over 21 causes a bust\n3.the dealer will hit until they win<have a sum higher than the player> or go over 21<bust>')
canvas = Canvas(m,width=800, height=600, bg='green')
bgimg='background/blackjack.jpg'
bgimg=ImageTk.PhotoImage(Image.open(bgimg))
canvas.create_image(0,0,image=bgimg,anchor='nw')
canvas.pack()
label=Label(m,text='choose hit or stay')
hitorstay_text=tkinter.Entry(m)
hitorstay_button=tkinter.Button(m,text='send',bg='red',width=15,command=lambda : hitorstay(takeinput()))
hitorstay_button.pack()
label.pack()
hitorstay_text.pack()
for i in range(0,2):
    card_from_deck=playingdeck.random_select()
    a=int(card_from_deck.number_pic)
    card_active=(card_from_deck.card_rank,card_from_deck.family)
    player.addtohand(card_active)
    FileDir='cards/'+ File[a]
    m.img = img = ImageTk.PhotoImage(Image.open(FileDir))
    cimg = canvas.create_image(0,i*100,image=img,anchor="nw")
    label=Label(image=img)
    label.image=img
rules.insert(END,f'\n\nyour hand :\n{player.plyrhand}')
rules.insert(END,f'sum of the cards : {sum_value(player.plyrhand)}')
for i in range(0,2):
    card_from_deck=playingdeck.random_select()
    a=card_from_deck.number_pic
    card_active=(card_from_deck.card_rank,card_from_deck.family)
    dealer.addtohand(card_active)
    FileDir = 'cards/' + File[a]
    m.img=img = ImageTk.PhotoImage(Image.open(FileDir))
    cimg = canvas.create_image(700,i*100,image=img,anchor="nw")
    label=Label(image=img)
    label.image=img
rules.insert(END,f'\n\n The dealer has : \n{dealer.delrhand[0]}, {dealer.delrhand[1]}')

m.mainloop()
