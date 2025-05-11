import pandas as pd
class CreateReport:

    def __init__(self, dataframe):
        self.dataframe = dataframe
       
    def save_to_csv(self, filepath: str):
        self.dataframe.to_csv(filepath)
