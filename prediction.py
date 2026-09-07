from sklearn.ensemble import RandomForestRegressor
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def prediction_module():

    st.header("AI Student Performance Prediction")

    conn = sqlite3.connect("college.db")

    df = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    conn.close()

    # Remove rows with missing values
    df = df.dropna()

    if len(df) >= 5:

        X = df[["attendance"]]

        y = df["marks"]

        # Improved Random Forest Model
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X, y)

        st.subheader(
            "Predict Student Marks"
        )

        attendance = st.slider(
            "Attendance Percentage",
            0,
            100,
            75
        )

        prediction = model.predict(
            [[attendance]]
        )

        predicted_marks = prediction[0]

        # Prediction Card
        st.metric(
            "Predicted Final Marks",
            f"{predicted_marks:.2f}"
        )

        # Performance Analysis
        st.subheader("Performance Analysis")

        if predicted_marks >= 85:
            st.success(
                "Excellent Performance Expected"
            )

        elif predicted_marks >= 70:
            st.info(
                "Good Performance Expected"
            )

        elif predicted_marks >= 50:
            st.warning(
                "Average Performance Expected"
            )

        else:
            st.error(
                "Needs Academic Improvement"
            )

        # Visualization
        st.subheader(
            "Prediction Visualization"
        )

        fig, ax = plt.subplots(figsize=(6,4))

        ax.bar(
            ["Attendance", "Predicted Marks"],
            [attendance, predicted_marks]
        )

        ax.set_title(
            "Student Performance Prediction"
        )

        ax.set_ylabel("Value")

        st.pyplot(fig)

        # Dataset Information
        st.subheader(
            "Training Dataset Information"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Students Trained",
            len(df)
        )

        col2.metric(
            "Average Attendance",
            round(df["attendance"].mean(), 2)
        )

        col3.metric(
            "Average Marks",
            round(df["marks"].mean(), 2)
        )

    else:

        st.warning(
            "Need at least 5 records with attendance and marks."
        )