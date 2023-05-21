import csv
from prediction.models import Passenger

path="../../titanic/database.csv"
with open(path, mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        name = lines[2]
        age = int(float(lines[4]))
        gender = lines[3]
        pc = lines[1]
        p1 = Passenger(name=name, age=age, pc=pc, gender=gender)
        p1.save()

"""
id,Pclass,Name,Sex,Age
0,Third,Braund,Male,22.0
"""