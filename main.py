import ttkbootstrap as ttk
import pandas as pd
import random
from PIL import Image, ImageTk
from tkinter import Canvas,PhotoImage
from FlexCard import Card
from deck import Deck

BACKGROUND_COLOR = "#B1DDC6"
URDU_FONT = "Jameel Noori Nastaleeq"

#Basic Functionality
def wrong_button_click():
    
    card.text_update()
    card.display_back()
    Wrong_button.state(['disabled'])
    Right_button.state(['disabled'])
    next_button.state(['!disabled'])

def right_button_click():
    card.deck_cards.Answered.append(card.Utext)
    score.set(card.update_score())
    print(score)
    card.text_update()
    card.display_back()
    Wrong_button.state(['disabled'])
    Right_button.state(['disabled'])
    next_button.state(['!disabled'])

def next():
        card.display_front()
        Wrong_button.state(['!disabled'])
        Right_button.state(['!disabled'])
        next_button.state(['disabled'])
    

#---------------------UI SETUP------------------

window = ttk.Window(title="Flash Card",themename='journal' )
window.config(background=BACKGROUND_COLOR,padx=100,pady=50)
card = Card(window=window)
card.display_back()

style = ttk.Style()
style.configure('NoBorder.TButton', borderwidth=0, focuscolor='none', bordercolor='none', lightcolor='none', darkcolor='none', troughcolor='none')

try:
    photo_wrong = ImageTk.PhotoImage(Image.open('images\\wrong.png'))
    photo_right = ImageTk.PhotoImage(Image.open('images\\right.png'))
    photo_next = ImageTk.PhotoImage(Image.open('images\skip.png'))
except FileNotFoundError:
    print("CORRECT WRONG PNG NOT FOUND")

Wrong_button = ttk.Button(image= photo_wrong ,padding= 0,style='NoBorder.TButton',command=wrong_button_click )
Wrong_button.grid(column=0,row=2,sticky='e')
Wrong_button.state(["disabled"]) 

Right_button = ttk.Button(image= photo_right ,padding= 0,style='NoBorder.TButton',command=right_button_click )
Right_button.grid(column=2,row=2,sticky='w') 
Right_button.state(["disabled"]) 

next_button = ttk.Button(image=photo_next,padding= 0,style='NoBorder.TButton',command=next,state='[disabled]')
next_button.grid(column=4,row=0,sticky='w')


score = ttk.StringVar(value = "0")
score_label =ttk.Label(text="", textvariable=score, font=("montserrat",40,'bold') ,background= BACKGROUND_COLOR)
score_label.grid(column=4,row=2,sticky='w')


window.mainloop()