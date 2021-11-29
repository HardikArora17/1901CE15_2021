
import os
import csv
from fpdf import FPDF
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdf_components import PDF_MINER
from tqdm import tqdm


#START MAKING THE PDF (NOW FOR BTECH)


u_l_x=10   #UPPER LEFT X CO-ORDINATE
u_l_y=15   #UPPER LEFT Y CO-ORDINATE

pdf_w=210  #WIDTH OF RECTANGLE
pdf_h=297  #HEIGHT OF RECTANGLE


def top_mtech(pdf,roll,name,dis,y):
    #SETTING UP THE MAIN RECTANGLE

    u_l_x=10   #UPPER LEFT X CO-ORDINATE
    u_l_y=15   #UPPER LEFT Y CO-ORDINATE

    pdf_w=210  #WIDTH OF RECTANGLE
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
    
    pdf_w=297  #WIDTH OF RECTANGLE
    pdf_h=210  #HEIGHT OF RECTANGLE

    s_x=u_l_x+left_logo_w-27#+20
    s_y=u_l_y+30+3

    width_details=pdf_w-2*u_l_x-2*left_logo_w-2*20
    height_details=15

    pdf.rectangle(s_x,s_y,width_details,height_details) 

    #WRITING THE DETAILS INSIDE THE BOX

    #ROLL_NUMBER
    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2,s_y)
    pdf.cell(10, 9, 'Roll No:', 0, 1, 'C')


    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+14.5,s_y+3)
    pdf.cell(15, 3, str(roll), 1, 1, 'L')


    #NAME

    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+43,s_y)
    pdf.cell(10, 9, 'Name:', 0, 1, 'C')


    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+10+45,s_y+3)
    pdf.cell(40, 3, str(name), 1, 1, 'C')


    #YEAR

    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+43+60,s_y)
    pdf.cell(10, 9, 'Year of Admission:', 0, 1, 'C')


    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+10+43+65,s_y+3)
    pdf.cell(15, 3, '20'+str(y), 1, 1, 'C')


    #PROGRAMME

    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+10.5+6,s_y+5)
    pdf.cell(10, 9, 'Programme: Bachelor of Technology', 0, 1, 'C')

    #COURSE

    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+2+52+10,s_y+5)
    pdf.cell(10, 9, 'Course: '+str(dis), 0, 1, 'C')

    
#CREDITS BLOCK

def credits_block_mtech(pdf,s_x,s_y,c_c,spi,cpi):
    s_x= s_x
    s_y= s_y#+68+42

    width=60
    height=5

    pdf.rectangle(s_x,s_y,width,height) 

    #CREDITS TAKEN
    pdf.set_font('Arial','B',6)
    pdf.set_xy(s_x+4,s_y-1.5)
    pdf.cell(10, 9, 'Credits Taken: '+str(c_c), 0, 1, 'C')

    #CREDITS CLEARED
    pdf.set_xy(s_x+24,s_y-1.5)
    pdf.cell(10, 9, 'Credits Cleared: '+str(c_c), 0, 1, 'C')

    #SPI
    pdf.set_xy(s_x+40,s_y-1.5)
    pdf.cell(10, 9, 'SPI:'+str(spi), 0, 1, 'C')

    #CPI
    pdf.set_xy(s_x+50,s_y-1.5)
    pdf.cell(10, 9, 'CPI:'+str(cpi), 0, 1, 'C')
    

def bottom_mtech(pdf):
    #BOTTOM PART
    pdf_w=210  #WIDTH OF RECTANGLE
    pdf_h=297  #HEIGHT OF RECTANGLE

    pdf.lines(10,215,210,215)

    #DATE OF ISSUE
    pdf.set_font('Arial','B',8)
    pdf.set_xy(15,245)
    pdf.cell(10, 9, 'Date of Issue:', 0, 1, 'L')

    #IIT PATNA STAMP
    pdf.stamp(90,240,27,32)

    #REGISTRAR
    pdf.sign(160,235,36,36)

    





        
        
        
        
                
 
    
    

