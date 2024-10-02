import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Membuat dataframe
def create_daily_user_df(df):
    
    daily_user_df = df.resample(rule='D', on='dteday').agg({
        "casual": "sum",          
        "registered": "sum"       
    })

    daily_user_df = daily_user_df.reset_index()

    return daily_user_df


# Kode untuk membuat Filter (Kalender)

all_df = pd.read_csv("day_df.csv")
new_hour_df = pd.read_csv("new_hour_df.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Kode untuk membuat Sidebar

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_day_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

main_hour_df = new_hour_df[(new_hour_df["dteday"] >= str(start_date)) & 
                (new_hour_df["dteday"] <= str(end_date))]

daily_user_df = create_daily_user_df(main_day_df)

# Kode untuk Main Dashboard

# Membuat header dashboard
st.header('Bike Sharing Dashboard :bike:')
st.text("By: Mochammad Aurich Ilham Wicaksono")

# st.dataframe(daily_user_df)

st.subheader("Pattern Peminjaman Sepeda oleh Pengguna 'Casual' dan Pengguna 'Registered'")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_user_df["dteday"],
    daily_user_df["casual"],
    marker='o', 
    linewidth=2,
    color="#90CAF9",
    label = 'Casual User'
)
ax.plot(
    daily_user_df["dteday"],
    daily_user_df["registered"],
    marker='o', 
    linewidth=2,
    color="#A5D6A7",
    label = 'Registered User'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.legend(fontsize=15,)
 
st.pyplot(fig)

# Subheader 2
st.subheader("Hubungan Komponen Cuaca terhadap Rata-rata Total Penyewaan Sepeda pada masing-masing Musim")
tab1, tab2, tab3, tab4 = st.tabs(["Temp", "Atemp", "Hum", "Windspeed"])
 
with tab1:
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(35, 30))
    
    colors = ["#42A5F5", "#66BB6A", "#FFA726", "#AB47BC"] 
    
    sns.scatterplot(x="temp", y="cnt", data=main_day_df[main_day_df['season']==1], color=colors[0], s=100, ax=ax[0,0])
    sns.regplot(x="temp", y='cnt', data=main_day_df[main_day_df['season']==1], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,0])
    ax[0,0].set_title("Spring", fontsize =40)
    ax[0,0].tick_params(axis='y', labelsize=25)
    ax[0,0].tick_params(axis='x', labelsize=25)
    ax[0,0].set_xlabel("Temp", fontsize=30)
    
    sns.scatterplot(x="temp", y="cnt", data=main_day_df[main_day_df['season']==2], color=colors[1], s=100, ax=ax[0,1])
    sns.regplot(x="temp", y='cnt', data=main_day_df[main_day_df['season']==2], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,1])
    ax[0,1].set_title("Summer", fontsize =40)
    ax[0,1].tick_params(axis='y', labelsize=25)
    ax[0,1].tick_params(axis='x', labelsize=25)
    ax[0,1].set_xlabel("Temp", fontsize=30)

    sns.scatterplot(x="temp", y="cnt", data=main_day_df[main_day_df['season']==3], color=colors[2], s=100, ax=ax[1,0])
    sns.regplot(x="temp", y='cnt', data=main_day_df[main_day_df['season']==3], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,0])
    ax[1,0].set_title("Fall", fontsize =40)
    ax[1,0].tick_params(axis='y', labelsize=25)
    ax[1,0].tick_params(axis='x', labelsize=25)
    ax[1,0].set_xlabel("Temp", fontsize=30)

    sns.scatterplot(x="temp", y="cnt", data=main_day_df[main_day_df['season']==4], color=colors[3], s=100, ax=ax[1,1])
    sns.regplot(x="temp", y='cnt', data=main_day_df[main_day_df['season']==4], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,1])
    ax[1,1].set_title("Winter", fontsize =40)
    ax[1,1].tick_params(axis='y', labelsize=25)
    ax[1,1].tick_params(axis='x', labelsize=25)
    ax[1,1].set_xlabel("Temp", fontsize=30)

    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(35, 30))
    
    colors = ["#42A5F5", "#66BB6A", "#FFA726", "#AB47BC"] 
    
    sns.scatterplot(x="atemp", y="cnt", data=main_day_df[main_day_df['season']==1], color=colors[0], s=100, ax=ax[0,0])
    sns.regplot(x="atemp", y='cnt', data=main_day_df[main_day_df['season']==1], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,0])
    ax[0,0].set_title("Spring", fontsize =40)
    ax[0,0].tick_params(axis='y', labelsize=25)
    ax[0,0].tick_params(axis='x', labelsize=25)
    ax[0,0].set_xlabel("Atemp", fontsize=30)
    
    sns.scatterplot(x="atemp", y="cnt", data=main_day_df[main_day_df['season']==2], color=colors[1], s=100, ax=ax[0,1])
    sns.regplot(x="atemp", y='cnt', data=main_day_df[main_day_df['season']==2], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,1])
    ax[0,1].set_title("Summer", fontsize =40)
    ax[0,1].tick_params(axis='y', labelsize=25)
    ax[0,1].tick_params(axis='x', labelsize=25)
    ax[0,1].set_xlabel("Atemp", fontsize=30)

    sns.scatterplot(x="atemp", y="cnt", data=main_day_df[main_day_df['season']==3], color=colors[2], s=100, ax=ax[1,0])
    sns.regplot(x="atemp", y='cnt', data=main_day_df[main_day_df['season']==3], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,0])
    ax[1,0].set_title("Fall", fontsize =40)
    ax[1,0].tick_params(axis='y', labelsize=25)
    ax[1,0].tick_params(axis='x', labelsize=25)
    ax[1,0].set_xlabel("Atemp", fontsize=30)

    sns.scatterplot(x="atemp", y="cnt", data=main_day_df[main_day_df['season']==4], color=colors[3], s=100, ax=ax[1,1])
    sns.regplot(x="atemp", y='cnt', data=main_day_df[main_day_df['season']==4], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,1])
    ax[1,1].set_title("Winter", fontsize =40)
    ax[1,1].tick_params(axis='y', labelsize=25)
    ax[1,1].tick_params(axis='x', labelsize=25)
    ax[1,1].set_xlabel("Atemp", fontsize=30)

    st.pyplot(fig)
 
