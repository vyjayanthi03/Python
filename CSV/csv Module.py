import csv

with open('C:Users/SSS2015046/Desktop/csvnew.csv', 'r') as csv_test:   #To read CSV
    # csv_reader = csv.reader(csv_test)
    csv_reader = csv.DictReader(csv_test)   #Dictionary
    for data in csv_reader:
        # print(data)
        print(data['Login email'])

# with open('C:Users/SSS2015046/Desktop/csv.csv', 'r') as csv_test:   #To read CSV
#     csv_reader = csv.reader(csv_test)
#
#     with open('C:Users/SSS2015046/Desktop/csvnew.csv','w') as csv_test_new:    #To write data to new file
#         csv_writer = csv.writer(csv_test_new, delimiter='\t')  #Separate by tab space
#
#     # next(csv_reader)    #To loop over 1st line/skip 1st line
#
#         for csv_r_data in csv_reader:
#             # print(csv_r_data)   #Print all lines
#             # print(csv_r_data[0])  #Print index 0 libe ie., 1st line
#             output = csv_writer.writerow(csv_r_data) #To write data to new file row by row
    #             print(csv_r_data)
