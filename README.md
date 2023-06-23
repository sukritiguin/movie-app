# Movie Recommendation System - Release Documentation
## Introduction
The Movie Recommendation System is a sophisticated software application designed to provide users with personalized movie recommendations based on their preferences and selected movies. This release documentation outlines the key features, updates, bug fixes, and known issues associated with the latest version of the system.

## Release Information
**Version:** 1.0.0

**Release Date:** June 23, 2023

## Download Pre-trained ML Models

This project utilizes two large machine learning models for its functionality. Due to their size, these models are not included in the GitHub repository. However, you can download them separately from the following location:

Download ML Models
Please follow these steps to integrate the models into the project:

- [Click](https://drive.google.com/drive/folders/1xTcCzSc-J-6G2w0K8pNRx91xSF8LfOQO?usp=sharing) on the provided link to access the Google Drive folder containing the models.

- Once the folder opens, locate the ML models and download them to your local machine.

- Extract the downloaded files if they are in a compressed format (e.g., ZIP or RAR).

- Navigate to the project's data folder in your local repository.

- Move the extracted ML model files to the data folder.

By following these instructions, you will have successfully obtained the necessary ML models for the project and placed them in the appropriate data folder. This ensures that the recommendation system and other components relying on these models can function correctly.

## Features and Enhancements

**Improved Recommendation Algorithm:** The recommendation algorithm has been enhanced to provide more accurate and relevant movie suggestions based on user-selected movies. The system now considers genre, rating, cast, and user reviews to generate high-quality recommendations.

**Enhanced User Interface:** The user interface has undergone significant improvements to enhance usability and provide a seamless user experience. The layout is optimized for different screen sizes and devices, ensuring consistency and visual appeal.

**Detailed Movie Information:** The system now displays comprehensive details about each movie, including the movie poster, title, tagline, genres, rating, votes, release date, and duration. Users can access essential information to make informed decisions.

**OTT Platform Availability:** Users can check the availability of movies on various over-the-top (OTT) platforms. The system provides information about the platforms where the selected movie can be streamed, allowing convenient access to preferred content providers.

**Text-to-Speech Movie Overviews:** Users can listen to movie overviews using text-to-speech technology. By clicking the "Overview" button, users can enjoy a spoken description of the movie, enhancing accessibility and providing an alternative way to consume information.

**Top Cast Information:** The system displays information about the top casts of each movie, including their names, characters, and profile images. Users can gain insights into key actors and actresses involved in a movie, enhancing their understanding and appreciation.

**Popular Movies of Casts:** Users can explore popular movies featuring the top casts of a selected movie. By scrolling through the list, users can discover other notable films in which the cast members have appeared, providing a convenient way to explore related content.

**Sentiment Analysis of User Reviews:** The system performs sentiment analysis on user reviews for each movie. Positive reviews are marked with a green checkmark, while negative reviews are marked with a red cross. This feature assists users in gauging public opinion and making informed decisions about movie choices.

**Movie Filtering Options:** The movie filter functionality has been expanded, allowing users to search for movies based on various criteria. Users can now filter movies by genre, release date range, language, and country. These filtering options provide users with more control and flexibility in finding movies that align with their preferences.


## Known Issues
- In rare cases, the movie filtering functionality may not return expected results when specific combinations of filters are applied. This issue is currently under investigation and will be addressed in a future release.
- On slower network connections, the loading time for movie details and cast information may be longer than expected. This delay is being actively optimized to improve performance.
## Roadmap

- ## Data Collection and Preparation

    Gather movie data from reliable sources such as online databases or APIs.
    Perform data cleaning and preprocessing to ensure data quality and consistency.
    Handle missing values, duplicates, and data imputation if required.


- ## Exploratory Data Analysis (EDA)

    Conduct a comprehensive analysis of the movie dataset.
    Explore various attributes such as movie genres, ratings, release dates, and more.
    Generate descriptive statistics, visualizations, and insights to better understand the dataset.

- ## Movie Recommendation System using Cosine Similarity

    Implement a movie recommendation system based on cosine similarity.
    Utilize the movie dataset to calculate similarity scores between movies.
    Recommend similar movies based on user preferences or selected movies.

- ## Web Scraping for Movie Details and Filter Page

    Scrape additional movie details and metadata from online sources such as IMDb or TMDb.
    Extract relevant information like movie descriptions, cast and crew, runtime, etc.
    Implement a filter page to allow users to search and browse movies based on different criteria.

- ## Sentiment Analysis using Count Vectorizer, Bag of Words, and Logistic Regression

    Perform sentiment analysis on movie reviews using machine learning techniques.
    Utilize count vectorization and bag of words approach to convert text data into numerical features.
    Train a logistic regression model to classify movie reviews as positive or negative sentiment.

- ## Integration and Deployment

    Combine the different components of the project into a cohesive system.
    Build a user-friendly interface using frameworks like Streamlit or Flask.
    Deploy the project on a web server or cloud platform for easy access and usage.

- ## Documentation and Refinement

    Create detailed documentation explaining the project, its functionalities, and usage instructions.
    Refine and optimize the codebase for better performance and maintainability.


The project roadmap outlines the key steps and components involved in building the movie recommendation system, including data collection, analysis, recommendation algorithms, web scraping, sentiment analysis, integration, and documentation. Following this roadmap will help guide the development process and ensure a systematic and successful project completion.
## Run Locally

- Clone the project

    ```bash
    git clone https://github.com/sukritiguin/movie-app
    ```

- Go to the project directory

    ```bash
    cd movie-app
    ```

- Install the required dependencies

    ```bash
    pip install -r requirements.txt
    ```
- Run the project
    ```bash
    streamlit run app.py
    ```
## Lessons Learned

While building this project, I gained valuable insights and acquired new skills in various areas. Here are the key lessons I learned:

1. **Logistic Regression:** I learned how to implement and utilize logistic regression for classification tasks, particularly in sentiment analysis of user reviews. This technique helped in analyzing the polarity of movie reviews and making informed decisions.

2. **Bag of Words and Count Vectorizer:** I explored the concepts of the bag of words model and count vectorizer to convert textual data into numerical representations. This was crucial for processing movie overviews and generating recommendations based on similarity.

3. **Web Scraping using BeautifulSoup and Selenium:** I developed proficiency in web scraping techniques using libraries like BeautifulSoup and Selenium. This allowed me to gather movie-related information, such as ratings, genres, and cast details, from various online sources.

4. **Streamlit:** I learned how to leverage the Streamlit library to build interactive and user-friendly web applications. Streamlit simplified the process of creating a sleek user interface for the Movie Recommendation System.

5. **Image Generation using Pillow:** I discovered how to utilize the Pillow library in Python to generate movie posters dynamically. This feature enhanced the visual appeal of the application and provided users with an immersive experience.

6. **TMDB API Handling:** I gained experience in working with APIs, particularly the TMDB API, to fetch movie data programmatically. This allowed me to retrieve comprehensive movie information, including release dates, languages, and availability on different streaming platforms.

7. **Pandas Data Manipulation and Cleaning:** I developed proficiency in using the Pandas library for data manipulation and cleaning tasks. This enabled me to preprocess and transform movie data, ensuring its suitability for analysis and recommendation generation.

8. **Cosine Similarity for Recommendation System:** I explored the concept of cosine similarity as a metric for measuring the similarity between movies. This technique formed the basis of the recommendation algorithm, allowing the system to suggest movies based on user preferences and selected movies.

## Challenges Faced and Solutions:

- **Challenge:** Obtaining accurate and comprehensive movie data from multiple sources.
  - **Solution:** By combining web scraping techniques with API integration, I was able to gather diverse and up-to-date movie information, ensuring the system's recommendation accuracy.

- **Challenge:** Handling large machine learning models and optimizing performance.
  - **Solution:** To address this challenge, I leveraged techniques such as model compression and loading models on-demand. This approach helped in managing the large ML models efficiently and improving the system's responsiveness.

- **Challenge:** Dealing with missing or incomplete data in the movie dataset.
  - **Solution:** I implemented data cleaning strategies, such as handling missing values, removing duplicates, and performing data imputation when appropriate. This improved the quality and reliability of the movie data used for recommendation generation.

- **Challenge:** Scraping movie trailer links from YouTube.

    - **Solution:** Initially, I attempted to extract the links using traditional web scraping techniques with libraries like BeautifulSoup. However, due to YouTube's dynamic nature, these methods proved ineffective. To overcome this challenge, I researched and learned about Selenium, a powerful web automation tool. I implemented a function called get_youtube_trailler(movie_name) that utilized Selenium to search for the movie trailer on YouTube and extract the corresponding link. By leveraging Selenium's capabilities, I successfully retrieved the movie trailer links, enhancing the overall functionality of the project and providing users with a valuable feature.
## Acknowledgements

Acknowledgements:

- **ChatGPT:** I would like to express my gratitude to ChatGPT, the language model developed by OpenAI, for its powerful natural language processing capabilities. It has been an invaluable tool in assisting with the development of this project.

- **YouTube:** I would like to acknowledge YouTube for providing a vast repository of informative and educational videos. Various YouTube channels and tutorials have contributed to my learning process and understanding of different concepts and techniques used in this project. In particular, I would like to mention the [CampusX Official](https://www.youtube.com/@campusx-official) YouTube channel for their insightful content.

- **Kaggle:** Kaggle, a platform for data science and machine learning, has been a valuable resource throughout this project. I would like to acknowledge the Kaggle community and the following Kaggle contributors for their shared code and datasets that have greatly assisted in the development of this project:
  - [Muhammad Ayman](https://www.kaggle.com/code/muhammadayman) for the recommendation system using cosine similarity.
  - [Lakshmi Npathi](https://www.kaggle.com/code/lakshmi25npathi) for the sentiment analysis of IMDb movie reviews.
  - [Shubham Trivedi](https://www.kaggle.com/code/shubhamptrivedi) for the sentiment analysis on IMDb movie reviews.

- **Stack Overflow:** Stack Overflow, a popular question and answer platform for programmers, has been instrumental in overcoming various technical challenges during the development of this project. The contributions of the Stack Overflow community are highly appreciated.

- **GitHub:** GitHub, a web-based hosting service for version control and collaboration, has played a significant role in the development and sharing of this project. I would like to acknowledge the following GitHub repositories for their valuable code references and inspiration:
  - [Pravinkumar O Singh](https://github.com/pravinkumarosingh) for the MoRe (Movie Recommendation) repository.
  - [Kishan Singh](https://github.com/kishan0725) for The Movie Cinema and AJAX Movie Recommendation System with Sentiment Analysis repositories.

I express my sincere thanks to all the individuals and platforms mentioned above for their contributions, which have enriched my learning experience and facilitated the development of this project.
