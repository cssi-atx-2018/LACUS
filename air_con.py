import csv
ac_dict = {}
states_dict = {}
with open('ac-sheet.csv','r') as f:
    reader = csv.reader(f)
    ac_dict = {rows[0]:rows[1:] for rows in reader}
with open('states-sheet.csv','r') as f:
    reader = csv.reader(f)
    states_dict = {rows[0]:rows[1:] for rows in reader}
