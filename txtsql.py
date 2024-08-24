import google.generativeai as genai
import sqlite3

import os 
os.environ["GOOGLE_API_KEY"]="AIzaSyB82BMvWIPevitjjH6ro2oW9VZVephHvPg"
genai.configure(api_key = os.environ["GOOGLE_API_KEY"])


model = genai.GenerativeModel(model_name = "gemini-pro")


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

