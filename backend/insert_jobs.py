import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryabhat@10",
    database="internship_ai"
)

cursor = db.cursor()

jobs = pd.read_csv(
   r"C:\Users\Arya\OneDrive\Desktop\AI internship\backend\datasets\final_jobs.csv"
)

for _, row in jobs.iterrows():

    query = """
    INSERT INTO jobs(
        company_name,
        role,
        required_skills,
        location,
        salary,
        description
    )
    VALUES(%s, %s, %s, %s, %s, %s)
    """

    values = (
        1,
        row["role"],
        row["required_skills"],
        row["location"],
        "Not Specified",
        row["description_y"]
    )

    cursor.execute(query, values)

db.commit()

cursor.close()

db.close()

print("Jobs inserted successfully")