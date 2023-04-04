#import the required libraries 

import streamlit as st
import streamlit_survey as ss
import pandas as pd

#the download function to download the csv output, which first takes output as a json file

def input_selection(json):
         df = pd.read_json(json) 
         csv = df.to_csv() #the json is converted into csv
         csv1 = csv.split('\n') #the CSV is converted to an array to remove the unecessary rows and columns
         #removing unecessary rows and columns 
         csv1.pop(1)
         csv1.pop(2)
         csv2=[csv1[0][1:],csv1[1].replace('value,','')]
         CSV = csv2[1]
         return type(CSV)
         
 



A = ["ALFA ROMEO", "CHEVROLET", "JAGUAR", "MERCEDES-BENZ", "FIAT", "BENTLEY", "LEXUS", "ACURA", "MITSUBISHI", "CHRYSLER"] 
B = ["ASTON MARTIN", "DODGE", "LAMBORGHINI", "NISSAN", "MINI", "BUICK", "MASERATI", "CADILLAC", "ROLLS-ROYCE", "LINCOLN"] 
C = ["AUDI", "FERRARI", "MAZDA", "PAGANI AUTOMOBILI S.P.A.", "SCION", "FORD", "ROUSH", "INFINITI", "TOYOTA", "GMC"]
D = ["BMW", "HONDA", "MCLAREN", "PORSCHE", "SUBARU", "HYUNDAI", "VOLKSWAGEN", "KIA", "VOLVO", "RAM"]

S = 0
G = 0
O = 0
T = 0


Def calculate_and_plot_user_preference(input):
    if input[0] in B:
       S += 1
    elif input[0] in D:
       G += 1
    elif input[0] in A:
       O += 1
    elif input[0] in C:
       T += 1
     
    if input[1] in A:
       S += 1
    elif input[1] in C:
       G += 1
    elif input[1] in D:
       O += 1
    elif input[1] in B:
       T += 1
    
    if input[2] in C:
       S += 1
    elif input[2] in B:
       G += 1
    elif input[2] in A:
       O += 1
    elif input[2] in D:
       T += 1

    if input[3] in A:
       S += 1
    elif input[3] in D:
       G += 1
    elif input[3] in C:
       O += 1 
    elif input[3] in B:
       T += 1
    
   if input[4] in D:
       S += 1
   elif input[4] in B:
       G += 1 
   elif input[4] in C:
       O += 1
   elif input[4] in A:
       T += 1

   if input[5] in B:
       S += 1
   elif input[5] in A:
       G += 1 
   elif input[5] in D:
       O += 1
   elif input[5] in C:
       T += 1

   if input[6] in C:
       S += 1
   elif input[6] in D:
       G += 1 
   elif input[6] in B:
       O += 1
   elif input[6] in A:
       T += 1
   
   if input[7] in B:
       S += 1
   elif input[7] in A:
       G += 1 
   elif input[7] in D:
       O += 1
   elif input[7] in C:
       T += 1

   if input[8] in D:
       S += 1
   elif input[8] in A:
       G += 1 
   elif input[8] in C:
       O += 1
   elif input[8] in B:
       T += 1
 
   if input[9] in C:
       S += 1
   elif input[9] in B:
       G += 1 
   elif input[9] in D:
       O += 1
   elif input[9] in A:
       T += 1
   
   prefs = {"S":S,"G":G,"O":O,"T":T}
   pref = [S,G,O,T]
   user_pref = list(filter(lambda x: prefs[x] == max(pref), prefs))[0]
   st.write("User preference is " + user_pref)
   P_df = pd.DataFrame(dict(r=[S,G,O,T],theta=["S","G","O","T"]))
   fig = px.line_polar(P_df, r='r', theta='theta', line_close=True)
   st.write(fig)



    
# the manufacturer CSV file is imported

f = open('manufacturers.csv', 'r')

# it's then converted to an array to generate the survey 

f_i = (f.read()).split('\n')

#generating the survey


survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(f_i), on_submit=lambda: st.write(input_selection(survey.to_json()))) # the survey is first converted to json after which it is given to the download function to download the CSV output

# generating the survey radios

with pages:
         radio = survey.radio(
                   options=f_i[pages.current].split(','),
                   index=0,
                   label_visibility="collapsed",
                   horizontal=True,
                   id=str(pages.current)
                   )
         
        
                     
       
