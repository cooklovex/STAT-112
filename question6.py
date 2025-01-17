import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
data = pd.read_csv(file_path)

# Remove rows where the Daily Screen Time is in the 12-16 hours range
data = data[(data['Daily Screen Time Hours'] < 12)]

# Categorize daily screen time into ranges
data['Screen Time Range'] = pd.cut(data['Daily Screen Time Hours'], bins=[0, 4, 8, 12], labels=['0-4', '4-8', '8-12'])

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Screen Time Range', y='Exam Stress Level', data=data, palette='muted', inner='quartile')
plt.title('Distribution of Exam Stress Levels by Daily Screen Time Range', fontsize=14)
plt.xlabel('Daily Screen Time Range (Hours)', fontsize=12)
plt.ylabel('Exam Stress Level', fontsize=12)
plt.grid(alpha=0.3)
plt.show()
