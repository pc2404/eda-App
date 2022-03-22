import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from src.utils import *

st.set_page_config(layout="wide")
st.title("📊 Exploratory Data Analysis App")
st.write("""The application lets you explore the uploaded dataset completely from top to down. 
You can view the report in the section named ***Pandas Profiling Report***.""")
st.sidebar.title("🛠 Controls")

with st.sidebar.header('📤 Upload data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    example_data=False
    filename=uploaded_file.name
else:
    example_data=True
    filename="Example Dataset"

st.sidebar.header("🔍 Pandas Profiling")
temp = st.sidebar.progress(0)
if st.sidebar.button('Run'):
    df = load_data(example_data, uploaded_file)
    st.write("---")
    st.header('**Input DataFrame**')
    st.write("Dataset Chosen : ",filename)
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr)
    temp.progress(100)
