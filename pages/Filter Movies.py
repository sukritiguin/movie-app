import streamlit as st
from functions import filter_df,list_to_strURL, get_card, get_total_pages, print_filter_cards_from_pages
import ast
import requests
from bs4 import BeautifulSoup


release_dict = filter_df['Release'].values[0]
release_dict = ast.literal_eval(release_dict)
genres_dict = filter_df["Genre"].values[0]
genres_dict = ast.literal_eval(genres_dict)
country_dict = filter_df["Country"].values[0]
country_dict = ast.literal_eval(country_dict)




release_button = st.radio(label="Select Release Year",options=release_dict.keys(),index=1,horizontal=True)
genre_button = st.multiselect(label="Select Genres",options=genres_dict.keys())
country_button = st.multiselect(label="Select Couries",options=country_dict.keys())

genre_url_sorted = list_to_strURL(genres_dict,genre_button)
country_url_sorted = list_to_strURL(country_dict,country_button)
# movie_url = f"https://myflixer.to/filter?type=movie&quality=all&release_year={release_dict[release_button]}&genre={genre_url_sorted}&country={country_url_sorted}"
# st.write(movie_url)

movie_url = f"https://myflixer.to/filter?type=movie&quality=all&release_year={release_dict[release_button]}"
if genre_button:
        movie_url += f"&genre={genre_url_sorted}"
else:
        movie_url += "&genre=all"
if country_button:
        movie_url += f"&country={country_url_sorted}"
else:
        movie_url += "&country=all"
# st.write(movie_url)


# needed_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}




while True:
        indicator = True
        try:
                response = requests.get(movie_url,timeout=5.0)
        except:
                indicator = False
                continue
        if indicator:break


doc = BeautifulSoup(response.content, 'html.parser')
total_pages = get_total_pages(doc)

if total_pages==0:
        print_filter_cards_from_pages(movie_url)
else:
        for i in range(1,total_pages+1,1):
                url = movie_url + f"&page={i}"
                print_filter_cards_from_pages(url)