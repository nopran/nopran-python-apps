import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Pengaturan Style dan Palet Warna
sns.set(style="whitegrid")
palette = sns.color_palette("viridis")

# Judul Aplikasi
st.title('Optimasi Pertumbuhan Tanaman: Analisis Kondisi Lingkungan')

# Fungsi untuk Memuat Data
@st.cache
def load_data():
    data = pd.read_csv('sf.csv')
    return data

# Fungsi untuk Membuat Plot
def plot_dist(column, title):
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True, bins=30, color=palette[2], ax=ax)
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(column, fontsize=14)
    ax.set_ylabel('Frekuensi', fontsize=14)
    # Menambahkan Anotasi
    mean_val = data[column].mean()
    ax.axvline(mean_val, color='red', linestyle='--')
    ax.text(mean_val+0.5, 10, f'Rata-rata: {mean_val:.2f}', color='red')
    return fig

# Memuat Data
data = load_data()

# Bagian: Menampilkan Data Mentah
st.write("### Data Mentah")
st.dataframe(data.head())

# Bagian: Penjelasan Data
st.write("### Penjelasan Data")
st.markdown("""
Ini adalah data yang berkaitan dengan kondisi pertanian, mencakup:
- **N, P, K**: Nutrisi tanah
- **Temperature**: Suhu lingkungan
- **Humidity**: Kelembaban
- **pH**: Tingkat keasaman tanah
- **Rainfall**: Curah hujan
- **Label**: Jenis tanaman
""")

# Bagian: Visualisasi Data
st.write("### Visualisasi Data")

# Distribusi Suhu
st.write("#### Distribusi Suhu")
st.pyplot(plot_dist('temperature', 'Distribusi Suhu'))

# Distribusi Kelembaban
st.write("#### Distribusi Kelembaban")
st.pyplot(plot_dist('humidity', 'Distribusi Kelembaban'))

# Distribusi pH
st.write("#### Distribusi pH")
st.pyplot(plot_dist('ph', 'Distribusi pH'))

# Distribusi Curah Hujan
st.write("#### Distribusi Curah Hujan")
st.pyplot(plot_dist('rainfall', 'Distribusi Curah Hujan'))

# Footer
st.write("Dibuat oleh [Nama Anda]")