with tab3:
    
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(35, 30))
    
    colors = ["#42A5F5", "#66BB6A", "#FFA726", "#AB47BC"] 
    
    sns.scatterplot(x="hum", y="cnt", data=main_day_df[main_day_df['season']==1], color=colors[0], s=100, ax=ax[0,0])
    sns.regplot(x="hum", y='cnt', data=main_day_df[main_day_df['season']==1], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,0])
    ax[0,0].set_title("Spring", fontsize =40)
    ax[0,0].tick_params(axis='y', labelsize=25)
    ax[0,0].tick_params(axis='x', labelsize=25)
    ax[0,0].set_xlabel("Hum", fontsize=30)
    
    sns.scatterplot(x="hum", y="cnt", data=main_day_df[main_day_df['season']==2], color=colors[1], s=100, ax=ax[0,1])
    sns.regplot(x="hum", y='cnt', data=main_day_df[main_day_df['season']==2], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,1])
    ax[0,1].set_title("Summer", fontsize =40)
    ax[0,1].tick_params(axis='y', labelsize=25)
    ax[0,1].tick_params(axis='x', labelsize=25)
    ax[0,1].set_xlabel("Hum", fontsize=30)

    sns.scatterplot(x="hum", y="cnt", data=main_day_df[main_day_df['season']==3], color=colors[2], s=100, ax=ax[1,0])
    sns.regplot(x="hum", y='cnt', data=main_day_df[main_day_df['season']==3], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,0])
    ax[1,0].set_title("Fall", fontsize =40)
    ax[1,0].tick_params(axis='y', labelsize=25)
    ax[1,0].tick_params(axis='x', labelsize=25)
    ax[1,0].set_xlabel("Hum", fontsize=30)

    sns.scatterplot(x="hum", y="cnt", data=main_day_df[main_day_df['season']==4], color=colors[3], s=100, ax=ax[1,1])
    sns.regplot(x="hum", y='cnt', data=main_day_df[main_day_df['season']==4], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,1])
    ax[1,1].set_title("Winter", fontsize =40)
    ax[1,1].tick_params(axis='y', labelsize=25)
    ax[1,1].tick_params(axis='x', labelsize=25)
    ax[1,1].set_xlabel("Hum", fontsize=30)

    st.pyplot(fig)

