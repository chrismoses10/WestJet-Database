import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\chris\Downloads\WestJet_Chatbot\WestJet_Claims.db")

df = pd.read_sql_query("SELECT * FROM CLAIMS", conn)

conn.close()

print(df.head())