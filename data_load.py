import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} does not exist.")
            return None
        return pd.read_csv(self.filepath)