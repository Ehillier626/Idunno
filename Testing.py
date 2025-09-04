import streamlit as st
import pandas as pd
import numpy as np
from Function import Addition
st.title("Select a date")

a = st.slider("select Number", 1, 100, key="a")

b = st.slider("select Number", 1, 100, key="b")

Addition(a, b)

st.write("The addition is", Addition(a, b))
