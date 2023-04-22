
import df2img
import base64
import tempfile 
from fpdf import FPDF
import plotly.express as px
import streamlit as st
import streamlit_survey as ss
import pandas as pd
from streamlit_option_menu import option_menu


with st.sidebar:
    choose = option_menu("Car comparison", ["method1","method2"])
    

if choose == "method1":
  Input = st.file_uploader("upload the input csv", type='csv', key="method1")
  Lookup = st.file_uploader("upload the lookup CSV", type='csv',key="method1_lookup")


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
      pages = survey.pages(len(input.index), on_submit=lambda: calculate_and_plot_user_preference(input,lookup,input_selection(survey.to_json()),S_count,G_count,O_count,T_count,S,G,O,T,A,B,C,D)) # the survey is first converted to json after which it is given to the download function to download the CSV output

      # generating the survey radios

      with pages:
               st.subheader("question " + str(pages.current+1))
               radio = survey.radio(label="label",
                         options=input.iloc[pages.current].tolist(),
                         index=0,
                         label_visibility="collapsed",
                         horizontal=True,
                         id=str(pages.current)
                         )                   
