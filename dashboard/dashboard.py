import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

st.header("Analisis Bike Sharing Projek")
st.caption("Projek analisis data dengan python oleh Adib HZ")

st.subheader("Tren Penggunaan Layanan Sepeda Tiap Tahunnya Berdasarkan Musim")

day_df = pd.read_csv("day_dataset.csv")
hour_df = pd.read_csv("hour_dataset.csv")

selected_year = st.selectbox("Pilih Tahun", day_df["yr"].unique())

year_df = day_df[day_df['yr'] == selected_year]

seasonal_usage = year_df.groupby('season')['cnt'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='season', 
    y='cnt', 
    data=seasonal_usage.sort_values(by="cnt", ascending=False), 
    palette='Set2'
)
ax.set_title('Total Penggunaan Sepeda per Musim (Satu Tahun Terakhir)')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

st.write("Tren penggunaan sepeda paling banyak pada tahun 2012 adalah pada saat musim semi(spring), sedangkan yang peling rendah adalah pada saat musim panas(summer)")

st.subheader("Jam Sibuk Penggunaan Sepeda pada Hari Kerja dan Hari Libur")

grouped = hour_df.groupby(['hr', 'is_weekend'])['cnt'].sum().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(12, 6))
grouped.plot(kind='bar', color=['orange', 'blue'], alpha=0.75, ax=ax)

# Menambahkan judul dan label
ax.set_title('Total Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Total Penyewaan')
ax.set_xticks(range(len(grouped.index)))  # Menampilkan semua jam
ax.set_xticklabels(grouped.index, rotation=0)

# Menambahkan grid dan legend
ax.grid(axis='y')
ax.legend(['Hari Kerja', 'Akhir Pekan'])

# Menampilkan grafik di Streamlit
st.pyplot(fig)

st.write("Jam sibuk penggunaan sepeda terjadi di sore hari pada pukul 16-15 dan juga pada pagi hari pukul 7-9, baik ketika hari kerja maupun hari libur")