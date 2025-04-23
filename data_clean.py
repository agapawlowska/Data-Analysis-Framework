import pandas as pd
from pandas.api.types import is_string_dtype

class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def remove_na(self, inplace = True):
        if inplace:
            self.dataframe.dropna(inplace = True)
            return None
        else:
            return self.dataframe
    
    def format_data(self, column_name, data_type):
        if column_name not in self.dataframe.columns:
            print(f"Column {column_name} does not exist")
            return None

        if data_type == 'date':
            self.dataframe[column_name] = pd.to_datetime(self.dataframe[column_name], errors='coerce')
        elif data_type == 'number':
            self.dataframe[column_name] = pd.to_numeric(self.dataframe[column_name], errors='coerce')
        elif data_type == 'string':
            self.dataframe[column_name] = self.dataframe[column_name].astype(str)
        else:
            print(f"Unsupported data type: {data_type}")

    def fill_total_sales(self):
        required_columns = ['unit_price', 'units_sold', 'total_sales']
        for column in required_columns:
            if column not in self.dataframe.columns:
                print(f"Missing column: {column}")
                return None

        try:
            self.dataframe['unit_price'] = pd.to_numeric(self.dataframe['unit_price'], errors='coerce')
            self.dataframe['units_sold'] = pd.to_numeric(self.dataframe['units_sold'], errors='coerce')        
        except:
            pass
        self.dataframe['total_sales'] = self.dataframe['total_sales'].fillna(self.dataframe['unit_price'] * self.dataframe['units_sold'])


    def remove_excess_spaces(self, column_name):
        if is_string_dtype(self.dataframe[column_name]):
            self.dataframe[column_name] = self.dataframe[column_name].str.strip()

    def data_summary(self):
        print("List of columns: ", list(self.dataframe.columns))
        print("Data types:\n", self.dataframe.dtypes)
        print("\nNaNs per column:\n", self.dataframe.isna().sum())
        