import streamlit as st
import streamlit_survey as ss

num = 0
#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: st.json(survey.to_json()))
with pages:
    if pages.current == 0:
        used_0 = survey.radio(
            "select_from_following",
            options=f_i[pages.current].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 1:
        used_1 = survey.radio(
            "select_from_following",
           options=f_i[2].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 2:
        used_2 = survey.radio(
            "select_from_following",
            options=f_i[2].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 3:
        used_3 = survey.radio(
            "select_from_following",
            options=f_i[3].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
         
    elif pages.current == 4:
        used_4 = survey.radio(
            "select_from_following",
            options=f_i[4].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
         
    elif pages.current == 5:
        used_5 = survey.radio(
            "select_from_following",
            options=f_i[5].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 6:
        used_6 = survey.radio(
            "select_from_following",
            options=f_i[6].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 7:
        used_7 = survey.radio(
            "select_from_following",
            options=f_i[7].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 8:
        used_8 = survey.radio(
            "select_from_following",
            options=f_i[8].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
    elif pages.current == 9:
        used_9 = survey.radio(
            "select_from_following",
            options=f_i[9].split(','),
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
 
     


                  
    
        
            
