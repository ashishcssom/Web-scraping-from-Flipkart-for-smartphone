# # Python code for scraping the Smartphone price from Flipkart
for i in range(1,51):
    page=i
    import os
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    import csv
    from flipkart_scrap import Flipkart
    Flipkart = Flipkart(page)
    Flipkart.page_load()
    Flipkart.create_csv_file()
    Flipkart.data_scrap()
    Flipkart.tearDown()
    print("Task completed")
    time.sleep(2)
import pandas as pd
from os import listdir
path=r"C:\Users\imash\Documents\flipkart/".replace("\\","/")
def list_of_files(dir_name,ext="csv"):
    return [f for f in listdir(dir_name) if f.endswith('.' + ext)]
filenames=list_of_files(path)
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ],axis=0)
combined_csv.to_csv("combine.csv",sep=',', encoding='utf-8', index=False)
