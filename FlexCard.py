import ttkbootstrap as ttk
import pandas as pd
import random
from PIL import Image, ImageTk
from tkinter import Canvas,PhotoImage

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
            self.display_front()
    

    def display_front(self):
        try:
            self.current_image = ImageTk.PhotoImage(Image.open(self.image_path_front))
        except FileNotFoundError:
            print(f"{self.image_path_front} NOT FOUND")
        else:
            self.canvas.create_image(415, 288, image=self.current_image)
            self.canvas.create_text(415,100,text="English",font=('montserrat',30,'bold'))
            self.english_text = self.canvas.create_text(415,288,text="English",font=('montserrat',70,'bold'))
    
    
    def display_back(self):
        try:
            self.current_image = ImageTk.PhotoImage(Image.open(self.image_path_back))
        except FileNotFoundError:
            print(f"{self.image_path_back} NOT FOUND")
        else:
            self.canvas.create_image(415, 288, image=self.current_image)
            self.canvas.create_text(415,100,text="اردو" , font=(URDU_FONT,50,'bold'))
            self.urdu_text = self.canvas.create_text(415,288,text="اردو" , font=(URDU_FONT,100,'bold'))
    
    def change_text(self,identifier,word):
        if identifier == 'u':
            self.canvas.itemconfig(self.urdu_text , text = word)
        elif identifier == 'e':
            self.canvas.itemconfig(self.english_text,text = word)