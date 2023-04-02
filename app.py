import streamlit_survey as ss
import streamlit as st

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')










survey = ss.StreamlitSurvey()
pages = survey.pages(1, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
     For x in range(len(f_i)-1):
         survey.radio('select from the following',options=f_i[x].split(','),index=0,horizontal=True,label_visibility="collapsed")
     
        
            
