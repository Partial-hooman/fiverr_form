import streamlit as st
import streamlit_survey as ss
import pandas as pd


#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: st.write((pd.read_json(survey.to_json())).to_csv()))
with pages:
         survey.radio(
            "select_from_following",
            options=f_i[pages.current].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
            id=str(pages.current)
        )
    
