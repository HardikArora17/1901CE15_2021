

                                                                        #END SEM ASSIGNMENT#
#NAME-HARDIK ARORA
#ROLL NUMBER -1901CE15
	

ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}

#IMPORTING THE LIBRARIES
import os
import numpy as np
import matplotlib as plt
import pandas as pd
from openpyxl import Workbook
from tqdm import tqdm



#FUNCTION FOR GETTING THE DEATILS OF A STUDENT CORRESPONDING TO HIS/HER ROLL NUMBER
def get_student_details(roll_no):
    global count_na
    df=pd.read_csv('tut07/studentinfo.csv')
    
    for index,row in df.iterrows():
        if(row[1]==roll_no):
            return (row['Name'],row['email'],row['aemail'],row['contact'])
    
    return ("NA_IN_STUDENTINFO","NA_IN_STUDENTINFO","NA_IN_STUDENTINFO","NA_IN_STUDENTINFO")    


#THIS FUNCTION TAKES THE LTP STRING AS INPUT AND RETURNS THE LIST OF FEEDBACK TYPES THAT SHOULD BE PRESENT FOR THAT PARTICULAR COURSE
#FOR EXAMPLE COURSE CE305 HAS LTP VALUE '3-3-0'
# THEN IT RETURNS [1,2]

def course_ltp_count(value):
    ltp=value.split('-')
    count=0
    d=[]
    for i,c in enumerate(ltp):
        if(c!='0'):     
            d.append(i+1)
    
    d=list(set(d))
    return d

#THIS FUNCTION RETUNRNS A DICT CORRESPONDING TO ALL THE DIFFERENT COURSES PRESENT IN THE COURSE MASTER FILE,ALONG WITH THEIR LTP LISTS.
#EXAMPLE - {'CE305':[1,2],'CE405':[2,3]}

def extract_course_information():
    
    df1=pd.read_csv(r'tut07/course_master_dont_open_in_excel.csv')

    sub_no_courses={}
    
    subject=list(df1['subno'])
    ltp=list(df1['ltp'])
    
    for s,l in zip(subject,ltp):    
        
        score=course_ltp_count(l)           
        if(len(score)==0):     #CHECKING IF THE COURSE IS WITH LTP '0-0-0'
            continue
        
        sub_no_courses[s]=course_ltp_count(l)
 
    return sub_no_courses
   
 
#THIS FUNCTION EXTRACTS ALL THE COURSES REGISTERED FOR THE ROLL NUMBERS PRESENT IN COURSES REGISTERED FILE AND RETURNS THEM IN THE FORM OF A DICTIOANRY

def extract_student_information():
    
    roll_no_courses={}

    df=pd.read_csv('tut07/course_registered_by_all_students.csv')

    r_no=list(df['rollno'])
    sub=list(df['subno'])
    reg_sem=list(df['register_sem'])
    sch_sem=list(df['schedule_sem'])
    subject_list=list(extract_course_information().keys())
    
    for r,s,s1,s2 in zip(r_no,sub,reg_sem,sch_sem): 
        
        if (s not in subject_list):               #CHECKING IF THE COURSE IS PRESENT IN THE COURSE_MASTER LIST AND IS NOT A COURSE WITH LTP '0-0-0'
            continue
        
        if(r not in roll_no_courses.keys()):
        	roll_no_courses[r]={}
         
        if(s not in roll_no_courses[r].keys()):
        	roll_no_courses[r][s]=[]
         
        roll_no_courses[r][s]=[s1,s2]
        
    return roll_no_courses
    


#THIS FUNCTION EXTRACTS ALL THE COURSES FOR WHICH FEED BACK IS GIVEN BY ALL THE ROLL NUMBERS  ALONG WITH THEIR FEEDBACK TYPE AND RETURNS THEM IN THE FORM OF A DICTIOANRY

def analyse_feedback():
    
    path_to_feedback=r'tut07\course_feedback_submitted_by_students.csv'
    feed=pd.read_csv(path_to_feedback)

    roll_no=feed['stud_roll']
    course=feed['course_code']
    type=feed['feedback_type']
    
    analyse_roll_no={}
    
    for k1,k2,k3 in zip(roll_no,course,type):
        if(k1 not in analyse_roll_no.keys()):
            analyse_roll_no[k1]={}
            
        if(k2 not in analyse_roll_no[k1].keys()):
            analyse_roll_no[k1][k2]=[]
            
        analyse_roll_no[k1][k2].append(k3)
        
    for k1 in analyse_roll_no.keys():
        for k2 in analyse_roll_no[k1].keys():
            analyse_roll_no[k1][k2]=list(set(analyse_roll_no[k1][k2]))
        
    return analyse_roll_no
            


output_file_name = "tut07/course_feedback_remaining.xlsx" 

#THIS FUNCTION TAKES CERTAIN VALUES AS INPUT AND WRITES THEM TO THE COURSE_REMAINING FILE

def write_output_file(r,subject,d1,x):
    roll_no=r
    register_sem=d1[0]
    schedule_sem=d1[1]
    subno=subject
    name,email,aemail,contact=get_student_details(r)
    
    x.append([str(roll_no),str(register_sem),str(schedule_sem),str(subno),str(name),str(email),str(aemail),str(contact)])
    
            
            
roll_no_courses = extract_student_information()
courses_ltp= extract_course_information()
analysed_roll_no=analyse_feedback()


fixed_line=["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"]

wb1=Workbook()
wb=wb1.create_sheet('Sheet1',0)
wb.append(fixed_line) 


for roll in list(roll_no_courses.keys()):
    
    if(roll not in analysed_roll_no.keys()):
        course_taken=roll_no_courses[roll]
        for c in course_taken.keys():
            write_output_file(roll,c,course_taken[c],wb)
        
        continue
        
    filled_form=analysed_roll_no[roll]
    course_taken=roll_no_courses[roll]
    
    for c in course_taken.keys():
        if(len(courses_ltp[c])==0):
            continue
        
        if(c not in filled_form.keys()):
            write_output_file(roll,c,course_taken[c],wb)
            
        else:
            if(filled_form[c]!=courses_ltp[c]):
                for k in courses_ltp[c]:
                    if(k not in filled_form[c]):
                        write_output_file(roll,c,course_taken[c],wb)
                        break
                        

wb1.save(output_file_name)    
                        
            




            
        
        
     
     
    
    
    
    
    
