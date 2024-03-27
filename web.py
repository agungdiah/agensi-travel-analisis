import streamlit as st
import pickle 
import pandas as pd

def recommend(tourism, tourism_data):
    recommend_index = tourism_data[tourism_data["Place_Name"] == tourism].index[0]
    recommended_list = tourism_data.iloc[recommend_index, 0:3].values.tolist()
    return recommended_list

st.title("Sistem Rekomendasi Tempat Wisata di Yogyakarta")
st.write("memudahkan kalian untuk menemukan tempat wisata yang memiliki kesamaan dengan tempat favorit yang dipilih!")

tourism_dict = pickle.load(open("tourism_dict.pkl", "rb"))
tourism_data = pd.DataFrame(tourism_dict)

tourism_places = tourism_data["Place_Name"].values
selected_tourism_places = st.selectbox("Pilih Tempat Wisata", tourism_places)

if st.button('Rekomendasi'):
    recommendations = recommend(selected_tourism_places, tourism_data)
    for place in recommendations:
        st.write(place)