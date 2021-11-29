print("************************************************************")
import os
import csv
from fpdf import FPDF
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdf_components import PDF_MINER
from mtech_functions import top_mtech,credits_block_mtech,bottom_mtech
from btech_functions import top_btech,credits_block_btech,bottom_btech

from tqdm import tqdm


#START MAKING THE PDF (NOW FOR BTECH)


u_l_x=10   #UPPER LEFT X CO-ORDINATE
u_l_y=15   #UPPER LEFT Y CO-ORDINATE

pdf_w=420  #WIDTH OF RECTANGLE
pdf_h=297  #HEIGHT OF RECTANGLE


def top(roll,name,dis,y):
    #SETTING UP THE MAIN RECTANGLE

    u_l_x=10   #UPPER LEFT X CO-ORDINATE
    u_l_y=15   #UPPER LEFT Y CO-ORDINATE

    pdf_w=420  #WIDTH OF RECTANGLE
    pdf_h=297  #HEIGHT OF RECTANGLE

    pdf.rectangle(u_l_x,u_l_y,pdf_w-2*u_l_x,pdf_h-2*u_l_y)

    #TOP PART

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #=========================================================================
    # FOR IIT PATNA LOGO LEFT
    s_x=u_l_x
    s_y=u_l_y

    left_logo_w=50
    left_logo_h=30

    pdf.rectangle(s_x,s_y,left_logo_w,left_logo_h)  
    pdf.imagex_logo(s_x+10,s_y+1,42,32)

    #=========================================================================
    # for IIT PATNA TEXT MIDDLE
    s_x=u_l_x+left_logo_w
    s_y=u_l_y

    text_w=pdf_w-2*u_l_x-2*left_logo_w
    text_h=30

    pdf.rectangle(s_x,s_y,text_w,text_h)  
    pdf.imagex_main_text(s_x+5,s_y+2,text_w,text_h)

    #========================================================================
    # for IIT PATNA LOGO RIGHT

    s_x=s_x+text_w
    s_y=u_l_y

    right_logo_w=50
    right_logo_h=30

    pdf.rectangle(s_x,s_y,right_logo_w,right_logo_h)  
    pdf.imagex_logo(s_x+10,s_y+1,42,32)

    #========================================================================

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #DETAILS BOX

    s_x=u_l_x+left_logo_w+20
    s_y=u_l_y+30+3

    width_details=pdf_w-2*u_l_x-2*left_logo_w-2*20
    height_details=15

    pdf.rectangle(s_x,s_y,width_details,height_details) 

    #WRITING THE DETAILS INSIDE THE BOX

    #ROLL_NUMBER
    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2,s_y)
    pdf.cell(20, 9, 'Roll No:', 0, 1, 'C')


    pdf.set_font('Arial','B',7)
    pdf.set_xy(s_x+2+24.5,s_y+3)
    pdf.cell(15, 3, str(roll), 1, 1, 'L')


    #NAME

    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2+73,s_y)
    pdf.cell(10, 9, 'Name:', 0, 1, 'C')


    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2+10+75,s_y+3)
    pdf.cell(70, 4, str(name), 1, 1, 'C')


    #YEAR

    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2+73+130,s_y)
    pdf.cell(10, 9, 'Year of Admission:', 0, 1, 'C')


    pdf.set_font('Arial','B',8)
    pdf.set_xy(s_x+2+10+75+140,s_y+3)
    pdf.cell(25, 3, '20'+str(y), 1, 1, 'C')


    #PROGRAMME

    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+10.5,s_y+5)
    pdf.cell(10, 9, 'Programme:', 0, 1, 'C')


    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+10.5+23,s_y+3+5)
    pdf.cell(25, 3, 'Bachelor of Technology', 0, 1, 'C')

    #COURSE

    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2+63.5+10.5,s_y+5)
    pdf.cell(10, 9, 'Course:', 0, 1, 'C')


    pdf.set_font('Arial','B',10)
    pdf.set_xy(s_x+2+10.5+63.5+30,s_y+3+5)
    pdf.cell(25, 3, str(dis), 0, 1, 'C')


    
#CREDITS BLOCK

