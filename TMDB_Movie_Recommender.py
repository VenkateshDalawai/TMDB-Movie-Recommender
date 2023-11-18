import streamlit as st
import pickle

movies=pickle.load(open("tmdb_new_dataset.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
st.title("TMDB Movie Recommendation System")
names=movies['original_title'].values

def recommend(movie):
    movie_index=movies[movies['original_title']==movie].index[0]#gives the index of the movie name
    distance=similarity[movie_index]#gives the simililar movie index
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda vector:vector[1])[1:6]#give the top 5 matched movie index
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies

selected_name=st.selectbox("select from the drop menu",names)
print(selected_name)

if st.button("Show Recommend"):
    movies_list=recommend(selected_name)
    for i in movies_list:
        st.text(i)

