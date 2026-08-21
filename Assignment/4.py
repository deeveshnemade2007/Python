import pandas as pd

df = pd.read_csv("C:/Users/Deevesh Nemade/Downloads/student_dataset_25.csv")
print(df)

print("="*100)
missing_data = df.isnull().sum()

print(missing_data)

print("="*100)
print("df.drop_duplicated().sum()")

print("="*100)
print(df.drop_duplicates())

print("="*100)
# numeric_col=df.select_dtypes(include=["number"]).columns

# metrices_df=pd.DataFrame({
#    'mean':df[numeric_col].mean()
#})
#print(metrices_df)

mean_age = df["Age"].mean()
print(f"Mean Age: {mean_age}")

mean_salary = df["Salary"].mean()
print(f"Mean Salary: {mean_salary}")

print("="*100)
df['Age'] = df['Age'].fillna(mean_age)
df['Salary'] = df['Salary'].fillna(mean_salary)