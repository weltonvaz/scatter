import csv
with open('PHI.csv') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
       print(row)
