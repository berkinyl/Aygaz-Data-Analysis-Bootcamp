import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleme
file_path = 'openpowerlifting.csv'
data = pd.read_csv(file_path)

# İlk 5 satırı görüntüle
print("Veri setinin ilk 5 satırı:")
print(data.head())

# Sütun isimlerini görüntüle
print("\nVeri seti sütunları:")
print(data.columns)

def add_random_missing_values(dataframe: pd.DataFrame, missing_rate: float = 0.1) -> pd.DataFrame:
    """
    Bir DataFrame'e rastgele NaN değerler ekler.
    
    Args:
        dataframe (pd.DataFrame): İşlenecek veri seti.
        missing_rate (float): Eksik değer oranı (varsayılan: 0.1).
        
    Returns:
        df_missing (pd.DataFrame): Eksik değerler eklenmiş DataFrame.
    """
    df_missing = dataframe.copy()
    df_size = dataframe.size
    num_missing = int(df_size * missing_rate)

    for _ in range(num_missing):
        row_idx = random.randint(0, dataframe.shape[0] - 1)
        col_idx = random.randint(0, dataframe.shape[1] - 1)
        df_missing.iat[row_idx, col_idx] = np.nan

    return df_missing

# Eksik değerlerin eklenmesi
data = add_random_missing_values(data, missing_rate=0.1)

# Eksik değerlerin toplamını görüntüle
print("Eksik değerlerin toplamı:")
print(data.isnull().sum())

# Eksik değerlerin doldurulması ve temizlenmesi
data['BodyweightKg'] = data['BodyweightKg'].fillna(data['BodyweightKg'].median())
data = data.dropna(subset=['Age', 'Sex', 'BestSquatKg', 'BestBenchKg', 'BestDeadliftKg'])

# Negatif değerlerin temizlenmesi
data = data[data['Age'] > 0]
weight_columns = ['BestSquatKg', 'BestBenchKg', 'BestDeadliftKg']
for col in weight_columns:
    data = data[data[col] >= 0]

# Cinsiyet sütununu kategorik yapma
data['Sex'] = data['Sex'].astype('category')

# Temizlenmiş veri setini görüntüle
print("Temizlenen veri setinin ilk 5 satırı:")
print(data.head())

print("\nEksik değerlerin toplamı (temizleme sonrası):")
print(data.isnull().sum())

# Cinsiyet dağılımını görselleştirme
sex_counts = data['Sex'].value_counts()
sex_counts.plot(kind='bar', color=['blue', 'orange'])
plt.title('Cinsiyet Dağılımı')
plt.xlabel('Cinsiyet')
plt.ylabel('Frekans')
plt.xticks(ticks=[0, 1], labels=['Female', 'Male'])
plt.show()

# Yaşa Göre Toplam Kaldırış
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='TotalKg', hue='Sex', data=data)
plt.title('Yaşa Göre Toplam Kaldırış')
plt.xlabel('Yaş')
plt.ylabel('Toplam Kaldırış (Kg)')
plt.legend(title='Cinsiyet')
plt.show()

# Korelasyon Matrisi
corr_matrix = data[['Age', 'BodyweightKg', 'BestSquatKg', 'BestBenchKg', 'BestDeadliftKg', 'TotalKg']].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title('Korelasyon Matrisi')
plt.show()
