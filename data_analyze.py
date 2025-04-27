import pandas as pd
class DataAnalyzer:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def overall_sales(self):
        overall_sales = self.dataframe.groupby('product')['total_sales'].sum().sort_values(ascending=False)
        return overall_sales
    
    def bestseller_per_region(self):
        region_bestsellers = self.dataframe.groupby(['region','product'])['total_sales'].sum().unstack().fillna(0)
        #total sales
        total_sales = region_bestsellers.values.sum()
        region_bestsellers_percentage = (region_bestsellers / total_sales) * 100
        region_bestsellers_percentage = region_bestsellers_percentage.round(2)

        return region_bestsellers, region_bestsellers_percentage
    
    def best_sales_rep(self):
        highest_sales_rep = self.dataframe.groupby('sales_person')['total_sales'].sum().sort_values(ascending=False)
        return highest_sales_rep
    
    def highest_sales_where(self):
        highest_sales_region = self.dataframe.groupby('region')['total_sales'].sum().sort_values(ascending=False)
        return highest_sales_region

    def highest_sales_when(self, nr_of_entries):
        try:
            nr_of_entries = int(nr_of_entries)
        except ValueError:
            raise ValueError(f"nr_of_entries must be an integer, got {type(nr_of_entries).__name__} instead.")

        self.dataframe['date'] = pd.to_datetime(self.dataframe['date'], errors='coerce')
        highest_sales_by_date = self.dataframe.groupby(self.dataframe['date'].dt.date)['total_sales'].sum()
        return highest_sales_by_date.sort_values(ascending=False).head(nr_of_entries)
