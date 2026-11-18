# 🎬 Movie Recommendation System

## 📌 Project Overview

The Movie Recommendation System is a content-based movie recommendation application that recommends movies similar to a movie selected by the user.

The system uses movie information such as:

- Genres
- Keywords
- Cast
- Director
- Overview

These features are combined into a single text-based feature called **tags**. The tags are converted into numerical vectors using **CountVectorizer**, and **Cosine Similarity** is used to identify movies with similar content.

The final recommendation system is deployed as an interactive web application using **Streamlit**.

The user can enter a movie name, and the system provides a list of similar movies along with information such as:

- Movie title
- Similarity score
- Rating
- Release year
- Movie overview

## 🎯 Problem Statement

With a large number of movies available across different platforms, users may find it difficult to discover movies that match their interests.

A movie recommendation system can help users discover similar movies based on the characteristics and content of a movie they already like.

This project aims to develop a content-based movie recommendation system that analyzes movie information and recommends similar movies to the user.

## 🚀 Objectives

The main objectives of this project are:

- To build a movie recommendation system using Python.
- To preprocess and combine movie and credits datasets.
- To extract meaningful features such as genres, keywords, cast, director, and overview.
- To create a combined text feature called `tags`.
- To convert movie tags into numerical vectors using CountVectorizer.
- To calculate similarity between movies using Cosine Similarity.
- To recommend movies based on their content similarity.
- To provide movie details along with recommendations.
- To develop an interactive and user-friendly web application using Streamlit.

## ✨ Features

- 🔎 Search for a movie by name.
- 🤖 Recommend similar movies using content-based filtering.
- 🎭 Uses genres, keywords, cast, director, and overview for recommendations.
- 📊 Displays similarity scores for recommended movies.
- ⭐ Displays movie ratings.
- 📅 Displays movie release years.
- 📝 Displays movie overviews.
- 🔤 Supports case-insensitive and flexible movie searches.
- ✏️ Handles minor spelling mistakes using fuzzy matching.
- ❌ Displays a suitable message when a movie is not found.
- 🎨 Provides an interactive and visually designed Streamlit interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | CountVectorizer and Cosine Similarity |
| Streamlit | Web application development |
| Pickle | Saving and loading processed model data |
| Jupyter Notebook | Data analysis and model development |

## 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains movie-related information used to build the recommendation system.

The project uses two CSV files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Movie Dataset

The movie dataset contains information such as:

- Movie title
- Genres
- Keywords
- Overview
- Release date
- Rating
- Popularity
- Runtime
- Budget
- Revenue

### Credits Dataset

The credits dataset contains information such as:

- Movie ID
- Movie title
- Cast
- Crew

The two datasets are merged using the movie ID.

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── movie_recommendation.ipynb
│
├── app.py
│
├── movie_dict.pkl
├── movie_details.pkl
├── movie_indices.pkl
├── similarity.pkl
│
├── movie_background.png
├── hero_background.png
│
├── requirements.txt
└── README.md
```

## 🔄 Methodology

The recommendation system follows a content-based filtering approach.

The overall workflow is:

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Merge Movies + Credits
      ↓
Feature Extraction
      ↓
Create Combined Tags
      ↓
CountVectorizer
      ↓
Cosine Similarity
      ↓
Recommendation Function
      ↓
Streamlit Application
```

## 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset before building the recommendation system.

The analysis included:

- Dataset size
- Missing value analysis
- Duplicate value analysis
- Genre distribution
- Movie rating distribution
- Movie popularity distribution
- Movies by release year
- Runtime distribution

### Dataset Size

The dataset contains:

- **4,803 movies**
- **20 columns** in the movie dataset
- **4,803 records** in the credits dataset
- **4 columns** in the credits dataset

### Missing Values

Missing values were checked in both datasets.

The main missing values in the movie dataset were found in:

- `homepage`
- `tagline`
- `overview`
- `runtime`
- `release_date`

The overview column was handled by replacing missing values with an empty string because the overview is used as part of the recommendation features.

### Duplicate Values

No duplicate records were found in the movie and credits datasets.

### Genre Distribution

The genre distribution was analyzed to understand how movies are distributed across different genres.

