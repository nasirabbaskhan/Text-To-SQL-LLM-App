import google.generativeai as genai #type:ignore
import streamlit as st
# importing for env variables loader
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

# configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# function to load Model and provide sql query as response
def get_gemini_response(prompt, question):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text


# function to retrieve query from the sql data base
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# definning your prompt

prompt = [
    """
    You are an expert in converting English questions to SQL queries! 
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION, and MARKS. 

    For Example:
    - Example 1: How many entries of records are present? 
      The SQL command will be: SELECT COUNT(*) FROM STUDENT;
    - Example 2: Tell me all the students studying in Data Science class? 
      The SQL command will be: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Provide the clean query that can be executed on the database without using any backticks or additional characters.
    The SQL command should not include any formatting characters or the word "SQL".
    """
]

# also the SQL code should not have ''' in biggining or end and sql word in output.

# streamlit app    
st.set_page_config(page_title="retrieve sql queryF")
st.header(" Gemini App to Retrieve SQL Data")

user_question = st.text_input("input:", key="input")

sumbit = st.button("ask the question")

if sumbit:
    sql_query = get_gemini_response(prompt,user_question)
    print(sql_query)
    data = read_sql_query(sql_query,"student.db")
    st.subheader("The resplonse is:")
    for row in data:
        print(row)
        st.write(row)
        