def credits_block(s_x,s_y,c_c,spi,cpi):
    s_x= s_x
    s_y= s_y#+68+42

    width=90
    height=5

    pdf.rectangle(s_x,s_y,width,height) 

    #CREDITS TAKEN
    pdf.set_font('Arial','B',8)
    pdf.set_xy(s_x+8,s_y-1.5)
    pdf.cell(10, 9, 'Credits Taken: '+str(c_c), 0, 1, 'C')

    #CREDITS CLEARED
    pdf.set_xy(s_x+35,s_y-1.5)
    pdf.cell(10, 9, 'Credits Cleared: '+str(c_c), 0, 1, 'C')

    #SPI
    pdf.set_xy(s_x+60,s_y-1.5)
    pdf.cell(10, 9, 'SPI:'+str(spi), 0, 1, 'C')

    #CPI
    pdf.set_xy(s_x+75,s_y-1.5)
    pdf.cell(10, 9, 'CPI:'+str(cpi), 0, 1, 'C')
    

def bottom():
    #BOTTOM PART
    pdf_w=420  #WIDTH OF RECTANGLE
    pdf_h=297  #HEIGHT OF RECTANGLE

    pdf.lines(10,215,410,215)

    #DATE OF ISSUE
    pdf.set_font('Arial','B',15)
    pdf.set_xy(15,245)
    pdf.cell(10, 9, 'Date of Issue:', 0, 1, 'L')

    #IIT PATNA STAMP
    pdf.stamp(160,230,52,52)

    #REGISTRAR
    pdf.sign(350,235,60,42)


name_roll_no={}
roll_dis={}
roll_subjects={}


sub_name={}
sub_ltp={}
sub_credit={}

