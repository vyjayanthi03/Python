import pandas as pd
import csv


with open('C:/Users/SSS2015046/Desktop/DB_Frontline Solutions Map.csv', 'r') as csv_f:
    csv_reader = csv.reader(csv_f)
    with open('C:Users/SSS2015046/Desktop/csvf.csv','w') as csv_test_new:
            csv_writer = csv.writer(csv_test_new, delimiter='\t')


