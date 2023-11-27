import streamlit as st
import pandas as pd
import plotly.express as px

# Fungsi untuk Memuat Data
@st.cache
def load_data():
    data = pd.read_csv('sf.csv')
    return data

# Memuat Data
data = load_data()

# Judul Aplikasi
st.title('Optimasi Pertumbuhan Tanaman: Analisis Kondisi Lingkungan')

# Menampilkan Data dan Penjelasan
st.write("### Data Mentah")
st.dataframe(data.head())

st.write("### Penjelasan Data")
# Tambahkan penjelasan data Anda di sini

# Pilihan Kolom untuk Visualisasi
col_options = list(data.columns)
selected_col = st.selectbox('Pilih Kolom untuk Visualisasi', col_options)

# Slider untuk Jumlah Bins
bins = st.slider('Pilih Jumlah Bins', min_value=10, max_value=100, value=30)

# Fungsi untuk Membuat Plot dengan Plotly
def plot_dist_plotly(column, bins):
    fig = px.histogram(data, x=column, nbins=bins, title=f'Distribusi {column}')
    fig.update_layout(bargap=0.1)
    return fig

# Visualisasi Data dengan Plotly
st.write("### Visualisasi Data")
st.plotly_chart(plot_dist_plotly(selected_col, bins))

# Footer
st.write("Dibuat oleh [Nama Anda]")
