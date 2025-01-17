import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
data = pd.read_csv(file_path)

# Categorize weekly study hours into ranges
data['Study Hour Range'] = pd.cut(data['Weekly Study Hours'], bins=[0, 10, 20, 30, 40, 50], labels=['0-10', '10-20', '20-30', '30-40', '40-50'])

# Calculate the average daily sleep duration for each study hour range
average_sleep = data.groupby('Study Hour Range')['Daily Sleep Hours'].mean().reset_index()

# Create a heatmap
plt.figure(figsize=(8, 6))
heatmap_data = average_sleep.pivot_table(index='Study Hour Range', values='Daily Sleep Hours')
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', cbar_kws={'label': 'Average Daily Sleep Hours'})
plt.title('Average Daily Sleep Duration by Weekly Study Hour Range', fontsize=14)
plt.xlabel('Weekly Study Hour Range', fontsize=12)
plt.ylabel('Average Daily Sleep Hours', fontsize=12)
plt.yticks(rotation=0)
plt.show()
