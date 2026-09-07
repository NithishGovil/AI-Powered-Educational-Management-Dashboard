import streamlit as st
import sqlite3
import pandas as pd

def student_module():

    st.header("Student Management")

    name = st.text_input("Student Name")
    dept = st.text_input("Department")
    year = st.number_input("Year",1,4)

    if st.button("Add Student"):

        conn = sqlite3.connect("college.db")

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO students
            (name,department,year)
            VALUES (?,?,?)
            """,
            (name,dept,year)
        )

        conn.commit()
        conn.close()

        st.success("Student Added Successfully")

    conn = sqlite3.connect("college.db")

    df = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    st.dataframe(df)
    st.subheader("Update Student Marks")

    student_id = st.number_input(
        "Student ID",
         min_value=1,
        key="marks_id"
    )

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        key="marks_value"
    )

    if st.button("Update Marks"):

        conn = sqlite3.connect("college.db")

        cur = conn.cursor()

        cur.execute(
            """
            UPDATE students
            SET marks = ?
            WHERE id = ?
            """,
            (marks, student_id)
        )

        conn.commit()
        conn.close()

        st.success("Marks Updated Successfully")
        st.rerun()