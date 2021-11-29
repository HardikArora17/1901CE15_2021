import streamlit as st

import os
import csv
import pandas as pd
from tqdm import tqdm
from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdf_components import PDF_MINER
from mtech_functions import top_mtech,credits_block_mtech,bottom_mtech
from btech_functions import top_btech,credits_block_btech,bottom_btech
from  main import generate_transcripts
import shutil
from zipfile import ZipFile

st.title('Transcript Generator')
st.header("Using python and pypdf")

g = st.file_uploader("Upload the grades.csv file",type=['csv'])

reader_1=pd.DataFrame()
reader_2=pd.DataFrame()
reader_3=pd.DataFrame()

if(g is not None):
    reader_3=pd.read_csv(g)
    st.write(reader_3.head())
    
else:
    st.warning("you need to upload a csv file")
    
    
n = st.file_uploader("Upload the names-roll.csv file",type=['csv'])

if(n is not None):
    reader_1=pd.read_csv(n)
    st.write(reader_1.head())
    
else:
    st.warning("you need to upload a csv file")
    
       
s = st.file_uploader("Upload the subjects_master.csv file",type=['csv'])

if(s is not None):
    reader_2=pd.read_csv(s)
    st.write(reader_2.head())
    
else:
    st.warning("you need to upload a csv file")
    
st.write('')    
user_input = st.text_input("Enter the range of roll numbers for which you want to generate transcript")

if(len(user_input)>1):
    r1=user_input.split('-')[0]
    r2=user_input.split('-')[1]
    
    initial =r1[:-2]
    roll_list=[]
    for i in range(int(r1[-2:]),int(r2[-2:])+1):
        if(i<10):
            roll_list.append(initial+"0"+str(i))
        else:
            roll_list.append(initial+str(i))
        
    st.write("Range entered succesfully")
    
if st.button('Generate Transcripts'):
    shutil.rmtree('transcriptsIITP_12/')
    os.mkdir('transcriptsIITP_12/')
    generate_transcripts(roll_list,reader_1,reader_2,reader_3)
    
    zipObj = ZipFile('storing_tables/transcripts.zip', 'w')
    path='transcriptsIITP_12/'
    
    for k in os.listdir(path):
        zipObj.write(path+k)
        
    zipObj.close()
    
# if(st.button('Download')):
#     st.write("Downloading......")
with open('storing_tables/transcripts.zip', 'rb') as f:
    st.download_button('Download Zip', f, file_name='transcripts.zip')
            
    
        
    
    