import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:/Users/berka/Downloads/cleaned_university_students_data.csv'
df = pd.read_csv(file_path)

# Scatter plot with a trendline
plt.figure(figsize=(10, 6))
sns.regplot(x='Weekly Study Hours', y='Exam Stress Level', data=df, scatter_kws={'alpha':0.5}, line_kws={'color': 'red'})
plt.title('Relationship Between Weekly Study Hours and Exam Stress Level', fontsize=14)
plt.xlabel('Weekly Study Hours', fontsize=12)
plt.ylabel('Exam Stress Level', fontsize=12)
plt.grid(alpha=0.3)
plt.show()
