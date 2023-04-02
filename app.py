import streamlit_survey as ss
import streamlit as st
import copy

num = 0

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

Selection=['placer']




with st.form('select from following', clear_on_submit=True):
     radio = st.radio(f_i[num])
 
     


                  
    
        
            
