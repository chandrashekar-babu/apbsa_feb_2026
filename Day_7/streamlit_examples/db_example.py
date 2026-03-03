import streamlit as st

conn = st.connection("user_accounts")
df = conn.query("select * from users")

"this is a dataframe view"
st.dataframe(df)

"this is a table view"
st.table(df)
