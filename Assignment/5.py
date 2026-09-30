import pandas as pd

# Load the final CSV file
df = pd.read_csv("final_student_data.csv")

print("Complete Data:")
print(df)

print("=" * 100)

print("FILTERING IT DEPARTMENT STUDENTS WITH SALARY GREATER THAN 40000")
print()

# Filter IT department and salary > 40000
df1 = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 40000)
]

# Display selected columns
print(df1[["First Name", "Last Name", "Department", "Salary"]])