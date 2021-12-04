import streamlit as st
import cv2

import os
import pandas as pd
from tqdm import tqdm
from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
from pdf_components import PDF_MINER
from mtech_functions import top_mtech,credits_block_mtech,bottom_mtech
from btech_functions import top_btech,credits_block_btech,bottom_btech
from  main import generate_transcripts
import shutil
from zipfile import ZipFile
import base64

LOGO_IMAGE = "title_image.png"
st.markdown("<h1 style='text-align: center; color: black;'>Transcript Generator</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 500px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)
#st.title('Transcript Generator')

# st.image('title_image.png')

#st.header("Using python and pypdf")
st.markdown("<h2 style='text-align: center; color: black;'>Using python and pypdf</h2>", unsafe_allow_html=True)

flag_sign=0
flag_stamp=0
col1, col2 = st.columns(2)

with col1:
    #input1 = st.number_input('Source Lattitude Coordinates')
    g = st.file_uploader("Upload the grades.csv file",type=['csv'])
    st.write(" ")
    n = st.file_uploader("Upload the names-roll.csv file",type=['csv'])
    st.write(" ")
    s = st.file_uploader("Upload the subjects_master.csv file",type=['csv'])

with col2:
    uploaded_file = st.file_uploader("Choose a image file for stamp", type=["jpg","png"])
    st.write(" ")
    
    if uploaded_file is not None:
        flag_stamp=1
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image, channels="BGR",width=100, use_column_width=100)
        cv2.imwrite("stamp_uploaded.png",opencv_image)

    uploaded_file_1 = st.file_uploader("Upload Sign", type=["jpg","png","jpeg"])
    
    if uploaded_file_1 is not None:
        flag_sign=1
        file_bytes = np.asarray(bytearray(uploaded_file_1.read()), dtype=np.uint8)
        opencv_image_1 = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image_1, channels="BGR",width=100, use_column_width=100)
        cv2.imwrite("sign_uploaded.png",opencv_image_1)




    # input2 = st.number_input('Source Longitude Coordinates')
    
#g = st.file_uploader("Upload the grades.csv file",type=['csv'])

reader_1=pd.DataFrame()
reader_2=pd.DataFrame()
reader_3=pd.DataFrame()

if(g is not None):
    reader_3=pd.read_csv(g,index_col=False)
    #st.write(reader_3.head())
    

#n = st.file_uploader("Upload the names-roll.csv file",type=['csv'])

if(n is not None):
    reader_1=pd.read_csv(n,index_col=False)
    #st.write(reader_1.head())
    

#s = st.file_uploader("Upload the subjects_master.csv file",type=['csv'])

if(s is not None):
    reader_2=pd.read_csv(s,index_col=False)
    #st.write(reader_2.head())
    

#uploaded_file = st.file_uploader("Choose a image file for stamp", type=["jpg","png"])

#uploaded_file_1 = st.file_uploader("Upload Sign", type=["jpg","png","jpeg"])
    
    
st.write('')    
user_input = st.text_input("Enter the range of roll numbers for which you want to generate transcript. For example 0401CS07-0401CS10")
range_correct=0
if(len(user_input)>1):
    
    r1=user_input.split('-')[0].upper()
    r2=user_input.split('-')[1].upper()
    
    if(r1[0:2]!=r2[0:2]):
        st.warning("The range should be corresponding to a single year")
    
    elif(r1[2:4]!=r2[2:4]):
        st.warning("The range should be corresponding to same programme")
    
    elif(r1[4:6]!=r2[4:6]):
        st.warning("The range should be corresponding to a single branch")
    
    elif(len(r1)<8 or len(r2)<8):
        st.warning("The range is not correct")
        
    else:
        initial =r1[:-2]
        roll_list=[]
        for i in range(int(r1[-2:]),int(r2[-2:])+1):
            if(i<10):
                roll_list.append(initial+"0"+str(i))
            else:
                roll_list.append(initial+str(i))
            
        range_correct=1
        st.write("Range entered succesfully")
        
flag_final=0
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Generate Transcripts Range wise')
    generate_all_button = st.button("Generate All")

if center_button:
    
    if(not (g and s and n)):
        st.warning("Enter all the required files")
    elif(range_correct!=1):
        st.warning("Enter range correctly")
        
    else:    
        if os.path.exists('transcriptsIITP/'):
            shutil.rmtree('transcriptsIITP/')
                    
        os.mkdir('transcriptsIITP/')
        generate_transcripts(roll_list,reader_1,reader_2,reader_3,flag_stamp,flag_sign)
        
        zipObj = ZipFile('storing_tables/transcripts.zip', 'w')
        path='transcriptsIITP/'
        
        for k in os.listdir(path):
            zipObj.write(path+k)
        
        flag_final=1
        zipObj.close()
        
if generate_all_button:
    
    if(not (g and s and n)):
        st.warning("Enter all the required files")
        
    else:    
        if os.path.exists('transcriptsIITP/'):
            shutil.rmtree('transcriptsIITP/')
                    
        os.mkdir('transcriptsIITP/')
        generate_transcripts([],reader_1,reader_2,reader_3,flag_stamp,flag_sign,1)
        
        zipObj = ZipFile('storing_tables/transcripts.zip', 'w')
        path='transcriptsIITP/'
        
        for k in os.listdir(path):
            zipObj.write(path+k)
        
        flag_final=1
        zipObj.close()

        
        
if(flag_final==1):
    with open('storing_tables/transcripts.zip', 'rb') as f:
        if st.download_button('Download Zip', f, file_name='transcripts.zip'):
            hellop=1
        
    

        
    
    