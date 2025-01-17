import pandas as pd
import numpy as np
import os

# Veri kümesini yükleme
file_path = "C:/Users/berka/Downloads/dirtydata.csv"  # Dosya yolunu güncelleyin
df = pd.read_csv(file_path, delimiter=";")  # Ayırıcıyı belirtiyoruz

# Sütun adlarını düzenleme
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
print("Düzenlenmiş sütun adları:", df.columns)

# Çalışılacak sütunlar
work_1c = [
    "study_hours_per_week",
    "sleep_hours_per_night",
    "exam_stress_level",
    "screen_time_hours_per_day"
]

# Eksik sütunları kontrol et
missing_columns = [col for col in work_1c if col not in df.columns]
if missing_columns:
    raise KeyError(f"Missing columns in the dataset: {missing_columns}")

# Çalışılacak sütunları kopyalama
work_2c = df[work_1c].copy()

# 1. "study_hours_per_week" temizleme
hours_study_mode = work_2c['study_hours_per_week'].mode()[0]
work_2c['study_hours_per_week'] = (
    work_2c['study_hours_per_week']
    .replace(['na', 'NA'], hours_study_mode)
    .astype(float)
    .apply(lambda x: max(0, min(x, 80)))  # Değerleri 0 ile 80 arasında sınırlama
    .round()
)

# 2. "sleep_hours_per_night" temizleme
sleep_mode = work_2c['sleep_hours_per_night'].mode()[0]
work_2c['sleep_hours_per_night'] = (
    work_2c['sleep_hours_per_night']
    .replace(['na', 'NA'], sleep_mode)
    .astype(float)
    .apply(lambda x: max(0, min(x, 12)))  # Uyku saatlerini 0 ile 12 arasında sınırlama
    .round()
)

# 3. "exam_stress_level" temizleme
stress_mode = work_2c['exam_stress_level'].mode()[0]
work_2c['exam_stress_level'] = (
    work_2c['exam_stress_level']
    .replace(['na', 'NA'], stress_mode)
    .astype(float)
    .apply(lambda x: max(1, min(x, 10)))  # Stres seviyesini 1 ile 10 arasında sınırlama
    .round()
)

# 4. "screen_time_hours_per_day" temizleme
screen_time_mode = work_2c['screen_time_hours_per_day'].mode()[0]
work_2c['screen_time_hours_per_day'] = (
    work_2c['screen_time_hours_per_day']
    .replace(['na', 'NA'], screen_time_mode)
    .astype(float)
    .apply(lambda x: max(0, min(x, 16)))  # Ekran süresini 0 ile 16 saat arasında sınırlama
    .round()
)

# Sütun adlarını yeniden adlandırma
work_2c.rename(columns={
    "study_hours_per_week": "Weekly Study Hours",
    "sleep_hours_per_night": "Daily Sleep Hours",
    "exam_stress_level": "Exam Stress Level",
    "screen_time_hours_per_day": "Daily Screen Time Hours"
}, inplace=True)

# Temizlenmiş verileri kaydetme
save_path = r'C:\Users\berka\Downloads\Project_University_Students'
if not os.path.exists(save_path):
    os.makedirs(save_path)
new_file_path = os.path.join(save_path, 'cleaned_university_students_data.csv')
work_2c.to_csv(new_file_path, index=False)

# Temizlenmiş verileri kontrol etme
print(work_2c.info())
print(work_2c.head())
print(f"Cleaned data saved to: {new_file_path}")


