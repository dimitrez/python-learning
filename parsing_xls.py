import csv
import re

price="/home/graff/Desktop/Price.csv"

with open(price) as csv_file:
    reader = csv.reader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        if row[0] != '' and row[17] != '0.00':
            artikul = row[1]
            img = row[2]
            img = img[12:-9]
            artikulManufactirer = row[3]
            categoty = row[4]
            brand_name = row[5]
            year = row[6]
            name = row[7]
            price_uah = row[17]

            print(artikul,img,categoty,brand_name,year,name,price_uah)