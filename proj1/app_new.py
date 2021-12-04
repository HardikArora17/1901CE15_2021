import streamlit as st

import os
import csv
import pandas as pd
from stqdm import stqdm
import numpy as np
import shutil
import base64
import streamlit.report_thread as ReportThread
from streamlit.server.server import Server

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, NamedStyle
from openpyxl.worksheet.table import Table, TableStyleInfo

from utils import get_styles
bold_, thin, heading_, correct_style, wrong_style, neut_style, true_style = get_styles()
from helpers import insert_info, add_borders, add_headings, fill_table_1, gen_roll_wise, get_net_scores_and_absentees, gen_concise, get_concise, send_mails

st.title('Marksheet Generator')
st.header("Using python, smtplib and openpyxl")

master_roll=pd.DataFrame()
responses=pd.DataFrame()

master_roll_uploaded = False
responses_uploaded = False
right_marks_entered = False
wrong_marks_entered = False
marksheets_generated = False
concise_generated = False


if('var' not in st.session_state):
    st.session_state.var=0
    
        
m_r = st.file_uploader("Upload the master_roll.csv file",type=['csv'])
if(m_r is not None):
    master_roll=pd.read_csv(m_r)
    if master_roll.shape[1]!=2:
        st.warning("Please upload a valid master_roll.csv file!")
    else:
        st.write(master_roll.head())
        master_roll_uploaded = True
else:
    st.warning("Please upload a CSV file.")

r = st.file_uploader("Upload the responses.csv file",type=['csv'])
if(r is not None):
    responses=pd.read_csv(r)
    try:
        if ('ANSWER' not in responses['Roll Number'].to_list()) or ('ANSWER' not in master_roll['roll'].to_list()):
            st.warning('no roll number with ANSWER is present, Cannot Process!')
        
        else:
            responses_uploaded = True
            st.write(responses.head())
            if master_roll_uploaded and responses_uploaded:
                st.write('All the files uploaded succesfully!')

            st.write('')    
            user_input1 = st.number_input("Enter marks for correct answer (For eg: 5)",0.000)
            
            right_marks = user_input1
            right_marks_entered = True
            st.write('')    
                
            user_input2 = st.number_input("Enter marks for wrong answer (For eg: -1)",max_value=0.000)
            wrong_marks = user_input2
            wrong_marks_entered = True
            neut_marks = 0
            
            if right_marks_entered and wrong_marks_entered:
                st.write("Marking scheme entered succesfully!")
        
                if st.button('Generate Marksheets'):
                    
                    # Check if the files and marking scheme have been uploaded.
                    if not (master_roll_uploaded and responses_uploaded):
                        st.warning('Please upload all the necessary files!')
                    if not (right_marks_entered and wrong_marks_entered):
                        st.warning('Please enter the marking scheme.')

                    # Clear the files created during the last run, and make new directories.
                    if os.path.exists('marksheet'):
                        shutil.rmtree('marksheet')
                        
                    os.mkdir('marksheet')

                    # Fenerate roll number wise marksheets
                    responses, net_scores, absent_rows = gen_roll_wise(responses, master_roll, right_marks, wrong_marks, neut_marks)
                    st.write('Roll Number wise Marksheets Generated Successfully!')
                    marksheets_generated = True
                    st.session_state.var=1
                    
                if st.button('Generate Concise Marksheet'):

                    # Check if the files and marking scheme have been uploaded ot not.
                    if not (master_roll_uploaded and responses_uploaded):
                        st.warning('Please upload all the necessary files!')
                    elif not (right_marks_entered and wrong_marks_entered):
                        st.warning('Please enter the marking scheme.')

                    else:
                        #st.write('rolln wise not generated')
                        responses, net_scores, absent_rows = get_net_scores_and_absentees(responses, master_roll, right_marks, wrong_marks, neut_marks)
                        responses = gen_concise(responses, net_scores, absent_rows)
                        concise_generated = True
                        st.write('Concise Marksheet Generated Succesfully!')

                        if concise_generated:
                            st.download_button(label='📥 Click to download concise_marksheet.csv',
                                                        data=responses.to_csv(),
                                                        file_name= 'concise_marksheet.csv',
                                                        mime='text/csv')

                if st.button('Send all marksheets via mail'):

                    if st.session_state.var==0:
                        st.warning('Please generate roll number wise marksheets first!')
                    elif st.session_state.var==1:
                        send_mails(responses,0)
                        st.write('All emails sent Succesfully!')
                        
            else:
                st.warning('Please enter a valid marking scheme')
            
        # else:
        #     st.warning('Please enter a valid marking scheme')   
                 
    except KeyError:
        st.warning('Please upload a master_roll.csv file')

else:
    st.warning("Please upload a CSV file")
        