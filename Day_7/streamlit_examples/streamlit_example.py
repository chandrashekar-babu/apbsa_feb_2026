import streamlit as st

'Hello, Streamlit!'

st.title("Welcome to Streamlit!")
st.header("This is a simple Streamlit app.")

st.write('You can write text, display data, and create interactive widgets.')
st.write('For example, here is a slider widget:')

st.markdown("---")
st.markdown("### Slider Example")

slider_value = st.slider('Select a value', 0, 100, 50)
st.write(f'You selected: {slider_value}')
st.write('You can also display data in a table:')

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.table(df)
st.write('This is just a basic example. Streamlit has many more features to explore!')