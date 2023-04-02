import streamlit_survey as ss
import streamlit as st

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')










survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i) - 1, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
     if pages.current == 0:
        st.write("Have you used Streamlit before?")
        for x in f_i:
            #st.write(f_i[0]) 
            survey.radio(
                         "used_st_before",
                          options=x.split(','),
                          index=0,
                          label_visibility="collapsed",
                          horizontal=True,
                          )
