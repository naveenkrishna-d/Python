from data_processing.load import load_data
from data_processing.process import process_data
from data_processing.save import save_data

source = "data_source"
destination = "data_destination"
data = "sample data"

load_data(source)            # Output: Loading data from data_source
processed_data = process_data(data)  # Output: Processing data: sample data
save_data(processed_data, destination)  # Output: Saving data to data_destination
print(processed_data)