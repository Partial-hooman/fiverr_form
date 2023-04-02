import streamlit as st
import streamlit_survey as ss

num = 0
#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: st.json(survey.to_json()))
with pages:
     globals()["radio"+str(pages.current)] = survey.radio("select from following", options=f_i[pages.current].split(','),index=0,label_visibility="collapsed", horizontal=True)
    #if pages.current == 0:
        #st.write("Have you used Streamlit before?")
        #used_0 = survey.radio(
        #    "select_from_following",
        #    options=f_i[pages.current].split(','),
        #    index=0,
        #    label_visibility="collapsed",
        #    horizontal=True,
        #)
    #elif pages.current == 1:
        #st.write("Have you used Streamlit before?")
        #used_1 = survey.radio(
        #    "select_from_following",
        #   options=f_i[pages.current].split(','),
        #    index=0,
        #    label_visibility="collapsed",
        #    horizontal=True,
        #)
    #elif pages.current == 2:
        #st.write("Have you used Streamlit before?")
        #used_2 = survey.radio(
        #    "select_from_following",
        #    options=f_i[pages.current].split(','),
        #    index=0,
        #    label_visibility="collapsed",
        #    horizontal=True,
        #)
    #elif pages.current == 3:
        # pass
    #elif pages.current == 4:
        # pass
    #elif pages.current == 5:
        # pass
    #elif pages.current == 6:
        # pass
    #elif pages.current == 7:
        # pass
    #elif pages.current == 8:
        # pass
    #elif pages.current == 9:
        # pass
 
     


                  
    
        
            
