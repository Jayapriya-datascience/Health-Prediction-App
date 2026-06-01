import streamlit as st
import pandas as pd
from datetime import date
from database import create_table, add_patient, view_patients, delete_patient, update_patient
from datetime import datetime

# Create database table
create_table()

# Title
st.title("Health Prediction Application")

# Input Fields
name = st.text_input("Full Name")
from datetime import date

dob = st.date_input(
    "Date of Birth",
    value=date(2001, 10, 13),
    min_value=date(1950, 1, 1),
    max_value=date.today()
)

email = st.text_input("Email")
glucose = st.number_input("Glucose")
haemoglobin = st.number_input("Haemoglobin")
cholesterol = st.number_input("Cholesterol")

# Validation
if email and "@" not in email:
    st.error("Invalid Email Address")

if dob > date.today():
    st.error("Future date is not allowed")

# Prediction Function
def predict_health(glucose, haemoglobin, cholesterol):

    if glucose > 140 or cholesterol > 240:
        return "High Risk"

    elif glucose > 110:
        return "Moderate Risk"

    else:
        return "Healthy"

# Save Button
if st.button("Predict and Save"):

    if not name:
        st.error("Please enter Full Name")

    elif not email:
        st.error("Please enter Email")

    else:
        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient((
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        ))

        st.success("Saved Successfully")

# Display Records
st.subheader("Patient Records")

patients = view_patients()

if patients:
    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df) 
    st.write(f"Total Records: {len(df)}")
    st.subheader("Delete Patient")

delete_id = st.number_input(
    "Enter Patient ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Record"):
    delete_patient(delete_id)
    st.success("Record Deleted Successfully")

# Update Section
st.subheader("Update Patient")

update_id = st.number_input(
    "Patient ID to Update",
    min_value=1,
    step=1,
    key="update_id"
)

new_name = st.text_input("New Name")
new_email = st.text_input("New Email")
new_glucose = st.number_input("New Glucose", key="g")
new_haemoglobin = st.number_input("New Haemoglobin", key="h")
new_cholesterol = st.number_input("New Cholesterol", key="c")

if st.button("Update Record"):

    remarks = predict_health(
        new_glucose,
        new_haemoglobin,
        new_cholesterol
    )

    update_patient(
        update_id,
        new_name,
        str(dob),
        new_email,
        new_glucose,
        new_haemoglobin,
        new_cholesterol,
        remarks
    )

    st.write("Updating ID:", update_id)
    st.success("Record Updated Successfully")

