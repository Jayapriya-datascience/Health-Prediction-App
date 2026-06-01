
# Health Prediction Application

## Overview

The Health Prediction Application is a Python-based application developed using Streamlit and SQLite. It allows users to manage patient health records and predict health risks based on blood test parameters such as Glucose, Haemoglobin, and Cholesterol.

This application demonstrates CRUD (Create, Read, Update, Delete) operations, data validation, persistent storage, and basic health risk prediction.

---

## Features

* Create Patient Records
* View Patient Records
* Update Existing Records
* Delete Patient Records
* Health Risk Prediction
* Input Validation
* SQLite Database Storage
* User-Friendly Streamlit Interface

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas

---

## Project Structure

```text
Health-Prediction-App/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
└── patient.db
```

---

## Input Fields

The application collects the following information:

* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks (Predicted Health Risk)

---

## Health Risk Prediction Logic

The application predicts health risk based on the entered blood test values:

* High Risk:

  * Glucose > 140 OR
  * Cholesterol > 240

* Moderate Risk:

  * Glucose > 110

* Healthy:

  * All values within normal range

---

## CRUD Operations

### Create

Add new patient records and automatically generate a health risk prediction.

### Read

Display all patient records in a tabular format.

### Update

Modify existing patient details and update the prediction result.

### Delete

Remove patient records from the database.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Health-Prediction-App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Machine Learning Model Integration
* External Healthcare API Integration
* User Authentication
* Data Visualization Dashboard
* PDF Report Generation

---

## Author

Jayapriya P

M.Sc. Data Science Graduate

Python | Machine Learning | Data Science
