import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/berka/Downloads/cleaned_university_students_data.csv"
df = pd.read_csv(file_path)

# Group daily sleep hours into bins for categorization
df['Sleep Hour Range'] = pd.cut(df['Daily Sleep Hours'], bins=[0, 4, 6, 8, 10, 12], labels=['0-4', '4-6', '6-8', '8-10', '10-12'])

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sleep Hour Range', y='Daily Screen Time Hours', data=df)
plt.title('Daily Screen Time vs Sleep Hour Ranges', fontsize=14)
plt.xlabel('Sleep Hour Range (Hours)', fontsize=12)
plt.ylabel('Daily Screen Time Hours', fontsize=12)
plt.grid(alpha=0.3)
plt.show()
