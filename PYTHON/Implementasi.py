# File: apriori_analysis_with_visuals.py

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns

# Data Pengunjung per Fakultas dan Peminjaman
data = {
    "Bulan": [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni"
    ],
    "FISIP_Pengunjung": [419, 423, 899, 454, 1131, 1022],
    "FKIP_Pengunjung": [840, 917, 1821, 877, 1396, 1152],
    "FEBM_Pengunjung": [298, 628, 2173, 1477, 1599, 1941],
    "FIKP_Pengunjung": [94, 222, 1176, 717, 855, 826],
    "FTTK_Pengunjung": [147, 109, 312, 128, 79, 129],
    "FISIP_Peminjaman": [14, 62, 972, 64, 137, 73],
    "FKIP_Peminjaman": [99, 135, 399, 84, 242, 115],
    "FEBM_Peminjaman": [9, 47, 757, 367, 409, 292],
    "FIKP_Peminjaman": [2, 1, 5, 4, 3, 2],
    "FTTK_Peminjaman": [0, 1, 3, 0, 2, 5],
}

# Membuat DataFrame dari Data
df = pd.DataFrame(data)

# Konversi data menjadi kategori dengan rentang kunjungan/peminjaman tinggi/sedang/rendah
def categorize(value):
    if value > 500:
        return "Tinggi"
    elif value > 100:
        return "Sedang"
    else:
        return "Rendah"

# Terapkan kategori pada semua kolom pengunjung dan peminjaman
for col in df.columns[1:]:
    df[col] = df[col].apply(categorize)

# Gabungkan kolom fakultas untuk analisis asosiasi
data_for_analysis = pd.get_dummies(df.drop(columns=["Bulan"]))

# Menampilkan dataset dengan one-hot encoding
print("Dataset One-Hot Encoded:")
print(data_for_analysis)

# Menerapkan algoritma Apriori untuk menemukan itemsets yang sering
frequent_itemsets = apriori(data_for_analysis, min_support=0.3, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Menemukan aturan asosiasi berdasarkan itemsets
# Untuk versi lama `mlxtend`, tambahkan parameter `num_itemsets` jika diperlukan
try:
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
except TypeError:
    rules = association_rules(frequent_itemsets, num_itemsets=len(frequent_itemsets), metric="confidence", min_threshold=0.7)

# Pastikan antecedents dan consequents dalam bentuk string agar mudah dibaca
rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

print("\nAturan Asosiasi:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Filter aturan dengan lift > 1 untuk menemukan hubungan bermakna
filtered_rules = rules[rules['lift'] > 1]
print("\nAturan Asosiasi dengan Lift > 1:")
print(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Simpan hasil ke file CSV untuk analisis lebih lanjut
frequent_itemsets.to_csv("frequent_itemsets.csv", index=False)
rules.to_csv("association_rules.csv", index=False)
filtered_rules.to_csv("filtered_rules.csv", index=False)

# Visualisasi Frequent Itemsets
plt.figure(figsize=(10, 6))
plt.barh(frequent_itemsets['itemsets'].astype(str), frequent_itemsets['support'], color='skyblue')
plt.xlabel('Support')
plt.ylabel('Itemsets')
plt.title('Frequent Itemsets')
plt.tight_layout()
plt.show()

# Visualisasi Aturan Asosiasi dengan Scatterplot (Confidence vs Lift)
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=rules,
    x='confidence',
    y='lift',
    size='support',
    hue='antecedents',
    palette='viridis',
    sizes=(50, 500),
    alpha=0.7
)
plt.title('Confidence vs Lift (Aturan Asosiasi)')
plt.xlabel('Confidence')
plt.ylabel('Lift')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Antecedents')
plt.tight_layout()
plt.show()
