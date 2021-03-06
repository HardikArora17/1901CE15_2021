
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
from matplotlib.font_manager import FontProperties

plt.rcParams["font.family"] = "arial"

from stqdm import stqdm
import streamlit as st

def plot_df(df,path_to_save,i):
  fig, ax = plt.subplots()

  # hide axes
  fig.patch.set_visible(False)
  ax.axis('off')
  ax.axis('tight')
  tab = ax.table(cellText=df.values, colLabels=df.columns, loc='center', colWidths=[0.15, 0.6, 0.125, 0.06, 0.06],cellLoc='center')
  
  for (row, col), cell in tab.get_celld().items():
    cell.set_text_props(fontproperties=FontProperties(weight='bold'))
    
  tab.auto_set_font_size(False)
  tab.set_fontsize(11)
  fig.tight_layout()
  ax.set_title("Semester "+str(i+1),)
  tab.scale(1, 2)

  plt.savefig(path_to_save, dpi=200,bbox_inches='tight',pad_inches = 0)


def generate_transcripts(lor,reader_1,reader_2,reader_3,flag_stamp,flag_sign,generate_all_flag=0):
    
    not_present_files=[]
    u_l_x=10   #UPPER LEFT X CO-ORDINATE
    u_l_y=15   #UPPER LEFT Y CO-ORDINATE

    pdf_w=420  #WIDTH OF RECTANGLE
    pdf_h=297  #HEIGHT OF RECTANGLE


    name_roll_no={}
    roll_dis={}
    roll_subjects={}

    sub_name={}
    sub_ltp={}
    sub_credit={}


    for index,row in reader_1.iterrows():
        name_roll_no[row['Roll']]=row['Name']
        roll_dis[row['Roll']]=row['Roll'][4:6]


    for index,row in reader_2.iterrows():
        sub_name[row['subno']]=row['subname']
        sub_ltp[row['subno']]=row['ltp']
        sub_credit[row['subno']]=row['crd']
    
    
    for index,row in reader_3.iterrows():
        
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
    #st.write("taskk3 done")
    d={'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}

    
    for r_no,s in roll_subjects.items():
        
        
        for k,v in s.items():
            
            credits=[v1[0] for v1 in v]
            grade=  [v1[1] for v1 in v]
            sub_code=[v1[2] for v1 in v]
            sub_type=[v1[3] for v1 in v]
            
            total=sum(credits)
            clear_cred=0
            p=0
            for i in range(len(grade)):
                grade[i]=grade[i].strip()
                
                if(grade[i].endswith('*')):
                    grade[i]=grade[i][:-1]
                    
                p+=d[grade[i]]*credits[i]
                if(d[grade[i]]==0):
                    clear_cred+=0
                else:
                    clear_cred+=credits[i]
                    
            spi=p/total
            spi=round(spi,2)
            if(r_no not in roll_result.keys()):
                roll_result[r_no]=[]
                roll_sem_wise[r_no]=[]
                
            roll_sem_wise[r_no].append((k,sub_code,sub_type,grade))  
            roll_result[r_no].append((k,total,spi,clear_cred))
            

    d={'CS':'Computer Science and Engineering','EE':'Electrical Engineering','ME':'Mechanical Engineering',}

    
    present_files=[]
    
    for r in lor:
        if(r not in roll_result.keys()):
            not_present_files.append(r)
        else:
            present_files.append(r)
        
    if(generate_all_flag):
        pbar = stqdm(roll_subjects.keys())
    else:
        pbar = stqdm(present_files)
        
    item=0
    st.write()
    flag=0
    
    for r_no in pbar:
        
        if(generate_all_flag):
            variable=list(roll_subjects.keys())[item]
        else:
            variable=present_files[item]
        
        item+=1
        pbar.set_description("Generating..  "+str(variable))
        
        s=roll_result[r_no]
        #r_no= r_no[:2] +'1'+ r_no[3:]
               
        if(r_no[2:4]=='01'):
            flag=1        
            pdf=PDF_MINER(orientation='L',unit='mm',format='A3')
            pdf.set_font("Times", size=10)
            pdf.add_page()
            top_btech(pdf,r_no,name_roll_no[r_no],d[roll_dis[r_no]],r_no[0:2])
            
        else:
            r_no= r_no[:2] +'0'+ r_no[3:]
            pdf=PDF_MINER(orientation='P',unit='mm',format='A4')
            pdf.set_font("Times", size=10)
            pdf.add_page()
            top_mtech(pdf,r_no,name_roll_no[r_no],d[roll_dis[r_no]],r_no[0:2])
            
        spi=[item[2] for item in s]
        credits_sem_wise=[item[1] for item in s]
        clear_credits_sem_wise=[item[3] for item in s]
        
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
            #plot_df(df,new_path,i)
            if(flag==1):
                if(len(roll_sem_wise[r_no])<=8):
                    if(i<4):
                        pdf.imagex_table(u_l_x+10+95*i,u_l_y+50+2,new_path,height=7*(j+1))
                        credits_block_btech(pdf,u_l_x+10+95*i,u_l_y+50+2+2+7*(j+1)+2,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                        
                    else:
                        pdf.imagex_table(u_l_x+10+95*(i-4),u_l_y+80+44+7,new_path,height=7*(j+1))
                        credits_block_btech(pdf,u_l_x+10+95*(i-4),u_l_y+80+44+7*(j+1)+9,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                    
                    if(i==3):
                        pdf.lines(10,u_l_y+50+2+2+7*10+2,410,u_l_y+50+2+2+7*10+2)
                    
                    bottom_btech(pdf,flag_stamp,flag_sign)
                    
                else:
                    if(i<4):
                        pdf.imagex_table(u_l_x+10+95*i,u_l_y+50+2,new_path,height=5*(j+1))
                        credits_block_btech(pdf,u_l_x+10+95*i,u_l_y+50+2+2+5*(j+1)+2,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                        
                    elif(i<8):
                        pdf.imagex_table(u_l_x+10+95*(i-4),u_l_y+80+24+7,new_path,height=5*(j+1))
                        credits_block_btech(pdf,u_l_x+10+95*(i-4),u_l_y+80+24+5*(j+1)+9,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                    
                    else:
                        pdf.imagex_table(u_l_x+10+95*(i-8),u_l_y+80+74+7,new_path,height=7*(j+1))
                        credits_block_btech(pdf,u_l_x+10+95*(i-8),u_l_y+80+74+7*(j+1)+9,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                    
                        
                    if(i==3):
                        pdf.lines(10,u_l_y+50+2+2+5*10+2,410,u_l_y+50+2+2+5*10+2)
                    if(i==7):
                        pdf.lines(10,u_l_y+50+2+2+5*20+2,410,u_l_y+50+2+2+5*20+2)
                    
                    bottom_btech(pdf,flag_stamp,flag_sign)
                    
            else:
                #print("mtech11")
                if(i<2):
                    pdf.imagex_table(u_l_x+10+70*i,u_l_y+50+2,new_path,60,4*(j+1))
                    credits_block_mtech(pdf,u_l_x+10+70*i,u_l_y+50+2+2+4*(j+1)+2,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                    
                elif(i>=2 and i<4):
                    pdf.imagex_table(u_l_x+10+70*(i-2),u_l_y+80+20,new_path,60,4*(j+1))
                    credits_block_mtech(pdf,u_l_x+10+70*(i-2),u_l_y+80+20+2+4*(j+1)+9,credits_sem_wise[i],clear_credits_sem_wise[i],spi[i],CPI[i])
                
                if(i==2):
                    pdf.lines(10,u_l_y+50+2+2+4*10+2,297,u_l_y+50+2+2+4*10+2)
        
                bottom_mtech(pdf,flag_stamp,flag_sign)
        
        
        filepath="transcriptsIITP/"  
        
        pdf.output(filepath+r_no+".pdf",'F')
        
        
    st.write("Successfully Generated all the transcripts")
   
    if(len(not_present_files)>0):
        st.write("Roll numbers not present")
        st.write(" ")
        st.write(not_present_files)
        


            
            
            
            
                    
    
                    
