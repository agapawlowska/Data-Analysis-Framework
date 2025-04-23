from data_load import DataLoader
from data_clean import DataCleaner
from data_analyze import DataAnalyzer
from report import CreateReport

#Load data
data_loader = DataLoader(r"D:\Aga\Data Analysis Framework\sample_sales_data.csv")
raw_data = data_loader.load_data()

#Initiate DataCleaner
data_cleaner = DataCleaner(raw_data)
#summarise data before cleaning
print("Raw data summary:")
data_cleaner.summary()
data_cleaner.remove_excess_spaces('region')
data_cleaner.remove_excess_spaces('product')
data_cleaner.format_data('date', 'date')
data_cleaner.format_data('unit_price', 'number')
data_cleaner.format_data('units_sold', 'number')
data_cleaner.fill_total_sales()
data_cleaner.remove_na()

print("Clean data summary:")
data_cleaner.summary()

cleaned_data = data_cleaner.dataframe
