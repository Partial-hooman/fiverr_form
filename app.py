import streamlit_survey as ss
import streamlit as st


survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(2, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
     if pages.current == 0:
        st.write("Have you used Streamlit before?")
        used_before = survey.radio(
                                    "used_st_before",
                                     options=["CHEVROLET","DODGE","FERRARI","HONDA"],
                                     index=0,
                                     label_visibility="collapsed",
                                     horizontal=True,
                                     )
