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
    card.display_back()

def right_button_click():
    card.display_front()



#--------------------Data Handling-----------------
deck_cards = Deck()
#---------------------UI SETUP------------------

window = ttk.Window(title="Flash Card" , themename='journal')
window.config(background=BACKGROUND_COLOR,padx=100,pady=50)

card = Card(window=window)
card.display_back()

style = ttk.Style()
style.configure('NoBorder.TButton', borderwidth=0 )

photo_wrong = ImageTk.PhotoImage(Image.open('images\wrong.png'))
photo_right = ImageTk.PhotoImage(Image.open('images\\right.png'))


Wrong_button = ttk.Button(image= photo_wrong ,padding= 0,style='NoBorder.TButton',command=wrong_button_click )
Wrong_button.grid(column=0,row=2,sticky='e') 

Right_button = ttk.Button(image= photo_right ,padding= 0,style='NoBorder.TButton',command=right_button_click )
Right_button.grid(column=2,row=2,sticky='w') 


window.mainloop()