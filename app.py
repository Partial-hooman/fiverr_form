import streamlit as st
import streamlit_survey as ss
import pandas as pd

def download(json):
         df = pd.read_json(json)
         csv = df.to_csv().encode('utf-8')
         data = str(csv)
         data1 = data.replace('label','')
         data2 = data.replace('value','')
         st.write(data2)
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
    
