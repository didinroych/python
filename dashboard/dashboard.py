import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
import streamlit as st
from babel.numbers import format_currency 

# Import data yang sudah di siap pakai
df = pd.read_csv("main_data.csv")  

# Konversi kolom date ke dalam tipe data datetime
df["date"] = pd.to_datetime(df["date"])

#Function Filter by date
def filter_by_date(df):
    
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    
    date_range = st.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)

    filtered_df = df[(df["date"] >= pd.to_datetime(date_range[0])) & (df["date"] <= pd.to_datetime(date_range[1]))]

    return filtered_df

#function sum all order, not filtered
def all_bs(filtered_df):
    st.write("Seluruh Data Bike-Sharing") 
    # Menghitung total bike share untuk setiap jam
    aggregated_data = filtered_df.groupby(['hour'])['total'].sum().reset_index() 
    
    st.write("Plot Jumlah Total Bike Share")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=aggregated_data, x='hour', y='total')
    st.pyplot(plt)
    plt.close()

#function sum all bike sharing by season
def bike_share_byseason(filtered_df):
    st.write("Filter berdasarkan Season")
    
    # Menermia multiple choice
    season_filter = st.multiselect('Pilih Season', options=['Spring', 'Summer', 'Fall', 'Winter'], default=['Spring'])
    
    if not season_filter:
        st.write("Pilih minimal satu season")
        return
    
    plt.figure(figsize=(10, 5)) 

    # Loop setiap season terpilih
    for season in season_filter:
        filtered_day_df = filtered_df[filtered_df['season'] == season]
        aggregated_data = filtered_day_df.groupby(['hour'])['total'].sum().reset_index()
        plt.plot(aggregated_data['hour'], aggregated_data['total'], label=season)
 
    plt.title('Average Total Bike Sharing by Hour (Season)')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Share')
    plt.legend(title="Season")
 
    st.pyplot(plt)
    plt.close()



#function sum all bike sharing by weathersit
def bs_byweathersit(filtered_df): 
    st.write("Filter berdasarkan Kondisi Cuaca (Weathersit)")
    
    # Filter Weathersit
    weathersit_filter = st.multiselect('Pilih Kondisi Cuaca', options=['Clear/Cloudy', 'Misty/Cloudy', 'Light Precipitation', 'Severe Weather'],default=['Clear/Cloudy'])
    if not weathersit_filter:
        st.write("Pilih minimal satu Weathersit")
        return   

    plt.figure(figsize=(10, 5)) 

    # Loop setiap weathersit terpilih
    for weather in weathersit_filter:
        filtered_day_df = filtered_df[filtered_df['weathersit'] == weather]
        aggregated_data = filtered_day_df.groupby(['hour'])['total'].sum().reset_index()
        plt.plot(aggregated_data['hour'], aggregated_data['total'], label=weather)
 
    plt.title('Average Total Bike Sharing by Hour (Weathersit)')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Share')
    plt.legend(title="Season")
 
    st.pyplot(plt)
    plt.close()
"""

"""
# Function sum all bike sharing by Typeday with Bar Plot
def bs_byTypeDay_workingday(filtered_df):
    st.write("Filter berdasarkan Tipe Hari")

    # Ubah opsi menjadi 'Workingday' dan 'Non-workingday'
    workingday_filter = st.multiselect('Pilih Tipe Hari', options=['Workingday', 'Non-workingday'], default='Workingday')

    if not workingday_filter:
        st.write("Pilih minimal satu tipe hari")
        return

    plt.figure(figsize=(10, 5))

    # Loop setiap tipe hari terpilih
    for workingday in workingday_filter:
        # Map 'Workingday' ke 1 dan 'Non-workingday' ke 0
        if workingday == 'Workingday':
            filtered_day_df = filtered_df[filtered_df['workingday'] == 1]
        elif workingday == 'Non-workingday':
            filtered_day_df = filtered_df[filtered_df['workingday'] == 0]

        # Mengelompokkan data berdasarkan jam
        aggregated_data = filtered_day_df.groupby(['hour'])['total'].sum().reset_index()

        # Menggunakan bar plot untuk visualisasi
        sns.barplot(x='hour', y='total', data=aggregated_data, label=workingday)

    # Set judul dan label plot
    plt.title('Average Total Bike Sharing by Hour (Tipe Hari)')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Share')
    plt.legend(title="Tipe Hari")

    st.pyplot(plt)
    plt.close()

def bs_byTypeDay_holiday(filtered_df):
    st.write("Filter berdasarkan Tipe Hari")

    # Ubah opsi menjadi 'Workingday' dan 'Non-workingday'
    nf_day_filter = st.multiselect('Pilih Tipe Hari', options=['Holiday', 'Weekend'], default='Weekend')

    if not nf_day_filter:
        st.write("Pilih minimal satu tipe hari")
        return

    plt.figure(figsize=(10, 5))

    # Loop setiap tipe hari terpilih
    for nf_day in nf_day_filter:
        # Map 'Workingday' ke 1 dan 'Non-workingday' ke 0
        if nf_day == 'Holiday':
            filtered_day_df = filtered_df[filtered_df['holiday'] == 1]
        elif nf_day == 'Weekend':
            filtered_day_df = filtered_df[filtered_df['weekend'] == 1]

        # Mengelompokkan data berdasarkan jam
        aggregated_data = filtered_day_df.groupby(['hour'])['total'].sum().reset_index()

        # Menggunakan bar plot untuk visualisasi
        sns.barplot(x='hour', y='total', data=aggregated_data, label=nf_day)

    # Set judul dan label plot
    plt.title('Average Total Bike Sharing by Hour (Tipe Hari)')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Share')
    plt.legend(title="Tipe Hari")

    st.pyplot(plt)
    plt.close()



# Main app
st.title("Bike Sharing Analysis")
df_filtered = filter_by_date(df)

# Display visualizations based on filtered data

tab1, tab2, tab3, tab4= st.tabs(["Total","by Season", "by Weathersit","by Type day"])
with tab1:
    all_bs(df_filtered)
with tab2:
    bike_share_byseason(df_filtered)
with tab3:
    bs_byweathersit(df_filtered)
    
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        bs_byTypeDay_workingday(df_filtered)
 
    with col2:
        bs_byTypeDay_holiday(df_filtered)
