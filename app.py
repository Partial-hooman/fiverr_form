import streamlit as st
import streamlit_survey as ss

num = 0
#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(2, on_submit=lambda: st.json(survey.json()))
with pages:
    if pages.current == 0:
        st.write("Have you used Streamlit before?")
        used_before = survey.radio(
            "used_st_before",
            options=["NA", "Yes", "No"],
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
        if used_before == "Yes":
            st.write("How often do you use Streamlit?")
            survey.select_slider(
                "st_frequency",
                options=["Every Day", "Every week", "Every Month", "Once a year", "Rarely"],
                label_visibility="collapsed",
            )
        elif used_before == "No":
            st.write("Have you used other dashboarding tools?")
            used_other = survey.radio(
                "used_other",
                options=["NA", "Yes", "No"],
                index=0,
                label_visibility="collapsed",
                horizontal=True,
            )
            if used_other == "Yes":
                st.write("Which tools?")
                survey.multiselect(
                    "other_tools",
                    options=["Dash", "Voila", "Panel", "Bokeh", "Plotly", "Other"],
                    label_visibility="collapsed",
                )
    elif pages.current == 1:
        st.write("How satisfied are you with this survey?")
        survey.select_slider(
            "Overall Satisfaction",
            options=["Very Unsatisfied", "Unsatisfied", "Neutral", "Satisfied", "Very Satisfied"],
            label_visibility="collapsed",
        )
 
     


                  
    
        
            
