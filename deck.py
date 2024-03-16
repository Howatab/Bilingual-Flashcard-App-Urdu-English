import pandas as pd

class Deck():
    def __init__(self):
        self.data_set = pd.read_csv('data\\words_data.csv',encoding='utf-8')
        self.deck = {}
        self.dict_maker()
        
        
    def dict_maker(self):
        for index, row in self.data_set.iterrows():
            row_dict = row.to_dict()
            self.deck[row_dict['word']] = row_dict['translation']