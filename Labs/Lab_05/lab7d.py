''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 4 (lab7d.py).  
''' 

import csv

def readCsv(filename): #CSV file reader
    list_of_dicts = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts

def writeCsv(filename, list_of_dicts): #Csv File writer
    with open(filename, 'w', newline='') as f:
        fieldnames = list_of_dicts[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)

def editCsv(list_of_dicts): #Change the data in csv file
    for row in list_of_dicts:
        if row.get('First Name') == 'Christopher':
            row['First Name'] = 'Chris'
        if row.get('Last Name') == 'Patal':
            row['Last Name'] = 'Patel'
        if row.get('Last Name') == 'Smith':
            row['Last Name'] = 'Nichols'
        if row.get('Address') == '81 Vanier':
            row['Address'] = '72 Princeton'
        if row.get('Last Name') == 'Geary':
            row['Address'] = '455 Bloor'
        if row.get('City') == 'North York':
            row['City'] = 'Toronto'
        if row.get('Country') == 'Canada':
            row['Country'] = 'CA'
    return list_of_dicts   

if __name__ == "__main__": #entry point
    inputFile = 'sample.csv'
    outputFile = 'sample2.csv'
    data = readCsv(inputFile)
    updatedData = editCsv(data)
    writeCsv(outputFile, updatedData)
