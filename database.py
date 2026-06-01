import sqlite3

def create_table():
    conn = sqlite3.connect("patient.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob TEXT,
        email TEXT,
        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_patient(data):
    conn = sqlite3.connect("patient.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO patients
    (name,dob,email,glucose,haemoglobin,cholesterol,remarks)
    VALUES(?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()

def view_patients():
    conn = sqlite3.connect("patient.db")
    c = conn.cursor()

    c.execute("SELECT * FROM patients")

    data = c.fetchall()

    conn.close()

    return data

def delete_patient(id):
    conn = sqlite3.connect("patient.db")
    c = conn.cursor()

    c.execute("DELETE FROM patients WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def update_patient(id, name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = sqlite3.connect("patient.db")
    c = conn.cursor()

    c.execute("""
    UPDATE patients
    SET name=?,
        dob=?,
        email=?,
        glucose=?,
        haemoglobin=?,
        cholesterol=?,
        remarks=?
    WHERE id=?
    """, (
        name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks,
        id
    ))

    conn.commit()
    conn.close()
    