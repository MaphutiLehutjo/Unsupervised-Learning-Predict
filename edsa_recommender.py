"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Welcome", "Team", "Data Collection", "EDA", "Modelling","Reviews"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------
    if page_selection == "Welcome":
        st.header("Welcome to Movie Recommender")

        st.image('./resources/imgs/Movie_night.jpeg', use_column_width=True)

        st.markdown("Are you a movie lover? Are you tired of wasting your time watching tons of trailers and ending up not watching their movies? Are you tired of finishing your popcorns before you find the right movie? That has come to an end!!")
        about = st.sidebar.checkbox("About")
        if about:

            st.subheader("**Problem Statement**")
            st.markdown("Recommender systems became a useful feature due to the growth of online streaming apps.\
                        There are a lot of things available online,\
                        and many users have a hard time not only finding something they want but even figuring out what it is that they want based on their mood.\
                        So,the recommender system is a delicate way of bringing users and relevant content together.\
                        In this case we are mainly focused on movies,\
                        Imagine after a long day at work and feeling like relaxing to your time favourite movie,or eating your favourite dinner while scrolling and wanting a movie to go with that.\
                         What the recommendation system does is narrowing the selection of specific content to the one that is the most relevant to the particular user.")

            st.subheader("**Overview**")
            st.markdown("How The App works? The Movie Recommender App filters or predicts your preferences based on your favourite or watched movie selections. With just a few clicks, you will select three of your most favourite movies from thousands of movies on the app and you will get top 10 movies you are most likely to enjoy. You have an option to view some data visualizations including word clouds that show the most popular words that appear in movie titles and plots on the most popular genres. The app also contains a contact page, where users of the app can rate our app and give feedback and suggestions.")
    

    if page_selection == "Team":
        st.header("Meet The Team")

        st.subheader("**TECHIQ SOLUTIONS**")

        st.image('./resources/imgs/R.jpeg',use_column_width=True)
        st.markdown("* Ramabopa Mahlatsi - Team Coordinator")
        st.markdown("* Lehutjo Maphuti")
        st.markdown("* Buthelezi Mandisa")
        st.markdown("* Mosibi Mosuwe")
        st.markdown("* Mzilikazi Nobuntu")

    if page_selection == "Data Collection":
        st.header("Data used")
        st.subheader("Where did we get the data?")
        st.image('./resources/imgs/SD.jpeg', use_column_width=True)
        st.markdown("The data was obtained from MovieLens \
            which has the several millions 5-star ratings obtained from users using the online streaming recommendation system.\
            The IMBD (imbd_df) was legally scraped from IMDB.")

        look = st.sidebar.checkbox("Data")
        if look:
            st.subheader("What did the data consist of?")
            st.markdown("* Movies -Movie titles are entered manually or imported from https://www.themoviedb.org/, and include the year of release in parentheses")
            st.markdown("* Genome_scores - is a score mapping the strength between movies and tag-related properties.")
            st.markdown("* Genome_tags - User assigned for the movies within the dataset.")
            st.markdown("* Imdb - Additional movie metadata scraped from IMDB using the links.csv file.")
            st.markdown("* Links - File providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs.")
            st.markdown("* Train - The training split of the dataset. Contains user and movie IDs with associated rating data.")
    
    if page_selection =="EDA":
        st.header("Exploratory Data Analysis")
        st.write("This process will be referred to as Exploratory Data Analysis or EDA. \
        The reason we explore the data is to gain insight on the data and how it behaves. Exploratory data analysis (EDA) is a term for certain kinds of initial analysis and findings done with data sets, usually early on in an analytical process. \
        Some experts describe it as “taking a peek” at the data to understand more about what it represents and how to apply it.")

        st.subheader("Most common genres")
        st.image('./resources/imgs/E.jpeg', use_column_width=True)
        st.markdown("The graph above shows that the most common genres are drama, comedy, thriller, etc.\
            People love drama movies more than any other genre therefore more of those should always form part of a user's recommendation.\
            Children and animation genres are equally common and this could be attributed to the fact that most children's movies are animated.")
        
        st.subheader('Ratings per viewer')
        st.image('./resources/imgs/D.jpeg',use_column_width=True)
        st.markdown("The bar graph above shows the number of times users have made ratings. \
            About 20 000 users have only rated movies less than 10 times while more than 100 000 have rated more than 10 times. \
            There are super rators, such as userID 72315 that have made more than 10 000 ratings.\
            Insight drawn from this graph is that a lot of people do rate movies therefore a recommender system is worth the investment.")

        source = st.sidebar.checkbox("Distribution of ratings")
        if source:
            st.subheader('Percentage of users per rating')
            st.image('./resources/imgs/C.jpeg', use_column_width=True)
            st.subheader('Ratings distribution')
            st.image('./resources/imgs/B.jpeg', use_column_width=True)
            st.markdown("The train distribution shows that there are relatively fewer movies that are lower rated.\
            This can be because most of the users who didn't like the movie, didn't care enough to rate the movie. \
            You should note this, it can be useful later.\
             As you wouldn't want to recommend movies with relatively low number of ratings as users probably didn't like them.\
            4 Star ratings make up the largest portion of ratings in the MovieLens dataset, accounting for 26.5% of the overall ratings. \
            5 star ratings make up 14.5% of the overall ratings (3rd largest portion). \
            0.5 star ratings account for the smallest portion of the ratings at a mere 1.6%. Ratings between 2 and 0.5 stars account for 12.9%")


        source = st.sidebar.checkbox("Movie Titles")
        if source:
            st.subheader('Most Frequent words in titles')
            st.image('./resources/imgs/H.jpeg', use_column_width=True)
            st.markdown("The visual above shows which words are commonly used when movies are titled. \
            The bigger the word, the more it is being used.\
            As can be seen, the word love, Man, and Girl appears the most.")

    if page_selection == "Modelling":
        st.header("Modelling")
        st.subheader("Content-based Filtering")
        st.image('./resources/imgs/JJJ.jpeg', use_column_width=True)
        st.markdown('Uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.')

        st.subheader("Colloboration-based filtering")
        st.markdown('builds a model from your past behavior (i.e. movies watched or selected by the you) as well as similar decisions made by other users.')
        st.image('./resources/imgs/SS.jpeg', use_column_width=True)
        st.markdown('The SVD and BaselineOnly algorithm gave us the best RMSE score, but SVD has a higher training time, therefore, we will train and predict with BaselineOnly. \
        We also decided to use collaborative model because of the cold-start problem. \
        The cold-start problem, which describes the difficulty of making recommendations when the users or the items are new, remains a great challenge for collaborative filtering. \
        We ultimately chose the BaselineOnly model based on the RMSE metric as well as the runtime.')



    if page_selection =="Reviews":
        st.header("Get in touch with us")
        st.markdown('''<span style="color:blue"> **Help us improve this app by rating it. Tell us how to give you a better user experience.** </span>''', unsafe_allow_html=True)
        @st.cache(allow_output_mutation=True)
        def get_data():
            return []
        name = st.text_input("User name")
        inputs = st.text_input("Let us improve your user experience!!!")
        rate = st.slider("Rate us", 0, 5)
        if st.button("Submit"):
            get_data().append({"User name": name, "Suggestion": inputs,"rating":rate})
        #st.markdown('''<span style="color:blue"> **What other users said:** </span>''', unsafe_allow_html=True)
        #st.write(pd.DataFrame(get_data()))
        st.markdown('''<span style="color:blue"> **For any questions contact us here:** </span>''', unsafe_allow_html=True)
        st.markdown('techiqdigitalsolutions@reviews.com')


    


    



    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
