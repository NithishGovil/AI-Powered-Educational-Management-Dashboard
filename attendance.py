import streamlit as st
import sqlite3

def attendance_module():

    st.header("Attendance Module")

    sid = st.number_input("Student ID",1)

    attendance = st.slider(
        "Attendance %",
        0,
        100,
        75
    )

    if st.button("Update Attendance"):

        conn = sqlite3.connect("college.db")

        cur = conn.cursor()

        cur.execute(
            """
            UPDATE students
            SET attendance=?
            WHERE id=?
            """,
            (attendance,sid)
        )

        conn.commit()
        conn.close()

        st.success("Attendance Updated")