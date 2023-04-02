import streamlit_survey as ss
import streamlit as st

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')










survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
     survey.radio(options=f_i[pages.current].split(','),index=0,horizontal=True)
        
        
            
