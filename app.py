import streamlit_survey as ss
import streamlit as st
import copy

num = 0

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

Selection=['placer']




with st.form(clear_on_submit=True):
     radio = st.radio('select from following',f_i[num])
 
     


                  
    
        
            
