import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv('data_bersih_day.csv')
hour_df = pd.read_csv('data_bersih_hour.csv')

st.title("Bike Sharing Data Analysis Dashboard :bicyclist:")
st.subheader("Analisis Data Penyewaan Sepeda")

# Sidebar for selecting analysis
analysis_type = st.sidebar.selectbox(
    "Choose Analysis",
    ("Perilaku Penyewaan Berdasarkan Tipe Pengguna", "Tren Penyewaan dari 2011 ke 2012")
)

# Conditional display of different analyses
if analysis_type == "Perilaku Penyewaan Berdasarkan Tipe Pengguna":
    st.header("Perbandingan Casual Users dan Registered Users")
    
    # Group data by holiday and workingday
    groupby_day_df = day_df.groupby(['holiday', 'workingday']).agg({
        'casual': 'mean',
        'registered': 'mean'
    }).reset_index()

    groupby_hour_df = hour_df.groupby(['holiday', 'workingday']).agg({
    'casual': 'mean',
    'registered': 'mean'
    }).reset_index()

    # Visualizing for casual users (day)
    st.subheader("Rata-rata Penyewaan Pengguna (Day)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=groupby_day_df, x='workingday', y='casual', hue='holiday', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda: Casual Users')
    ax.set_xlabel('Hari Kerja (0 = Tidak, 1 = Ya)')
    ax.set_ylabel('Rata-rata Penyewaan Kasual')
    st.pyplot(fig)
    
    # Visualizing for registered users (day)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=groupby_day_df, x='workingday', y='registered', hue='holiday', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda: Registered Users')
    ax.set_xlabel('Hari Kerja (0 = Tidak, 1 = Ya)')
    ax.set_ylabel('Rata-rata Penyewaan Terdaftar')
    st.pyplot(fig)

    # Visualizing for casual users (hour)
    st.subheader("Rata-rata Penyewaan Pengguna (Hour)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=groupby_hour_df, x='workingday', y='casual', hue='holiday', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda: Casual Users')
    ax.set_xlabel('Hari Kerja (0 = Tidak, 1 = Ya)')
    ax.set_ylabel('Rata-rata Penyewaan Kasual')
    st.pyplot(fig)
    
    # Visualizing for registered users (hour)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=groupby_hour_df, x='workingday', y='registered', hue='holiday', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda: Registered Users')
    ax.set_xlabel('Hari Kerja (0 = Tidak, 1 = Ya)')
    ax.set_ylabel('Rata-rata Penyewaan Terdaftar')
    st.pyplot(fig)

elif analysis_type == "Tren Penyewaan dari 2011 ke 2012":
    st.header("Tren Penyewaan Sepeda dari 2011 ke 2012")
    
    # Group data by year for the day data
    day_total_per_year = day_df.groupby('yr').agg({'cnt': 'sum'}).reset_index()
    hour_total_per_year = hour_df.groupby('yr').agg({'cnt': 'sum'}).reset_index()
    
    # Visualizing the trend (day)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=day_total_per_year, x='yr', y='cnt', marker='o', ax=ax)
    ax.set_title('Tren Penyewaan Sepeda dari Tahun 2011 ke 2012 (day)')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Total Penyewaan')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['2011', '2012'])
    st.pyplot(fig)

    # Visualizing the trend (hour)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=hour_total_per_year, x='yr', y='cnt', marker='o', ax=ax)
    ax.set_title('Tren Penyewaan Sepeda dari Tahun 2011 ke 2012 (hour)')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Total Penyewaan')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['2011', '2012'])
    st.pyplot(fig)