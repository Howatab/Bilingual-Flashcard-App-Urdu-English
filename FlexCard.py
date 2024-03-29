import ttkbootstrap as ttk
import pandas as pd
from PIL import Image, ImageTk
from tkinter import Canvas,PhotoImage
from deck import Deck


URDU_FONT = "Jameel Noori Nastaleeq"

class Card:
    def __init__(self, window) -> None:
            self.canvas = Canvas(master=window, width=830, height=576 )
            self.canvas.grid(column=0,columnspan=3)
            self.english_text = None
            self.urdu_text = None
            self.canvas.config(background="#B1DDC6")
            self.image_path_front = "images/card_front.png"  # Ensure the correct path
            self.image_path_back = "images/card_back.png"  # Ensure the correct path
            self.current_image = None
            self.deck_cards = Deck()
            self.Utext = self.deck_cards.next_card()
            self.Etext = self.deck_cards.deck[self.Utext]
            self.identifier = 'u'
            self.display_front()
            
    
    def text_update(self):
        self.Utext = self.deck_cards.next_card()
        self.Etext = self.deck_cards.deck[self.Utext]
        self.change_text()
    
    def display_front(self):
        try:
            self.current_image = ImageTk.PhotoImage(Image.open(self.image_path_front))
        except FileNotFoundError:
            print(f"{self.image_path_front} NOT FOUND")
        else:
            self.identifier = 'e'
            self.canvas.create_image(415, 288, image=self.current_image)
            self.canvas.create_text(415,100,text="English",font=('montserrat',30,'bold'))
            self.english_text = self.canvas.create_text(415,288,text=self.Etext,font=('montserrat',60,'bold'))
    
    
    def display_back(self):
        try:
            self.current_image = ImageTk.PhotoImage(Image.open(self.image_path_back))
        except FileNotFoundError:
            print(f"{self.image_path_back} NOT FOUND")
        else:
            self.identifier = 'u'
            self.canvas.create_image(415, 288, image=self.current_image)
            self.canvas.create_text(415,100,text="اردو" , font=(URDU_FONT,50,'bold'))
            self.urdu_text = self.canvas.create_text(415,288,text=self.Utext , font=(URDU_FONT,100,'bold'))
    
    def change_text(self):
        if self.identifier == 'u':
            self.canvas.itemconfig(self.urdu_text , text = self.Utext)
        elif self.identifier == 'e':
            self.canvas.itemconfig(self.english_text,text = self.Etext)
            
    def update_score(self):
        return f"{len(self.deck_cards.Answered)}"