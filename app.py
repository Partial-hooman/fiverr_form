#import the required libraries 

import streamlit as st
import streamlit_survey as ss
import pandas as pd

#the download function to download the csv output, which first takes output as a json file

def download(json):
         df = pd.read_json(json) 
         csv = df.to_csv() #the json is converted into csv
         csv1 = csv.split('\n') #the CSV is converted to an array to remove the unecessary rows and columns
         # removing unecessary rows and columns 
         csv1.pop(1)
         csv1.pop(2)
         csv2=[csv1[0][1:],csv1[1].replace('value,','')]
         CSV='\n'.join(csv2)
         #st.write(CSV)
         # the CSV output is then exported and then downloaded through streamlit's download button widget 
         st.download_button(
                             label="Download selection as CSV",
                             data=CSV,
                             file_name='output.csv',
                             mime='text/csv',
                            )
         
    
# the manufacturer CSV file is imported

f = open('manufacturers.csv', 'r')

# it's then converted to an array to generate the survey 

f_i = (f.read()).split('\n')

#generating the survey


survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: download(survey.to_json())) # the survey is first converted to json after which it is given to the download function to download the CSV output
# generating the survey radios

with pages:
         survey.radio(
            options=f_i[pages.current].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
            id=str(pages.current)
        )
    
