import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="FilmAdatbázis")
st.title("🎬 Saját Filmnaplóm")

BACKEND_URL = "https://mpny.onrender.com/movies"

with st.sidebar:
    st.header("Új film rögzítése")
    with st.form("movie_form"):
        title = st.text_input("Film címe")
        genre = st.selectbox("Műfaj", ["Akció", "Vígjáték", "Dráma", "Sci-fi", "Horror", "Dokumentum"])
        submit = st.form_submit_button("Mentés")
        
        if submit and title:
            try:
                requests.post(BACKEND_URL, json={"title": title, "genre": genre})
                st.success(f"'{title}' elmentve!")
            except:
                st.error("Hiba: A backend nem elérhető!")

try:
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.subheader("Rögzített filmek")
            st.dataframe(df[['title', 'genre']], use_container_width=True)
            
            st.subheader("Műfaji eloszlás")
            st.bar_chart(df['genre'].value_counts())
        else:
            st.info("Még nincs mentett filmed.")
except:

    st.warning("Csatlakoztasd a backendet az adatok látványához.")