with open('tut05/names-roll.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     print("hellooo")
     for row in reader:
         name_roll_no[row['Roll']]=row['Name']
         roll_dis[row['Roll']]=row['Roll'][4:6]

with open('tut05/subjects_master.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         sub_name[row['subno']]=row['subname']
         sub_ltp[row['subno']]=row['ltp']
         sub_credit[row['subno']]=row['crd']
         
         
with open('tut05/grades.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         roll_no=row['Roll']
         sem=int(row['Sem'])
         sub_code=row['SubCode']
         sub_type=row['Sub_Type']
         credit=int(row['Credit'])
         grade=row['Grade']
        
         if roll_no not in roll_subjects.keys(): 
            roll_subjects[roll_no]={}
            roll_subjects[roll_no][sem]=[]
            roll_subjects[roll_no][sem].append((credit,grade,sub_code,sub_type))
         else:
            if(sem not in roll_subjects[roll_no].keys()):
                roll_subjects[roll_no][sem]=[]
                roll_subjects[roll_no][sem].append((credit,grade,sub_code,sub_type))
            else:
                roll_subjects[roll_no][sem].append((credit,grade,sub_code,sub_type))


roll_result={}
roll_sem_wise={}

d={'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}


for r_no,s in roll_subjects.items(): 
    for k,v in s.items():
        
        credits=[v1[0] for v1 in v]
        grade=  [v1[1] for v1 in v]
        sub_code=[v1[2] for v1 in v]
        sub_type=[v1[3] for v1 in v]
        
        total=sum(credits)
        p=0
        for i in range(len(grade)):
            grade[i]=grade[i].strip()
            
            if(grade[i].endswith('*')):
                grade[i]=grade[i][:-1]
                
            p+=d[grade[i]]*credits[i]
            
        spi=p/total
        spi=round(spi,2)
        if(r_no not in roll_result.keys()):
            roll_result[r_no]=[]
            roll_sem_wise[r_no]=[]
            
        roll_sem_wise[r_no].append((k,sub_code,sub_type,grade))  
        roll_result[r_no].append((k,total,spi))
        

d={'CS':'Computer Science and Engineering','EE':'Electrical Engineering','ME':'Mechanical Engineering'}

flag=0
for r_no,s in tqdm(roll_result.items()):
    
    if('CS' in r_no or 'EE' in r_no):
        continue
    
    filepath="proj2/transcriptsIITP_12/"  
    
    if(r_no[2:4]=='01'):
        flag=1        
        pdf=PDF_MINER(orientation='L',unit='mm',format='A3')
        pdf.set_font("Times", size=10)
        pdf.add_page()
        top(r_no,name_roll_no[r_no],d[roll_dis[r_no]],r_no[0:2])
        
    else:
        print("mtech11111111")
        pdf=PDF_MINER(orientation='P',unit='mm',format='A4')
        pdf.set_font("Times", size=10)
        pdf.add_page()
        top_mtech(pdf,r_no,name_roll_no[r_no],d[roll_dis[r_no]],r_no[0:2])
        
    spi=[item[2] for item in s]
    credits_sem_wise=[item[1] for item in s]
    CPI=[]
    total_credits_sem=[]
    t=0
    c=0
    for i in range(len(credits_sem_wise)):
        t+=credits_sem_wise[i]
        c+=credits_sem_wise[i]*spi[i]
        
        temp=c/t
        temp=round(temp,2)
        CPI.append(temp)
        total_credits_sem.append(t)
             
    
    for i in range(len(roll_sem_wise[r_no])):
        fixed_line={"Sub. Code":[],"Subject Name":[ ],"L-T-P":[],
                        "CRD":[],"GRD":[]}
            
        for j in range(len(roll_sem_wise[r_no][i][2])):
            kl=roll_sem_wise[r_no][i]
            
            fixed_line["Sub. Code"].append(kl[1][j])
            fixed_line["Subject Name"].append(sub_name[kl[1][j]])
            fixed_line["L-T-P"].append(sub_ltp[kl[1][j]])
            fixed_line["CRD"].append(sub_credit[kl[1][j]])
            fixed_line["GRD"].append(kl[3][j])
            
            
        df=pd.DataFrame.from_dict(fixed_line)
        
        df=df.style.hide_index().set_caption("Semester "+str(i+1)).set_table_styles([{
        'selector': 'caption',
        'props': 'caption-side: bottom; font-size:1.25em;'
         }]).set_properties(**{'color': 'black !important','border': '1px black solid !important','text-align': 'center','background-color': 'white'} ).set_table_styles([{'selector': 'th','props': [('border', '1px black solid !important')]},{
        'selector': 'caption',
        'props': [('caption-side','inline-start'),('font-size','1.25em')]
         }]).set_properties(subset=['Subject Name'], **{'width': '300px'})
 
        
        path_to_table=r"C:\Users\Dell\Desktop\1901CE15_2021\proj2\storing_tables"
        new_path=os.path.join(path_to_table,"table_"+str(i)+".png")
        
        
        dfi.export(df,new_path)
        
        if(flag==1):
            if(i<4):
                pdf.imagex_table(u_l_x+10+95*i,u_l_y+50+2,new_path,height=7*(j+1))
                credits_block(u_l_x+10+95*i,u_l_y+50+2+2+7*(j+1)+2,credits_sem_wise[i],spi[i],CPI[i])
                
            else:
                pdf.imagex_table(u_l_x+10+95*(i-4),u_l_y+80+44+7,new_path,height=7*(j+1))
                credits_block(u_l_x+10+95*(i-4),u_l_y+80+44+7*(j+1)+9,credits_sem_wise[i],spi[i],CPI[i])
            
            if(i==3):
                pdf.lines(10,u_l_y+50+2+2+7*10+2,410,u_l_y+50+2+2+7*10+2)
            
            bottom()
    
        else:
            print("mtech11")
            if(i<2):
                pdf.imagex_table(u_l_x+25+70*i,u_l_y+50+2,new_path,60,4*(j+1))
                credits_block_mtech(pdf,u_l_x+25+70*i,u_l_y+50+2+2+4*(j+1)+2,credits_sem_wise[i],spi[i],CPI[i])
                
            else:
                pdf.imagex_table(u_l_x+25+70*(i-2),u_l_y+94+7,new_path,60,4*(j+1))
                credits_block_mtech(pdf,u_l_x+25+70*(i-2),u_l_y+50+44+4*(j+1)+9,credits_sem_wise[i],spi[i],CPI[i])
            
            if(i==2):
                pdf.lines(10,u_l_y+50+2+2+4*10+2,297,u_l_y+50+2+2+4*10+2)
    
            bottom_mtech(pdf)
    
    pdf.output(filepath+r_no+".pdf",'F')
    
    break




        
        
        
        
                
 
                
