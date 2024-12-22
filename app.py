
backgroundColor="#FFFFFF"

import streamlit as st
import pandas as pd
import pickle


st.title('Movie Recommender System')

movies = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl','rb'))

def similar_movies(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    #To preserve index position after sorting, using enumerate
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    similar = []
    for i in movies_list:
        similar.append(movies.iloc[i[0]]['title'])
    return similar

movie_like = st.selectbox('Movies Like?',movies['title'].values)

if st.button('Recommend'):
    recommended = similar_movies(movie_like)
    for i in recommended:
        st.write(i)