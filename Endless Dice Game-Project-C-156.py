# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:08:33 2022

@author: PC_RC
"""

from tkinter import*
from PIL import ImageTk, Image
import random
root = Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background = "yellow2")

img = ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))

player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_score_label = Label(root, bg = "royal blue", fg = "white")
player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_score_label = Label(root, bg = "royal blue", fg = "white")
player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "chocolate1", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_dice_label["text"] = "Player 1 Dice Random Number: " + str(random_no)
    player1_score = player1_score + random_no
    
player1_button = Button(root, image = img, command  = player1)
player1_button.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(1,6)
    random_dice_label["text"] = "Player 2 Dice Random Number: " + str(random_no2)
    player2_score = player2_score + random_no2

player2_button = Button(root, image = img, command = player2)
player2_button.place(relx = 0.9, rely = 0.6, anchor = CENTER)

root.mainloop()