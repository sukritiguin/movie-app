import requests
from bs4 import BeautifulSoup
import re
import streamlit as st
from selenium import webdriver

from PIL import Image, ImageDraw, ImageFont



"""
def get_image_with_text(text):
    # create an image object
    img = Image.new("RGB", (500, 750), color="yellow")

    # create an ImageDraw object
    draw = ImageDraw.Draw(img)

    # create a font object
    font = ImageFont.truetype("arial.ttf", 36)

    # draw text on the image
    # text = "Hello, Duniya! "
    textwidth, textheight = draw.textsize(text, font)
    x = (500 - textwidth) / 2
    y = (750 - textheight) / 2
    draw.text((x, y), text, fill="black", font=font)
    return img

"""

# import random
# from PIL import Image, ImageDraw, ImageFont
#
# def get_image_with_text(text):
#     # create an image object
#     img = Image.new("RGB", (500, 750), color=get_random_color())
#
#     # create an ImageDraw object
#     draw = ImageDraw.Draw(img)
#
#     # create a font object
#     font = get_random_font(36)
#
#     # draw text on the image
#     textwidth, textheight = draw.textsize(text, font)
#     x = (500 - textwidth) / 2
#     y = (750 - textheight) / 2
#     draw.text((x, y), text, fill="black", font=font)
#     return img
#
# def get_random_color():
#     # return tuple(random.randint(0, 255) for _ in range(3))
#     offset = random.randint(0, 50)
#     base_color = get_random_color()
#     color_with_offset = tuple(min(c + offset, 255) for c in base_color)
#     return color_with_offset
#
# def get_random_font(size):
#     fonts = [
#         "arial.ttf",
#         "times.ttf",
#         "calibri.ttf",
#         "impact.ttf",
#         "georgia.ttf",
#         "verdana.ttf",
#         "comic.ttf",
#         "courier.ttf",
#         "roboto.ttf",
#         "futura.ttf"
#     ]
#     font_name = random.choice(fonts)
#     return ImageFont.truetype(font_name, size)






import random
from PIL import Image, ImageDraw, ImageFont

