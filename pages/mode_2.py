#import the required libraries 
import df2img
import base64
import tempfile 
from fpdf import FPDF
import plotly.express as px
import streamlit as st
import streamlit_survey as ss
import pandas as pd

# prepares the ratings for calculations        

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
    DF = DF.drop(['label'])
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
    for x in a:
        a_ratings.append(DF[x].tolist()[0])
    for x in b:
        b_ratings.append(DF[x].tolist()[0])
    for x in c:
        c_ratings.append(DF[x].tolist()[0])
    for x in d:
        d_ratings.append(DF[x].tolist()[0])
    Data = {"Ratings  1":a_ratings,INP.columns[0]:A,"Ratings  2":b_ratings,INP.columns[1]:B,"ratings  3":c_ratings,INP.columns[2]:C,"ratings  4":d_ratings,INP.columns[3]:D}
    st.write('Ratings:')    
    st.dataframe(Data)
    ratings = [sum(a_ratings),sum(b_ratings),sum(c_ratings),sum(d_ratings)]
    Frame = pd.DataFrame(Data)
    return ratings, Frame 


 
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Export results</a>'













# function to calculate user pref and plot graph using method2

def calculate_and_plot_user_preference(Input,Lookup,input):

                       
  
   ratings, Frame = input

   prefs = {(list(Input.columns))[0]:ratings[0],(list(Input.columns))[1]:ratings[1],(list(Input.columns))[2]:ratings[2],(list(Input.columns))[3]:ratings[3]}
   pref = ratings 
   pref2 = [*set(pref)]
   pref2.sort(reverse = True)

   st.header("User preference is:")
   for x in range(len(pref2)):
       my_srs = pd.Series(prefs).astype(int)
       user_pref = "".join((my_srs.index[my_srs == pref2[x]].tolist()))
       st.write(str(x+1)+"."+user_pref)

   st.write(prefs)
   #plotting the graph 
   P_df = pd.DataFrame(dict(r=ratings,theta=[list(Input.columns)[0],list(Input.columns)[1],list(Input.columns)[2],list(Input.columns)[3]]))
   fig = px.line_polar(P_df, r='r', theta='theta', line_close=True,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig)
   fig2 = px.pie(values=pref, names=[list(Input.columns)[0],list(Input.columns)[1],list(Input.columns)[2],list(Input.columns)[3]], hole=.5,color_discrete_sequence=["#0068c9","#83c9ff","#ff2b2b","#ffabab","#29b09d","#7defa1","#ff8700","#ffd16a","#6d3fc0","#d5dae5"])
   st.plotly_chart(fig2)
   temp = tempfile.NamedTemporaryFile(suffix='.png')
   temp2 = tempfile.NamedTemporaryFile(suffix='.png')
   # Save the figures as a pdf 
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
         fig_size=(790, 1440)
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
         fig_size=(790, 1440)
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
         fig_size=(805, 1440)
        )
   df_temp = tempfile.NamedTemporaryFile(suffix='.png')
   df_temp2 = tempfile.NamedTemporaryFile(suffix='.png')
   df_temp3 = tempfile.NamedTemporaryFile(suffix='.png')
   df2img.save_dataframe(fig=Df_fig, filename=df_temp.name)
   df2img.save_dataframe(fig=Df_fig2, filename=df_temp2.name)
   df2img.save_dataframe(fig=Df_fig3, filename=df_temp3.name)
   pdf = FPDF('L')
   pdf.add_page()
   pdf.image(str(df_temp.name))
   pdf.image(str(df_temp2.name))
   pdf.image(str(df_temp3.name))
   pdf.set_font('Arial', 'B', 16)
   pdf.image(str(temp.name),x=-25)
   pdf.cell(40, 1, 'User preference (radar chart)',align = 'L')
   pdf.add_page()
   pdf.image(str(temp2.name),x=25)
   pdf.cell(40, 1, 'User preference (pie chart)',align = 'L')
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


      #generating the survey
      survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
      pages = survey.pages(len(input.index), on_submit=lambda: calculate_and_plot_user_preference(input,lookup,input_ratings(survey.to_json(),input)))#,S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D)) # the survey is first converted to json after which it is given to the download function to download the CSV output

      # generating the survey radios

      with pages:
               col0, padding0, col1, padding1, col2, padding2, col3, padding3 = st.columns([1,1.4,1,1.4,1,1.4,1,1.4])
               with col0:
                       st.write("    ")
                       st.write("    ")
                       Slb0 = survey.selectbox("rating:", options=[1,2,3,4],id=f"A_{pages.current}",label_visibility="collapsed")
               with padding0:
                       st.markdown(f"<p style='text-align: center;'>{(input.iloc[pages.current].tolist())[0].strip()}</p>", unsafe_allow_html=True)
               with col1:
                       st.write("    ")
                       st.write("    ")
                       Slb1 = survey.selectbox("rating:", options=[1,2,3,4],id=f"B_{pages.current}",label_visibility="collapsed")
               with padding1:
                       st.markdown(f"<p style='text-align: center;'>{(input.iloc[pages.current].tolist())[1].strip()}</p>", unsafe_allow_html=True)
               with col2:
                       st.write("    ")
                       st.write("    ")
                       Slb2 = survey.selectbox("rating:", options=[1,2,3,4],id=f"C_{pages.current}",label_visibility="collapsed")
               with padding2:
                       st.markdown(f"<p style='text-align: center;'>{(input.iloc[pages.current].tolist())[2].strip()}</p>", unsafe_allow_html=True)
               with col3:
                       st.write("    ")
                       st.write("    ")
                       Slb3 = survey.selectbox("rating:", options=[1,2,3,4],id=f"D_{pages.current}",label_visibility="collapsed")
               with padding3:
                       st.markdown(f"<p style='text-align: center;'>{(input.iloc[pages.current].tolist())[3].strip()}</p>", unsafe_allow_html=True)
        
