import dotenv

dotenv.load_dotenv()

import mysql.connector
from google import genai  # Updated to the new SDK
import os
import streamlit as st

# Initialize the new Client
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))


def get_gemini_response(question, prompt_text):
    # Use gemini-2.5-flash for stable free access
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{prompt_text}\n\nQuestion: {question}"
    )
    return response.text


def read_sql_query(sql, db):
    connection = mysql.connector.connect(
        database=db,
        host="localhost",
        user="root",
        password="Seshathri3@"  # Use your actual password securely
    )
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.close()
    return results


# Simplified prompt as a string
prompt_context = """
You are an expert in converting English questions to SQL query!
The Database name is 'student'. 
The Table name is 'students' (plural). 
The columns are: id, name, age, marks.

Example: How many students are there?
Query: SELECT COUNT(*) FROM students;

CRITICAL: Only return the raw SQL query. Do not include markdown backticks or the word 'SQL'.
"""
st.set_page_config(page_title="Gemini SQL Retriever")
st.header("Gemini SQL Retriever")

question = st.text_input("Enter question", key="input")
submit = st.button("Generate & Run Query")

if submit:
    with st.spinner("Generating SQL..."):
        try:
            # 1. Get the SQL query from Gemini
            sql_query = get_gemini_response(question, prompt_context).strip()
            st.subheader("Generated SQL:")
            st.code(sql_query, language="sql")

            # 2. Execute against local MySQL
            results = read_sql_query(sql_query, "student")

            # 3. Display Results
            st.subheader("Database Results:")
            if results:
                st.table(results)
            else:
                st.write("Query successful, but no data found.")
        except Exception as e:
            st.error(f"Error: {e}")