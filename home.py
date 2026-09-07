import streamlit as st
import sqlite3
import pandas as pd

def home_module():

    st.title(
        "Educational Institute Management System"
    )

    st.success(
        "Welcome to the Dashboard"
    )

    conn = sqlite3.connect(
        "college.db"
    )

    students = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    fees = pd.read_sql_query(
        "SELECT * FROM fees",
        conn
    )

    conn.close()

    total_students = len(
        students
    )

    avg_attendance = round(
        students["attendance"]
        .fillna(0)
        .mean(),
        2
    )

    revenue = 0

    if not fees.empty:

        revenue = fees[
            fees["status"] == "Paid"
        ]["amount"].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Students",
        total_students
    )

    col2.metric(
        "Average Attendance",
        f"{avg_attendance}%"
    )

    col3.metric(
        "Revenue",
        f"₹{revenue:,.0f}"
    )

    st.markdown("---")

    st.subheader(
        "System Features"
    )

    st.markdown("""
    ✅ Student Management

    ✅ Attendance Tracking

    ✅ Fee Management

    ✅ Analytics Dashboard

    ✅ AI Prediction

    ✅ Business Intelligence Reports
    """)