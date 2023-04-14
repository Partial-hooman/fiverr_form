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
         

def input_ratings(json,INP):
    A = (INP.iloc[:,0]).tolist()
    B = (INP.iloc[:,1]).tolist()
    C = (INP.iloc[:,2]).tolist()
    D = (INP.iloc[:,3]).tolist()
    a = []
    b = []
    c = []
    d = []
    a_ratings = []
    b_ratings = []
    c_ratings = []
    d_ratings = []
    DF = pd.read_json(json)
    #DF = DF.to_csv()
    DF = DF.drop(['label'])
    #st.dataframe(DF)
    columns = list(DF.columns)
    for x in columns:
        if "A" in x:
           a.append(x)
        elif "B" in x:
           b.append(x)
        elif "C" in x:
           c.append(x)
        elif "D" in x:
           d.append(x)
    #st.write(a,b,c,d)
    for x in a:
        a_ratings.append(DF[x].tolist()[0])
    for x in b:
        b_ratings.append(DF[x].tolist()[0])
    for x in c:
        c_ratings.append(DF[x].tolist()[0])
    for x in d:
        d_ratings.append(DF[x].tolist()[0])
    Data = {"Ratings":a_ratings,INP.columns[0]:A,"Ratings":b_ratings,INP.columns[1]:B,"ratings":c_ratings,INP.columns[2]:C,"ratings":d_ratings,INP.columns[3]:D}
    #st.write(a_ratings,b_ratings,c_ratings,d_ratings)
    st.write('Ratings:')    
    st.dataframe(Data)
    ratings = [sum(a_ratings),sum(b_ratings),sum(c_ratings),sum(d_ratings)]
    Frame = pd.DataFrame(Data)
    return ratings, Frame 


 
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Export results</a>'



S_count = 0
G_count = 0
O_count = 0
T_count = 0













# function to calculate user pref and plot graph, takes user selection as input 

