
import csv

def serachByTime(csv_file):
    time = input('Time : ')

    for row in csv_file:
        if time == row[5]:
            print(row)

def serachByLab(csv_file):
    labN = input('enter the lab number : ')

    # this line will search for the lab number in the csv file and return all rows that have it.
    lab = "LAB " + labN
    for row in csv_file:
        if lab == row[8]:
            print(row)

# Open the CSV file
with open('Academic-Affairs-First-term-2024.csv', 'r') as file:
    csv_file = csv.reader(file)

    # Print menu
    print(' T -> serachByTime \n L -> serachByLab')

    # Assign choosing value
    src = input('choose :')

    if src.capitalize() == 'T':
        serachByTime(csv_file)
    elif src.capitalize() == 'L':
        serachByLab(csv_file)
    else:
        print('open your eyes')
