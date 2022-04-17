import streamlit as st
import pickle
import pandas as pd
st.title('Anime Recommender System')


def recommend(anime):
    anime_index = animes[animes['title'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_animes = []

    for i in anime_list:
        recommended_animes.append(animes.iloc[i[0]].title)
    return recommended_animes


anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
animes = pd.DataFrame(anime_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
selected_anime = st.selectbox(
     'Choose any anime you like:',
     animes['title'].values)

st.write('You selected:', selected_anime)

if st.button('Recommend'):
    recommendations = recommend(selected_anime)
    for i in recommendations:
        st.write(i)
else:
    st.write('Hello Otakus! you will get your recommendations here.....')
