import streamlit as st
import df2img
import base64
import tempfile 
from fpdf import FPDF
import plotly.express as px
import streamlit as st
import streamlit_survey as ss
import pandas as pd

st.set_page_config(
    page_title="car comparison",
    page_icon="",
)


st.write("# CAR COMPARISON")

st.sidebar.success("Select a method.")
