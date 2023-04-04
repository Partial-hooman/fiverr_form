#import the required libraries 

import streamlit as st
import streamlit_survey as ss
import pandas as pd

#the download function to download the csv output, which first takes output as a json file

#def download(json):
         df = pd.read_json(json) 
         csv = df.to_csv() #the json is converted into csv
         csv1 = csv.split('\n') #the CSV is converted to an array to remove the unecessary rows and columns
         removing unecessary rows and columns 
         csv1.pop(1)
         csv1.pop(2)
         csv2=[csv1[0][1:],csv1[1].replace('value,','')]
         CSV = csv2[1]
         return CSV
         




A = ["ALFA ROMEO", "CHEVROLET", "JAGUAR", "MERCEDES-BENZ", "FIAT", "BENTLEY", "LEXUS", "ACURA", "MITSUBISHI", "CHRYSLER"] 
B = ["ASTON MARTIN", "DODGE", "LAMBORGHINI", "NISSAN", "MINI", "BUICK", "MASERATI", "CADILLAC", "ROLLS-ROYCE", "LINCOLN"] 
C = ["AUDI", "FERRARI", "MAZDA", "PAGANI AUTOMOBILI S.P.A.", "SCION", "FORD", "ROUSH", "INFINITI", "TOYOTA", "GMC"]
D = ["BMW", "HONDA", "MCLAREN", "PORSCHE", "SUBARU", "HYUNDAI", "VOLKSWAGEN", "KIA", "VOLVO", "RAM"]

S,G,O,T = 0





    
# the manufacturer CSV file is imported

f = open('manufacturers.csv', 'r')

# it's then converted to an array to generate the survey 

f_i = (f.read()).split('\n')

#generating the survey


survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: download(survey.to_json())) # the survey is first converted to json after which it is given to the download function to download the CSV output

# generating the survey radios

with pages:
         radio = survey.radio(
                   options=f_i[pages.current].split(','),
                   index=0,
                   label_visibility="collapsed",
                   horizontal=True,
                   id=str(pages.current)
                   )
         
        
                     
       
