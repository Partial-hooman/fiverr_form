import streamlit_survey as ss
import streamlit as st
import copy

num = 0

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

Selection=['placer']




with st.form('survey',clear_on_submit=True):
     for x in f_i:
          radio = st.radio('select from following',(x.split(',')))
      
     submit = st.form_submit_button('submit')
 
     


                  
    
        
            
