import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def analytics_module():

    st.header("Analytics Dashboard")

    conn = sqlite3.connect("college.db")

    # ==========================
    # STUDENT DATA
    # ==========================

    df = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Students",
        len(df)
    )

    col2.metric(
        "Average Attendance",
        round(
            df["attendance"].fillna(0).mean(),
            2
        )
    )

    col3.metric(
        "Departments",
        df["department"].nunique()
    )

    # ==========================
    # STUDENT RECORDS
    # ==========================

    st.subheader("Student Records")

    st.dataframe(df)

    # ==========================
    # ATTENDANCE ANALYSIS
    # ==========================

    st.subheader("Attendance Analysis")

    if not df.empty:

        fig, ax = plt.subplots(
            figsize=(10,5)
        )

        ax.bar(
            df["name"],
            df["attendance"].fillna(0)
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.ylabel(
            "Attendance (%)"
        )

        plt.xlabel(
            "Students"
        )

        plt.title(
            "Student Attendance Analysis"
        )

        plt.tight_layout()

        st.pyplot(fig)

    # ==========================
    # DEPARTMENT PIE CHART
    # ==========================

    st.subheader(
        "Department Distribution"
    )

    if not df.empty:

        dept_counts = (
            df["department"]
            .value_counts()
        )

        fig2, ax2 = plt.subplots(
            figsize=(7,7)
        )

        ax2.pie(
            dept_counts,
            labels=dept_counts.index,
            autopct="%1.1f%%"
        )

        ax2.set_title(
            "Department Distribution"
        )

        st.pyplot(fig2)

    # ==========================
    # REVENUE ANALYTICS
    # ==========================

    st.subheader(
        "Fee Analytics"
    )

    fee_df = pd.read_sql_query(
        "SELECT * FROM fees",
        conn
    )

    if not fee_df.empty:

        total_revenue = fee_df[
            fee_df["status"] == "Paid"
        ]["amount"].sum()

        paid_students = len(
            fee_df[
                fee_df["status"] == "Paid"
            ]
        )

        pending_students = len(
            fee_df[
                fee_df["status"] == "Pending"
            ]
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Revenue Generated",
            f"₹{total_revenue:,.0f}"
        )

        col5.metric(
            "Paid Students",
            paid_students
        )

        col6.metric(
            "Pending Students",
            pending_students
        )

        # Revenue Chart

        revenue_data = fee_df[
            "status"
        ].value_counts()

        fig3, ax3 = plt.subplots(
            figsize=(6,4)
        )

        ax3.bar(
            revenue_data.index,
            revenue_data.values
        )

        ax3.set_title(
            "Fee Status Analysis"
        )

        ax3.set_ylabel(
            "Number of Students"
        )

        st.pyplot(fig3)

    else:

        st.warning(
            "No fee records available."
        )

    conn.close()