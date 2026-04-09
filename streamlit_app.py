import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Hello world!")

with st.sidebar:
    st.header("About this app")
    st.write("This is my first app.")

st.header("KodingKyla is learning Streamlit!", divider='rainbow')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Favorite number value")
    st.write("What is you favorite number between 0 and 100?")
    st.markdown("*You may only select one value.*")
    x = st.slider("Select a value", 0, 100, 50)
with col2:
    st.subheader("Your selection")
    st.write("This is your selected value.")
    st.write(f"You selected: {x}")

st.divider()
st.header("Random chart", divider='rainbow')
st.write("This is the chart area for a random number generator.")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.area_chart(df)
