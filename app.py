import streamlit as st


num = 0
#radio=[]

f = open('manufacturers.csv', 'r')

f_i = (f.read()).split('\n')

form = st.form('survey',clear_on_submit=True):



with form:
     st.radio('select from following',(f_i[num].split(',')))
      
     submit = st.form_submit_button('submit')
     if submit:
          st.write(','.join(radio))
          
 
     


                  
    
        
            
