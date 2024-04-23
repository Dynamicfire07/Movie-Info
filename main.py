import requests
import streamlit as st



# Author: Dynamic_fire07 aka Shaurya Jain
# This was built in a day
# Adviced not to be copy this code

API_KEY = "35a1ef28"

try:
    movie = st.text_input("Enter a movie")
    response = requests.get(f"http://www.omdbapi.com/?t={movie}&apikey=35a1ef28")
    text = response.json()
    print(text["Title"])
    st.title(text["Title"])
    st.image(text["Poster"])
    st.subheader(f"Year: {text['Year']}")
    st.subheader(f"Runtime: {text['Runtime']}")
    st.subheader(f"Released on: {text['Released']}")
    st.subheader(f"Genre: {text['Genre']}")
    st.info(f"Plot: {text['Plot']}")
    st.subheader(f"Actors: {text['Actors']}")
    st.subheader(f"Director: {text['Director']}")
    st.subheader(f"Language: {text['Language']}")
    st.subheader(f"BoxOffice: {text['BoxOffice']}")
    st.info(f"Rating: {text['Ratings'][0]['Value']}")
    st.info(f"Rating 2: {text['Ratings'][1]['Value']}")
except KeyError:
    "Movie not found!"
