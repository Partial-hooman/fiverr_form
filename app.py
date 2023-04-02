import streamlit as st
import streamlit_survey as ss
import pandas as pd

def download(json):
         df = pd.read_json(json)
         df.to_csv('output.csv', encoding='utf-8', index=False)
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
            "select_from_following",
            options=f_i[pages.current].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
            id=str(pages.current)
        )
    
