import pandas as pd 
import csv
class csv_handler:
    def __init__(self,csv_folder_path):
        self.path = csv_folder_path
    
    def load(self):
        csv.reader(path)
        


if __name__ == "__main__":
    path = "~/Documents/finance/depences/2022/avril.csv"
    processor = csv_handler(path)
    processor.load()