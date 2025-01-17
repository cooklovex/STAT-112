import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
data = pd.read_csv(file_path)

# Categorize screen time into ranges
data['Screen Time Range'] = pd.cut(data['Daily Screen Time Hours'], bins=[0, 4, 8, 12, 16], labels=['0-4', '4-8', '8-12', '12-16'])

# Calculate the mean exam stress level for each screen time range
average_stress = data.groupby('Screen Time Range')['Exam Stress Level'].mean()

# Create a line plot
plt.figure(figsize=(10, 6))
average_stress.plot(kind='line', marker='o', color='blue')
plt.title('Relationship Between Screen Time and Exam Stress Levels', fontsize=14)
plt.xlabel('Daily Screen Time Range (Hours)', fontsize=12)
plt.ylabel('Average Exam Stress Level', fontsize=12)
plt.grid(alpha=0.3, linestyle='--')
plt.xticks(rotation=0)
plt.show()

# Print the averages for verification
print(average_stress)
