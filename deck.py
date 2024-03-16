import pandas as pd
import random                                                               

class Deck():
    def __init__(self):
        self.data_set = pd.read_csv('data\\words_data.csv',encoding='utf-8')
        self.deck = {}
        self.dict_maker()
        self.Answered = []
        
    def dict_maker(self):
        for index, row in self.data_set.iterrows():
            row_dict = row.to_dict()
            self.deck[row_dict['word']] = row_dict['translation']
        
    def next_card(self):
        card = random.choice(list(self.deck.keys()))
        if card in self.Answered:
            card = self.next_card()
        return card                                                                                                                                                                                                                       