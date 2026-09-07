import streamlit as st

from login import login

from modules.home import home_module
from modules.student import student_module
from modules.attendance import attendance_module
from modules.fee import fee_module
from modules.analytics import analytics_module
from modules.prediction import prediction_module

# ==========================
# LOGIN SESSION MANAGEMENT
# ==========================

if "logged_in" not in st.session_state:

    st.session_state[
        "logged_in"
    ] = False

if not st.session_state[
    "logged_in"
]:

    login()

    st.stop()

# ==========================
# PAGE SETTINGS
# ==========================

st.set_page_config(
    page_title="Educational Dashboard",
    layout="wide"
)

# ==========================
# LOGOUT BUTTON
# ==========================

if st.sidebar.button(
    "Logout"
):

    st.session_state[
        "logged_in"
    ] = False

    st.rerun()

# ==========================
# DASHBOARD TITLE
# ==========================

st.title(
    "Business Management Dashboard for Educational Institutes"
)

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