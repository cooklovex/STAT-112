import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
data = pd.read_csv(file_path)

# Select variables
study_hours = data['Weekly Study Hours']
sleep_hours = data['Daily Sleep Hours']

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, sleep_hours, alpha=0.6, edgecolor='k')
plt.title('Relationship Between Weekly Study Hours and Daily Sleep Hours', fontsize=14)
plt.xlabel('Weekly Study Hours', fontsize=12)
plt.ylabel('Daily Sleep Hours', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Overview of the data
correlation = study_hours.corr(sleep_hours)
print(f"Correlation between study hours and sleep hours: {correlation:.2f}")
