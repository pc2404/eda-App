import streamlit as st
import numpy as np
import pandas as pd

@st.cache
def load_data(example_data, uploaded_file):
    """
    Loading data
    """
    if example_data:
        df = pd.DataFrame(
            np.random.rand(100, 5),
            columns=['a', 'b', 'c', 'd', 'e']
        )
    else:
        ## Loading csv
        df = pd.read_csv(uploaded_file)
    return df