import streamlit as st
import streamlit_survey as ss
import pandas as pd

def download(json):
         df = pd.read_json(json)
         csv = df.to_csv()
         csv1 = csv.split('\n') 
         csv1.pop(1)
         csv1.pop(2)
         csv1[0].replace(',','')
         csv1[1].replace('value,','')
         st.write(csv1)
         st.download_button(
                             label="Download selection as CSV",
                             data=csv,
                             file_name='output.csv',
                             mime='text/csv',
                            )
         
    

#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: download(survey.to_json()))
with pages:
         survey.radio(
            options=f_i[pages.current].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
            id=str(pages.current)
        )
    
