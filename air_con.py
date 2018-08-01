"""ac_dict = {"Trane XV20i TruComfort Variable Speed, Model 4TTV0024A": [22, 24000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0036A": [22, 36000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0048A": [22, 48000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0060A": [22, 60000]}"""
import csv
ac_dict = {}
states_dict = {'Texas': 10.98}
with open('ac-sheet.csv','r') as f:
    reader = csv.reader(f)
    ac_dict = {rows[0]:rows[1:] for rows in reader}
