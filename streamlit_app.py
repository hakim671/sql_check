import streamlit as st
import psycopg2
import pandas as pd

st.title("My PostgreSQL App")

try:
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"]
    )

    st.success("✅ PostgreSQL connected!")

    df = pd.read_sql("SELECT * FROM users", conn)

    st.dataframe(df)

    conn.close()

except Exception as e:
    st.error(f"❌ Connection error: {e}")
