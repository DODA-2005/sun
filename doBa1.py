import csv

def inputstud():
    with open('college.csv', 'a',) as f:
        writer = csv.writer(f)
        while True:
            sno = int(input("enter roll no: "))
            name = input('enter name: ')
            city = input('enter city: ')
            percent = int(input('enter percentage: '))
            writer.writerow([sno, name, city, percent])
            a = input('Add more records?')
            if a != 'yes':
                break

def readcollege():
    with open('college.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Check if the row has at least three elements before accessing row[2]
            if len(row) >= 3 and row[2].lower() == 'kolkata':
                print(row)

# Input student records
inputstud()

# Read and print records where the city is 'Kolkata'
readcollege()
