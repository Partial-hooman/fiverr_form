import streamlit_survey as ss
import streamlit as st
import copy


f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

Selection=['placer']








#survey = ss.StreamlitSurvey()
#pages = survey.pages(len(f_i), on_submit=lambda: St.write(Selection) #st.success("Your responses have been recorded. Thank you!"))

#with pages:
     #radio = survey.radio('select from the following',options=f_i[pages.current].split(','),index=0,horizontal=True,label_visibility="collapsed")
     #if pages.next:
        #Selection.append(radio)
     #elif pages.previous:
        #Selection.pop()
 

survey = ss.StreamlitSurvey()
pages = survey.pages(len(f_i), on_submit=lambda:  st.success("Your responses have been recorded. Thank you!"))

with pages:
     radio = survey.radio('select from the following',options=f_i[pages.current].split(','),index=0,horizontal=True,label_visibility="collapsed")
     if pages.previous:
        st.write(Selection)
     


                  
    
        
            