def get_image_with_text(text):
    width = 500
    height = 750
    # Available fonts provided by PIL
    available_fonts = [
        "arial.ttf",
        "arialbd.ttf",
        "arialbi.ttf",
        "ariali.ttf",
        "cour.ttf",
        "courbd.ttf",
        "courbi.ttf",
        "couri.ttf",
        "times.ttf",
        "timesbd.ttf",
        "timesbi.ttf",
        "timesi.ttf",
        "verdana.ttf",
        "verdanab.ttf",
        "verdanai.ttf",
        "verdanaz.ttf"
    ]

    # Randomly select font
    font_file = random.choice(available_fonts)
    font_size = 50

    # Randomly select background color
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a new image with the specified background color
    image = Image.new("RGB", (width, height), bg_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Add tiny repeated text in the background
    tiny_text = text
    tiny_font_size = 20
    tiny_font = ImageFont.truetype(font_file, tiny_font_size)
    tiny_text_width, tiny_text_height = draw.textsize(tiny_text, font=tiny_font)

    for i in range(0, width, tiny_text_width):
        for j in range(0, height, tiny_text_height):
            draw.text((i, j), tiny_text, font=tiny_font, fill=(255, 255, 255))

    # Split the text into words
    words = text.split()
    words_per_line = 2
    line_height = 60
    current_line = []

    # Calculate the position for the text with a random offset
    font = ImageFont.truetype(font_file, font_size)
    offset = random.uniform(0.2, 0.7)
    x = int(width * offset)
    y = (height - (len(words) // words_per_line) * line_height) // 2

    # Write the text on the image
    text_color = (0, 0, 0)  # Dark black color
    len_ = len(words)
    i = 0
    while i<len_:
        current_line.append(words[i])
        if len(current_line) == words_per_line or i==len_-1:
            line = " ".join(current_line)
            text_width, text_height = draw.textsize(line, font=font)
            draw.text((x - text_width // 2, y), line, font=font, fill=text_color)
            y += line_height
            current_line = []
        i += 1
    # Draw corner circles
    corner_colors = [
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ]
    corner_ellipse_colors = [
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ]

    circle_radius = random.randint(80, 160)
    half_circle_radius = circle_radius // 2
    circle_positions = [(0, 0), (0, height), (width, 0), (width, height)]
    for position, color, ellipsis_color in zip(circle_positions, corner_colors, corner_ellipse_colors):
        draw.ellipse((position[0] - circle_radius, position[1] - circle_radius,
                      position[0] + circle_radius, position[1] + circle_radius), fill=color)
        draw.ellipse((position[0] - half_circle_radius, position[1] - half_circle_radius,
                      position[0] + half_circle_radius, position[1] + half_circle_radius), fill=ellipsis_color)

    return image





def get_year_regx(s:str)->str:
    match = re.search(r'\d{4}', s)
    return match.group()

def get_soup(url):
    response = requests.get(url)
    doc = BeautifulSoup(response.content,"html.parser")
    return doc


def get_all_genres_pages_link():
    """
    url = "https://www.imdb.com/feature/genre"
    response = requests.get(url)
    doc = BeautifulSoup(response.content, "html.parser")
    filters_link = doc.find_all("div", class_="table-cell primary")
    genres_movies_lists = set()
    for filter_page in filters_link:
        genres_movies_lists.add("https://www.imdb.com" + filter_page.find("a")['href'])

    all_genres_links = set()
    for link in genres_movies_lists:
        if link.find("https://www.imdb.com/search/title?genres=") != -1:
            all_genres_links.add(link)

    final_genres_links = set()
    for link in all_genres_links:
        final_genres_links.add(link[:link.find("&")])

    all_genres_pages_link_list = list(final_genres_links)
    all_genres_pages_link_dict = dict()
    for link in all_genres_pages_link_list:
        temp = link.split("https://www.imdb.com/search/title?genres=")[1]
        all_genres_pages_link_dict[temp.capitalize()] = temp.lower()
    return all_genres_pages_link_dict
    """
    page_link_dict = {
        "Action" : "https://www.imdb.com/search/title/?genres=Action",
        "Adventure" : "https://www.imdb.com/search/title/?genres=Adventure",
        "Animation": "https://www.imdb.com/search/title/?genres=Animation",
        "Biography": "https://www.imdb.com/search/title/?genres=Biography",
        "Comedy": "https://www.imdb.com/search/title/?genres=Comedy",
        "Crime": "https://www.imdb.com/search/title/?genres=Crime",
        "Documentary": "https://www.imdb.com/search/title/?genres=Documentary",
        "Drama": "https://www.imdb.com/search/title/?genres=Drama",
        "Family": "https://www.imdb.com/search/title/?genres=Family",
        "Fantasy": "https://www.imdb.com/search/title/?genres=Fantasy",
        "History": "https://www.imdb.com/search/title/?genres=History",
        "Horror": "https://www.imdb.com/search/title/?genres=Horror",
        "Mystery": "https://www.imdb.com/search/title/?genres=Mystery",
        "Romance": "https://www.imdb.com/search/title/?genres=Romance",
        "Sci-Fi": "https://www.imdb.com/search/title/?genres=Sci-Fi",
        "War": "https://www.imdb.com/search/title/?genres=War",
        "Thriller": "https://www.imdb.com/search/title/?genres=Thriller",
        "Sport": "https://www.imdb.com/search/title/?genres=Sport",
    }
    return page_link_dict


def get_language_by_values():
    url = "https://www.imdb.com/search/title/"
    response = requests.get(url)
    doc = BeautifulSoup(response.content,"html.parser")
    options = doc.find("select",class_="languages").find_all("option")
    language_by_values = dict()
    for option in options:
        language_by_values[option.text] = option['value']
    return language_by_values


def get_country_code():
    url = "https://www.imdb.com/search/title"
    response = requests.get(url)
    doc = BeautifulSoup(response.content,"html.parser")
    options = doc.find("select",{"name":"countries"}).find_all("option")
    country_code_dict = dict()
    for option in options:
        country_code_dict[option.get_text()] = option['value']
    return country_code_dict

def get_poster_through_imdb_id(imdb_id):
    # Replace "API_KEY" with your own TMDb API key
    API_KEY = "3222076ed226933d3e1302ce9f3b73dc"

    # Build the TMDb API request URL
    url = "https://api.themoviedb.org/3/find/{}?api_key={}&external_source=imdb_id".format(imdb_id,API_KEY)

    # Send the request
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Check if there are any movies in the response
        if data.get("movie_results"):
            # Get the first movie in the response
            movie = data["movie_results"][0]

            # Get the movie poster path
            poster_path = movie["poster_path"]

            # Build the TMDb image URL
            poster_url = "https://image.tmdb.org/t/p/w500{}".format(poster_path)

            # Print the poster URL
            return poster_url if poster_url!=None else "https://image.tmdb.org/t/p/w500/example_poster.jpg"
    else:
        return  "https://image.tmdb.org/t/p/w500/example_poster.jpg"


def get_details_of_card(card):
    imdb_id = card.find("a")['href'].split("/title/")[1][:-1]
    middle_tag = card.find("div", class_="lister-item-content")
    muted_texts = card.find("div", class_="lister-item-content").find_all("p", class_="text-muted")
    text = card.find("div", class_="lister-item-content").find("p", class_="").get_text().replace("\n", "")
    movie_details = dict()
    movie_details["movie_poster"] = get_poster_through_imdb_id(imdb_id=imdb_id)

    try:
        movie_details["movie_title"] = middle_tag.find("h3").find("a").get_text()
    except:
        movie_details["movie_title"] = "NA"

    if movie_details['movie_poster'] == None:
        movie_details['movie_poster'] = get_image_with_text(text=movie_details['movie_title'])

    try:
        movie_details["movie_release_year"] = get_year_regx(
            middle_tag.find("h3").find("span", class_="lister-item-year").get_text())
    except:
        movie_details["movie_release_year"] = "NA"

    try:
        movie_details["movie_runtime"] = muted_texts[0].find("span", class_="runtime").get_text()
    except:
        movie_details["movie_runtime"] = "NA"

    try:
        movie_details["movie_genres"] = muted_texts[0].find("span", class_="genre").get_text().replace("\n",
                                                                                                       "").replace(" ",
                                                                                                                   "")
    except:
        movie_details["movie_genres"] = "NA"

    try:
        movie_details["movie_description"] = muted_texts[1].get_text().replace("\n", "")
    except:
        movie_details["movie_description"] = "NA"

    try:
        movie_details["movie_rating"] = card.find("div", class_="lister-item-content").find("div",
                                                                                            class_="ratings-bar").find(
            "strong").get_text()
    except:
        movie_details["movie_rating"] = "NA"

    try:
        movie_details["movie_votes"] = card.find("div", class_="lister-item-content").find("p",
                                                                                           "sort-num_votes-visible").get_text().replace(
            "\n", "")
    except:
        movie_details["movie_votes"] = "NA"
    movie_details["movie_stars"] = text[text.find("Stars"):]

    return movie_details


def get_next_page_url(temp, base_url):
    temp1 = temp.split("-")
    curr_start = int(temp1[0].replace(",", ""))
    temp2 = temp1[1].split("of")
    curr_end = int(temp2[0].replace(" ", "").replace(",", ""))
    total = int(re.sub(r'\D', "", temp2[1]))

    if curr_end == total:
        return None
    currURL = f"{base_url}&start={curr_end + 1}&ref_=adv_nxt"
    return currURL

def get_all_details(search_url,i=1):
    doc = get_soup(search_url)
    cards = doc.find_all("div",class_="lister-item mode-advanced")
    for card in cards:
        get_details_of_card(card)
    next_url = get_next_page_url(doc.find("div",class_="desc").find("span").get_text(),search_url)
    if next_url==None:return
    get_all_details(next_url,i)

def get_all_page_last_part(url):
    doc = get_soup(url)
    temp = doc.find("div",class_="desc").find("span").get_text()
    if temp.find("1-50") != -1:
        temp1 = temp.split(" of ")[1]
        total = int(re.sub(r'\D', "",temp1))
        start = 1
        last_part_dict = dict()
        while start<total:
            last_part_dict[f"{start} to {start+49}"] = start
            start += 50
        return last_part_dict
    # if total card is less than 50
    total = int(re.sub(r"\D","",temp))
    return {f"1-{total}":1}

def get_youtube_url(movie_name):
    # Replace "API_KEY" with your own YouTube Data API v3 key
    API_KEY = "AIzaSyBfhpgGvwb_8MHbGAE611kRsIpADjOffpA"

    # Replace "movie_name" with the actual name of the movie you want to search for
    # movie_name = "ballabhpurer roopkotha trailler"

    # Build the search request URL
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={} trailer&key={}".format(movie_name, API_KEY)

    # Send the search request
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Check if there are any videos in the response
        if data.get("items"):
            # Get the first video in the response
            video = data["items"][0]

            # Get the video ID
            video_id = video["id"]["videoId"]

            # Build the YouTube video player URL
            video_url = "https://www.youtube.com/watch?v={}".format(video_id)

            # Print the video URL
            # print("Video URL:", video_url)
            return video_url
    else:
        # Print an error message
        # print("Failed to search for video:", response.text)
        return "https://www.youtube.com"


def get_youtube_trailler(movie_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(f"https://www.youtube.com/results?search_query={movie_name + 'trailer'}")

    html_content = browser.page_source
    soup = BeautifulSoup(html_content, "html.parser")

    video_element = soup.find("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")['href']

    return "https://www.youtube.com/" + video_element



def show_card(card_html):
    left, right = st.columns(2)
    card_dict = get_details_of_card((card_html))
    with left:
        if card_dict["movie_poster"]:
            st.image(card_dict["movie_poster"])
        else:
            st.error("Could not load image")
    with right:
        st.subheader(card_dict["movie_title"] + f" ({card_dict['movie_release_year']})")
        st.markdown("##### Runtime : " + card_dict['movie_runtime'])
        st.markdown("##### Rating : " + card_dict['movie_rating'])
        st.markdown("##### " + card_dict['movie_votes'])
        st.markdown("**Movie Starts :** " + card_dict['movie_stars'])
        st.markdown("**Description :** " + card_dict['movie_description'])
        st.markdown(
            f"""
            <a href="{get_youtube_trailler(movie_name=card_dict['movie_title'])}" style="padding: 8px 12px; background-color: blue; color: white; border-radius: 4px; text-decoration: none;">Watch Trailer</a>
            """,
            unsafe_allow_html=True,
        )