with tab4:
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(35, 30))
    
    colors = ["#42A5F5", "#66BB6A", "#FFA726", "#AB47BC"] 
    
    sns.scatterplot(x="windspeed", y="cnt", data=main_day_df[main_day_df['season']==1], color=colors[0], s=100, ax=ax[0,0])
    sns.regplot(x="windspeed", y='cnt', data=main_day_df[main_day_df['season']==1], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,0])
    ax[0,0].set_title("Spring", fontsize =40)
    ax[0,0].tick_params(axis='y', labelsize=25)
    ax[0,0].tick_params(axis='x', labelsize=25)
    ax[0,0].set_xlabel("Windspeed", fontsize=30)
    
    sns.scatterplot(x="windspeed", y="cnt", data=main_day_df[main_day_df['season']==2], color=colors[1], s=100, ax=ax[0,1])
    sns.regplot(x="windspeed", y='cnt', data=main_day_df[main_day_df['season']==2], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[0,1])
    ax[0,1].set_title("Summer", fontsize =40)
    ax[0,1].tick_params(axis='y', labelsize=25)
    ax[0,1].tick_params(axis='x', labelsize=25)
    ax[0,1].set_xlabel("Windspeed", fontsize=30)

    sns.scatterplot(x="windspeed", y="cnt", data=main_day_df[main_day_df['season']==3], color=colors[2], s=100, ax=ax[1,0])
    sns.regplot(x="windspeed", y='cnt', data=main_day_df[main_day_df['season']==3], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,0])
    ax[1,0].set_title("Fall", fontsize =40)
    ax[1,0].tick_params(axis='y', labelsize=25)
    ax[1,0].tick_params(axis='x', labelsize=25)
    ax[1,0].set_xlabel("Windspeed", fontsize=30)

    sns.scatterplot(x="windspeed", y="cnt", data=main_day_df[main_day_df['season']==4], color=colors[3], s=100, ax=ax[1,1])
    sns.regplot(x="windspeed", y='cnt', data=main_day_df[main_day_df['season']==4], scatter=False, color='red', line_kws={'label': 'Garis Regresi'}, ax=ax[1,1])
    ax[1,1].set_title("Winter", fontsize =40)
    ax[1,1].tick_params(axis='y', labelsize=25)
    ax[1,1].tick_params(axis='x', labelsize=25)
    ax[1,1].set_xlabel("Windspeed", fontsize=30)

    st.pyplot(fig)


# Subheader 3
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam untuk masing-masing Hari")

fig, ax = plt.subplots(figsize=(16, 8))

def get_hari(num_of_weekday):
    
    hari_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if 0 <= num_of_weekday < len(hari_list):
        return hari_list[num_of_weekday]
    else:
        return "Invalid weekday number"

for weekday in new_hour_df['weekday'].unique():
  cnt_in_hour_weekday = main_hour_df[main_hour_df['weekday'] == weekday].groupby('hr')['cnt'].mean()
  plt.plot(cnt_in_hour_weekday.index, cnt_in_hour_weekday.values, label=f"{get_hari(weekday)}", marker='o')

plt.xlabel('Hour of the Day')
plt.ylabel('Rata-rata Bike Rental Count')
plt.title('Rata-rata Bike Rental Count berdasarkan Hour for Each Weekday')
plt.legend()
plt.grid(True)
plt.show()

st.pyplot(fig)

# Subheader 4
st.subheader("Rata-rata Total Penyewa Sepeda di Masing-masing Rush Hour Group")
st.text("Keterangan: \n - Weekday : Senin - Jumat (Rush Hour: 07:00 - 09:00 & 16:00 - 18:00)\n - Weekend : Sabtu - Minggu (Rush Hour: 10:00 - 18:00)")
fig, ax = plt.subplots(figsize=(16, 8))

colors = ["#FFB74D", "#FFE082", "#42A5F5", "#90CAF9"]

sns.barplot(x='rush_hour_group', y='cnt', data=main_hour_df, palette=colors )
plt.xlabel('Rush Hour Group')
plt.ylabel('Rata-rata Total Penyewaan Sepeda (cnt)')
plt.title('Rata-taya total penyewaan sepeda berdasarkan Rush Hour Group')
plt.grid(True)
plt.show()

st.pyplot(fig)

# st.dataframe(all_df)