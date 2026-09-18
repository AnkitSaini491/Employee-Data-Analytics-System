import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Create Employee Dataset
# -----------------------------------

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit",
             "Anjali", "Vikas", "Pooja", "Karan", "Sneha"],
    "Department": ["IT", "HR", "IT", "Finance", "Sales",
                   "IT", "HR", "Finance", "Sales", "IT"],
    "Age": [24, 29, 26, 31, 28, 25, 35, 30, 27, 24],
    "Experience": [1, 5, 2, 7, 4, 2, 10, 6, 3, 1],
    "Salary": [35000, 50000, 42000, 65000, 48000,
               40000, 70000, 60000, 45000, 38000],
    "Performance": [4, 3, 5, 4, 3, 5, 4, 3, 4, 5],
    "Attrition": ["No", "No", "No", "Yes", "No",
                  "No", "No", "Yes", "No", "No"]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("employee_data.csv", index=False)

print("Employee Data:")
print(df)

# -----------------------------------
# 2. Basic Information
# -----------------------------------

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

# -----------------------------------
# 3. Department-wise Employee Count
# -----------------------------------

department_count = df["Department"].value_counts()

print("\n--- Employees by Department ---")
print(department_count)

# -----------------------------------
# 4. Average Salary by Department
# -----------------------------------

avg_salary = df.groupby("Department")["Salary"].mean()

print("\n--- Average Salary by Department ---")
print(avg_salary)

# -----------------------------------
# 5. Average Experience
# -----------------------------------

average_experience = df["Experience"].mean()

print("\nAverage Employee Experience:",
      round(average_experience, 2), "years")

# -----------------------------------
# 6. Highest Paid Employee
# -----------------------------------

highest_paid = df.loc[df["Salary"].idxmax()]

print("\n--- Highest Paid Employee ---")
print(highest_paid)

# -----------------------------------
# 7. Best Performing Employees
# -----------------------------------

best_performers = df[df["Performance"] == 5]

print("\n--- Best Performing Employees ---")
print(best_performers[["Name", "Department", "Performance"]])

# -----------------------------------
# 8. Attrition Analysis
# -----------------------------------

attrition_count = df["Attrition"].value_counts()

print("\n--- Attrition Analysis ---")
print(attrition_count)

# -----------------------------------
# 9. Department-wise Salary Chart
# -----------------------------------

avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# -----------------------------------
# 10. Employee Count Chart
# -----------------------------------

department_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Employee Distribution by Department")
plt.ylabel("")
plt.tight_layout()
plt.show()

# -----------------------------------
# 11. Experience vs Salary
# -----------------------------------

plt.scatter(df["Experience"], df["Salary"])

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

# -----------------------------------
# 12. Final Report
# -----------------------------------

print("\n========== FINAL ANALYTICS REPORT ==========")

print("Total Employees:", len(df))
print("Total Departments:", df["Department"].nunique())
print("Average Salary: ₹", round(df["Salary"].mean(), 2))
print("Highest Salary: ₹", df["Salary"].max())
print("Average Experience:",
      round(df["Experience"].mean(), 2), "years")

print("\nDepartment with Highest Average Salary:",
      avg_salary.idxmax())

print("Total Employees Who Left:",
      (df["Attrition"] == "Yes").sum())

print("============================================")
print("Analysis Completed Successfully!")
