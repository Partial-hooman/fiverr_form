import streamlit_survey as ss
import streamlit as st

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')










survey = ss.StreamlitSurvey()
pages = survey.pages(1, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
     For x in f_i:
         survey.radio('select from the following',options=x.split(','),index=0,horizontal=True,label_visibility="collapsed")
     
        
            
