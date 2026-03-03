import streamlit as st

conn = st.connection("userdb")
df = conn.query("select * from users")
st.dataframe(df)