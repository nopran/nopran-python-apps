import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title('Optimasi Pertumbuhan Tanaman: Analisis Kondisi Lingkungan')

# Memuat Data
@st.cache  # Cache the data for faster loading
def load_data():
    data = pd.read_csv('sf.csv')  # Ganti dengan path ke file CSV Anda
    return data

data = load_data()

# Menampilkan Data Mentah
st.write("### Data Mentah")
st.dataframe(data.head())

# Penjelasan Data
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

# Fungsi untuk Membuat Plot
def plot_dist(column, title):
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True, bins=30, ax=ax)
    plt.title(title)
    return fig

# Visualisasi Data
st.write("### Visualisasi Data")

# Suhu
st.write("#### Distribusi Suhu")
st.pyplot(plot_dist('temperature', 'Distribusi Suhu'))

# Kelembaban
st.write("#### Distribusi Kelembaban")
st.pyplot(plot_dist('humidity', 'Distribusi Kelembaban'))

# pH
st.write("#### Distribusi pH")
st.pyplot(plot_dist('ph', 'Distribusi pH'))

# Curah Hujan
st.write("#### Distribusi Curah Hujan")
st.pyplot(plot_dist('rainfall', 'Distribusi Curah Hujan'))

# Footer
st.write("Dibuat oleh [Nama Anda]")