def calculate_and_plot_user_preference(Input,Lookup,input):#,S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D):
   # count calculation 
   #inp = []
   #for x in input:
         #if x in A:
            #inp.append("A")
         #if x in B:
            #inp.append("B")
         #if x in C:
            #inp.append("C")
         #if x in D:
            #inp.append("D")
                       
  
   ratings, Frame = input
   #inp2 = {(list(Input.columns))[0]:A,(list(Input.columns))[1]:B,(list(Input.columns))[2]:C,(list(Input.columns))[3]:D}
   #st.write('['+",".join(inp)+']')
   #for i in range(len(input)):
         #if input[i].strip() in inp2.get(S[i]):
            #S_count += 1
            #st.write("S",S[i])
         #elif input[i].strip() in inp2.get(G[i]):
            #G_count += 1
            #st.write("G",G[i])
         #elif input[i].strip() in inp2.get(O[i]):
            #O_count += 1
            #st.write("O",O[i])
         #elif input[i].strip() in inp2.get(T[i]):
            #T_count += 1
            #st.write("T",T[i])
         

   prefs = {(list(Input.columns))[0]:ratings[0],(list(Input.columns))[1]:ratings[1],(list(Input.columns))[2]:ratings[2],(list(Input.columns))[3]:ratings[3]}
   pref = ratings 
   pref2 = [*set(pref)]
   pref2.sort(reverse = True)
   #st.write('USER RESPONSE: ' + "[" + ','.join(input) + ']')
   st.header("User preference is:")
   for x in range(len(pref2)):
       my_srs = pd.Series(prefs).astype(int)
       user_pref = "".join((my_srs.index[my_srs == pref2[x]].tolist()))
       st.subheader(str(x+1)+"."+user_pref)
   #user_pref = list(filter(lambda x: prefs[x] == max(pref), prefs))[0]
   #st.write('USER RESPONSE: ' + "[" + ','.join(input) + ']')
   #my_srs = pd.Series(prefs).astype(int)
   #user_pref = "".join((my_srs.index[my_srs == max(pref)].tolist()))
   #st.header("User preference is " + user_pref)
   st.write(prefs)
   #plotting the graph 
   P_df = pd.DataFrame(dict(r=ratings,theta=[list(Input.columns)[0],list(Input.columns)[1],list(Input.columns)[2],list(Input.columns)[3]]))
   fig = px.line_polar(P_df, r='r', theta='theta', line_close=True,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig)
   fig2 = px.pie(values=pref, names=[list(Input.columns)[0],list(Input.columns)[1],list(Input.columns)[2],list(Input.columns)[3]], hole=.5,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig2)
   #buffer = io.BytesIO()
   #buffer2 = io.BytesIO()
   temp = tempfile.NamedTemporaryFile(suffix='.png')
   temp2 = tempfile.NamedTemporaryFile(suffix='.png')
   # Save the figure as a pdf to the buffer
   fig.write_image(file=temp, format="png")
   fig2.write_image(file=temp2, format="png")
   Df_fig = df2img.plot_dataframe(
         Input,
         title=dict(
              font_color="darkred",
              font_family="Times New Roman",
              font_size=16,
              text="Input data:",
              ),
         tbl_header=dict(
              align="right",
              fill_color="blue",
              font_color="white",
              font_size=10,
              line_color="darkslategray",
              ),
         tbl_cells=dict(
         align="right",
         line_color="darkslategray",
              ),
         row_fill_color=("#ffffff", "#d7d8d6"),
         fig_size=(560, 1440)
        )
   Df_fig2 = df2img.plot_dataframe(
         Lookup,
         title=dict(
              font_color="darkred",
              font_family="Times New Roman",
              font_size=16,
              text="Lookup data:",
              ),
         tbl_header=dict(
              align="right",
              fill_color="blue",
              font_color="white",
              font_size=10,
              line_color="darkslategray",
              ),
         tbl_cells=dict(
         align="right",
         line_color="darkslategray",
              ),
         row_fill_color=("#ffffff", "#d7d8d6"),
         fig_size=(560, 1440)
        )
   Df_fig3 = df2img.plot_dataframe(
         Frame,
         title=dict(
              font_color="darkred",
              font_family="Times New Roman",
              font_size=16,
              text="Ratings:",
              ),
         tbl_header=dict(
              align="right",
              fill_color="blue",
              font_color="white",
              font_size=10,
              line_color="darkslategray",
              ),
         tbl_cells=dict(
         align="right",
         line_color="darkslategray",
              ),
         row_fill_color=("#ffffff", "#d7d8d6"),
         fig_size=(560, 1440)
        )
   df_temp = tempfile.NamedTemporaryFile(suffix='.png')
   df_temp2 = tempfile.NamedTemporaryFile(suffix='.png')
   df_temp3 = tempfile.NamedTemporaryFile(suffix='.png')
   df2img.save_dataframe(fig=Df_fig, filename=df_temp.name)
   df2img.save_dataframe(fig=Df_fig2, filename=df_temp2.name)
   df2img.save_dataframe(fig=Df_fig3, filename=df_temp3.name)
   pdf = FPDF()
   pdf.add_page()
   pdf.image(str(df_temp.name))
   pdf.image(str(df_temp2.name))
   pdf.image(str(df_temp3.name))
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
      A = (input.iloc[:,0]).tolist()
      B = (input.iloc[:,1]).tolist()
      C = (input.iloc[:,2]).tolist()
      D = (input.iloc[:,3]).tolist()
      lookup = pd.read_csv(Lookup,sep=r'\s*,\s*', engine='python')
      S = (lookup.iloc[:,0]).tolist()
      G = (lookup.iloc[:,1]).tolist()
      O = (lookup.iloc[:,2]).tolist()
      T = (lookup.iloc[:,3]).tolist()
      st.header("uploaded data frames")
      st.write("Main Data:")
      st.dataframe(input)
      st.write("lookup table:")
      st.dataframe(lookup)
      # the manufacturer CSV file is imported

      #f = open('manufacturers.csv', 'r')

      # it's then converted to an array to generate the survey 

      #f_i = (f.read()).split('\n')

      #generating the survey
      survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
      pages = survey.pages(len(input.index), on_submit=lambda: calculate_and_plot_user_preference(input,lookup,input_ratings(survey.to_json(),input)))#,S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D)) # the survey is first converted to json after which it is given to the download function to download the CSV output

      # generating the survey radios

      with pages:
               st.subheader((input.iloc[pages.current].tolist())[0])
               Slb0 = survey.selectbox("rating:", options=[1,2,3,4],id=f"A_{pages.current}")
               st.subheader((input.iloc[pages.current].tolist())[1])
               Slb1 = survey.selectbox("rating:", options=[1,2,3,4],id=f"B_{pages.current}")
               st.subheader((input.iloc[pages.current].tolist())[2])
               Slb2 = survey.selectbox("rating:", options=[1,2,3,4],id=f"C_{pages.current}")
               st.subheader((input.iloc[pages.current].tolist())[3])
               Slb3 = survey.selectbox("rating:", options=[1,2,3,4],id=f"D_{pages.current}")
               #radio = survey.radio(label="label",
                         #options=input.iloc[pages.current].tolist(),
                         #index=0,
                         #label_visibility="collapsed",
                         #horizontal=True,
                         #id=str(pages.current)
                         #)                   
                
        
                     
       
