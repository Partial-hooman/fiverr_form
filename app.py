#import the required libraries 
import df2img
import base64
import tempfile 
from fpdf import FPDF
import plotly.express as px
import streamlit as st
import streamlit_survey as ss
import pandas as pd
#converts user input into array for further calculations
#import io
def input_selection(json):
         df = pd.read_json(json) 
         csv = df.to_csv() #the json is converted into csv
         csv1 = csv.split('\n') #the CSV is converted to an array to remove the unecessary rows and columns
         #removing unecessary rows and columns 
         csv1.pop(1)
         csv1.pop(2)
         csv2=[csv1[0][1:],csv1[1].replace('value,','')]
         CSV = csv2[1].split(',')
         return CSV
         
 
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Export results</a>'



S_count = 0
G_count = 0
O_count = 0
T_count = 0













# function to calculate user pref and plot graph, takes user selection as input 

def calculate_and_plot_user_preference(input,S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D):
   # count calculation 
   inp = []
   for x in input:
         if x in A:
            inp.append("A")
         elif x in B:
            inp.append("B")
         elif x in C:
            inp.append("C")
         elif x in D:
            inp.append("D")
                       
   
   for i in range(len(inp)):
         if inp[i] == S[i]:
            S_count += 1
         if inp[i] == G[i]:
            G_count += 1
         if inp[i] == O[i]:
            O_count += 1
         if inp[i] == T[i]:
            T_count += 1
         

   prefs = {"S":S_count,"G":G_count,"O":O_count,"T":T_count}
   pref = [S_count,G_count,O_count,T_count]
   #user_pref = list(filter(lambda x: prefs[x] == max(pref), prefs))[0]
   st.write('USER RESPONSE: ' + "[" + ','.join(input) + ']')
   my_srs = pd.Series(prefs).astype(int)
   user_pref = "".join((my_srs.index[my_srs == max(pref)].tolist()))
   st.header("User preference is " + user_pref)
   st.write(prefs)
   #plotting the graph 
   P_df = pd.DataFrame(dict(r=[S_count,G_count,O_count,T_count],theta=["S","G","O","T"]))
   fig = px.line_polar(P_df, r='r', theta='theta', line_close=True,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig)
   fig2 = px.pie(values=pref, names=["S","G","O","T"], hole=.5,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig2)
   #buffer = io.BytesIO()
   #buffer2 = io.BytesIO()
   temp = tempfile.NamedTemporaryFile(suffix='.png')
   temp2 = tempfile.NamedTemporaryFile(suffix='.png')
   # Save the figure as a pdf to the buffer
   fig.write_image(file=temp, format="png")
   fig2.write_image(file=temp2, format="png")
   pdf = FPDF()
   pdf.add_page()
   pdf.set_font('Arial', 'B', 16)
   pdf.image(str(temp.name),x=-25)
   pdf.cell(40, 10, 'User preference (radar chart)',align = 'L')
   pdf.add_page()
   pdf.image(str(temp2.name),x=-50)
   pdf.cell(40, 10, 'User preference (pie chart)',align = 'L')
   # Download the pdf from the buffer
   html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Graphs")
   st.markdown(html, unsafe_allow_html=True)
    

Input = st.file_uploader("upload the input csv", type='csv')
Lookup = st.file_uploader("upload the lookup CSV", type='csv')


if Input is not None:
   if Lookup is not None:
      input = pd.read_csv(Input,sep=r'\s*,\s*',engine='python')
      A = input['A'].tolist()
      B = input['B'].tolist()
      C = input['C'].tolist()
      D = input['D'].tolist()
      lookup = pd.read_csv(Lookup,sep=r'\s*,\s*', engine='python')
      S = lookup['S'].tolist()
      G = lookup['G'].tolist()
      O = lookup['O'].tolist()
      T = lookup['T'].tolist()
      st.header("uploaded data frames")
      st.write("Main Data:")
      st.dataframe(input)
      st.write("lookup table:")
      st.dataframe(lookup)
      # the manufacturer CSV file is imported

      f = open('manufacturers.csv', 'r')

      # it's then converted to an array to generate the survey 

      f_i = (f.read()).split('\n')

      #generating the survey
      survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
      pages = survey.pages(len(f_i), on_submit=lambda: calculate_and_plot_user_preference(input_selection(survey.to_json()),S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D)) # the survey is first converted to json after which it is given to the download function to download the CSV output

      # generating the survey radios

      with pages:
               st.subheader("question " + str(pages.current+1))
               radio = survey.radio(label="label",
                         options=f_i[pages.current].split(','),
                         index=0,
                         label_visibility="collapsed",
                         horizontal=True,
                         id=str(pages.current)
                         )                   
                
        
                     
       
