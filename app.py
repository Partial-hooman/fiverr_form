import streamlit_survey as ss
import streamlit as st

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')










survey = ss.StreamlitSurvey()
For x in range(len(f_i)):
    survey.radio('select from the following',options=f_i[x].split(','),index=0,horizontal=True,label_visibility="collapsed")
     
        
            
