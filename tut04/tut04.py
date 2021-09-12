import os
import csv
from openpyxl import Workbook

os.mkdir('tut04/output_by_subject')
os.mkdir('tut04/output_individual_roll')

i=0
roll_no={}
sub_no={}

import csv
with open('tut04/regtable_old.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        if(row['rollno'] not in roll_no.keys()):
            roll_no[row['rollno']]=[]
            roll_no[row['rollno']].append((row['register_sem'],row['subno'],row['sub_type']))
        else:
            roll_no[row['rollno']].append((row['register_sem'],row['subno'],row['sub_type']))
        
        if(row['subno'] not in sub_no.keys()):
            sub_no[row['subno']]=[]
            sub_no[row['subno']].append((row['rollno'],row['register_sem'],row['sub_type']))
        else:
            sub_no[row['subno']].append((row['rollno'],row['register_sem'],row['sub_type']))
         

for r,v in roll_no.items():
    wb1=Workbook()
    wb=wb1.active
    filepath="tut04/output_individual_roll/"+r+".xlsx"     
    fixed_line=["roll_no","register_sem","subno","sub_type"]
    wb.append(fixed_line)

    for item in v:
        a=[]
        a=[r,item[0],item[1],item[2]]
        wb.append(a)

    wb1.save(filepath)
    
for r,v in sub_no.items():
    wb1=Workbook()
    wb=wb1.active
    filepath="tut04/output_by_subject/"+r+".xlsx"     
    fixed_line=["roll_no","register_sem","subno","sub_type"]
    wb.append(fixed_line)

    for item in v:
        a=[]
        a=[item[0],item[1],r,item[2]]
        wb.append(a)

    wb1.save(filepath)
    
