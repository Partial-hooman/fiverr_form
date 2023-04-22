
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
