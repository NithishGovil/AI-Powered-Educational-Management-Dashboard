import streamlit as st
import sqlite3

def fee_module():

    st.header("Fee Management")

    sid = st.number_input("Student ID")

    amount = st.number_input("Fee Amount")

    status = st.selectbox(
        "Status",
        ["Paid","Pending"]
    )

    if st.button("Save Fee"):

        conn = sqlite3.connect("college.db")

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO fees
            (student_id,amount,status)
            VALUES(?,?,?)
            """,
            (sid,amount,status)
        )

        conn.commit()
        conn.close()

        st.success("Fee Saved")