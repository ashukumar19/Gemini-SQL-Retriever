from dotenv import load_dotenv
load_dotenv()

from pandas import read_sql
import streamlit as st 
import os
import sqlite3

import google.generativeai as genai

# Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION TO LOAD GEMINI MODEL AND PROVIDE QUERY AS RESPONSE

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to check database and show sample data
def check_database(db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        
        if tables:
            st.write("Tables in database:", [table[0] for table in tables])
            
            # Show sample data from STUDENT table
            cur.execute("SELECT * FROM STUDENT LIMIT 5;")
            sample_data = cur.fetchall()
            if sample_data:
                st.write("Sample data from STUDENT table:")
                for row in sample_data:
                    st.write(row)
            else:
                st.warning("STUDENT table is empty!")
        else:
            st.error("No tables found in database!")
        
        conn.close()
    except Exception as e:
        st.error(f"Database Error: {e}")

# Function to retrieve query from the SQL database

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"SQL Error: {e}")
        return []

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Ocean Engineering class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Ocean Engineering";
    \nExample 3 - Show me students with marks greater than 85, 
    the SQL command will be something like this SELECT * FROM STUDENT WHERE MARKS > 85;
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="Use me to retrieve any SQL Query")
st.header("Gemini App to get your SQL Data")

# Check database status
if st.button("Check Database"):
    check_database("student.db")

question = st.text_input("Input: ", key='input')

submit = st.button("Ask me Anything")


if submit:
    response = get_gemini_response(question, prompt)
    st.write("Generated SQL Query:")
    st.code(response)
    
    data = read_sql_query(response, "student.db")
    
    if data:
        st.subheader("The Response is")
        for row in data:
            st.write(row)
    else:
        st.warning("No data found or query returned empty results.")
 