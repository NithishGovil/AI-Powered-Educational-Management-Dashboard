import streamlit as st

# ==========================
# PAGE SETTINGS
# ==========================

st.set_page_config(
    page_title="AI-Powered Educational Management Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# IMPORT MODULES
# ==========================

from login import login
from home import home_module
from student import student_module
from attendance import attendance_module
from fee import fee_module
from analytics import analytics_module
from prediction import prediction_module

# ==========================
# LOGIN SESSION MANAGEMENT
# ==========================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# ==========================
# LOGOUT BUTTON
# ==========================

if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

# ==========================
# DASHBOARD TITLE
# ==========================

st.title("AI-Powered Educational Management Dashboard")

# ==========================
# SIDEBAR MENU
# ==========================

menu = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Student",
        "Attendance",
        "Fee",
        "Analytics",
        "Prediction"
    ]
)

# ==========================
# MODULE ROUTING
# ==========================

if menu == "Home":
    home_module()

elif menu == "Student":
    student_module()

elif menu == "Attendance":
    attendance_module()

elif menu == "Fee":
    fee_module()

elif menu == "Analytics":
    analytics_module()

elif menu == "Prediction":
    prediction_module()
