import pandas as pd

df1 = pd.read_json("C:/Users/Deevesh Nemade/Downloads/nepse-listed-companies-2021.json")

print(df1)
print()

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print()
df2= pd.read_csv("C:/Users/Deevesh Nemade/Downloads/customers-100.csv")

print(df2)





import pandas as pd

df1 = pd.read_json("C:/Users/Deevesh Nemade/Downloads/nepse-listed-companies-2021.json")
df2 = pd.read_csv("C:/Users/Deevesh Nemade/Downloads/customers-100.csv")

print("DF1 — last 5 rows:")
print(df1.tail())

print("\nDF1 — shape (rows, columns):")
print(df1.shape)

print("\nDF1 — column types and non-null values:")
df1.info()

print("\nDF1 — statistical summary:")
print(df1.describe(include="all"))

print("\n" + "-" * 100 + "\n")

print("DF2 — last 5 rows:")
print(df2.tail())

print("\nDF2 — shape (rows, columns):")
print(df2.shape)

print("\nDF2 — column types and non-null values:")
df2.info()

print("\nDF2 — statistical summary:")
print(df2.describe(include="all"))




