import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
data = pd.read_csv(file_path)

# Calculate the average sleep duration for each exam stress level
average_sleep = data.groupby('Exam Stress Level')['Daily Sleep Hours'].mean()

# Create a bar plot
plt.figure(figsize=(10, 6))
average_sleep.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Average Daily Sleep Duration by Exam Stress Level', fontsize=14)
plt.xlabel('Exam Stress Level', fontsize=12)
plt.ylabel('Average Daily Sleep Hours', fontsize=12)
plt.grid(alpha=0.3, linestyle='--')
plt.xticks(rotation=0)
plt.show()

# Print the averages for verification
print(average_sleep)