**Drama** has the highest number of movies in this dataset.

### Rating Distribution

The movie rating distribution was visualized using a histogram.

The average movie rating in the dataset is approximately:

**6.09**

### Popularity Distribution

Movie popularity was also analyzed using a histogram.

The average popularity value in the dataset is approximately:

**21.49**

### Release Year Analysis

The release year of movies was extracted from the release date.

The dataset contains movies released from approximately:

**1916 to 2017**

### Runtime Analysis

The distribution of movie runtimes was visualized.

The average runtime is approximately:

**106.88 minutes**

## 🎬 Recommendation Results

The recommendation system was tested using different movie titles to check whether the generated recommendations were relevant to the selected movie.

For example, when **Avatar** was entered, the system generated movies such as:

| Movie | Similarity Score |
|---|---:|
| Aliens | 0.48 |
| Moonraker | 0.43 |
| Alien | 0.42 |
| Alien³ | 0.40 |
| Silent Running | 0.39 |

The system was also tested using **Toy Story**.

The recommendations included movies such as:

| Movie | Similarity Score |
|---|---:|
| Toy Story 2 | 0.50 |
| Toy Story 3 | 0.47 |
| Small Soldiers | 0.29 |
| Everything You Always Wanted to Know About Sex *But Were Afraid to Ask | 0.28 |
| The 40 Year Old Virgin | 0.27 |

These tests were used as qualitative sanity checks to verify that the recommendation system was producing similar movies based on their content.

### Evaluation Approach

Since this is a content-based recommendation system, classification metrics such as accuracy, precision, recall, and F1-score are not used as the primary evaluation method.

Instead, the system was evaluated through:

- Sample movie testing
- Relevance of recommended movies
- Similarity scores
- Manual inspection of recommendations
- Testing different movie inputs
- Testing flexible and misspelled movie searches

## ⚙️ Installation

### 1. Clone or download the project

Download the project and open the project folder in Command Prompt or a terminal.

### 2. Install the required libraries

Run:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

Run:

```bash
python -m streamlit run app.py
```

The application will open in a web browser.

## 🖥️ How to Use the Application

1. Open the Movie Recommendation System.
2. Enter the name of a movie in the search box.
3. Click the **Recommend** button.
4. The system finds the selected movie.
5. The system calculates its similarity with other movies.
6. The top similar movies are displayed.
7. View the movie title, similarity score, rating, release year, and overview.

### Example

Enter:

```text
Avatar
```

The system will display movies that are similar to Avatar based on the movie's content features.

### Flexible Search

The application supports flexible movie searches, including:

```text
Avatar
avatar
Avatr
```

These inputs can be used to find the corresponding movie through title normalization and fuzzy matching.

If a completely unrelated movie name is entered, the application displays a movie-not-found message.

## ⚠️ Limitations

- The system uses content-based filtering and does not consider user ratings or preferences from other users.
- Recommendations depend on the information available in the movie dataset.
- Movies with limited or incomplete descriptive information may receive less meaningful recommendations.
- The system does not currently provide personalized recommendations based on a user's viewing history.
- The current recommendation system focuses on movie content rather than real-time user behavior.

## 🔮 Future Enhancements

The project can be extended with:

- Collaborative filtering based on user ratings.
- Hybrid recommendation combining content-based and collaborative filtering.
- User login and personalized recommendation history.
- Movie posters and trailers using external APIs.
- More advanced NLP techniques for movie descriptions.
- Improved ranking of recommendations.
- User rating and feedback functionality.
- Deployment of the application on a cloud platform.

## 🏁 Conclusion

The Movie Recommendation System demonstrates how machine learning and natural language processing techniques can be used to build a content-based recommendation application.

Movie information such as genres, keywords, cast, director, and overview was combined into a single feature and converted into numerical vectors using CountVectorizer.

Cosine Similarity was then used to identify movies with similar content.

The recommendation system was integrated with Streamlit to provide an interactive user interface where users can search for a movie and receive similar movie recommendations.

This project provides a practical implementation of data preprocessing, exploratory data analysis, feature engineering, text vectorization, similarity-based recommendation, and web application development using Python.