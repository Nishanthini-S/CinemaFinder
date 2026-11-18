import streamlit as st
import pickle
import base64
import re
from difflib import get_close_matches


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Cinema Finder",
    page_icon="🎬",
    layout="wide"
)


# ============================================================
# LOAD IMAGES
# ============================================================

with open("movie_background.png", "rb") as file:
    background_image = base64.b64encode(
        file.read()
    ).decode()

with open("hero_background.png", "rb") as file:
    hero_image = base64.b64encode(
        file.read()
    ).decode()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
f"""
<style>

.stApp {{
    background-image:
        linear-gradient(
            rgba(5, 4, 15, 0.40),
            rgba(5, 4, 15, 0.72)
        ),
        url("data:image/png;base64,{background_image}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}}


#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}


.block-container {{
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}}


/* =========================================================
   HERO CARD
   ========================================================= */

.hero-card {{
    position: relative;

    min-height: 370px;

    border-radius: 30px;

    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.16);

    background:
        linear-gradient(
            90deg,
            rgba(8,6,18,0.98) 0%,
            rgba(10,7,20,0.93) 38%,
            rgba(10,7,20,0.70) 65%,
            rgba(10,7,20,0.25) 100%
        );

    box-shadow:
        0 25px 80px rgba(0,0,0,0.60),
        0 0 45px rgba(139,92,246,0.12);

    display: flex;
    align-items: center;
}}


/* =========================================================
   HERO IMAGE
   ========================================================= */

.hero-photo {{
    position: absolute;

    right: 0;
    top: 0;

    width: 63%;
    height: 100%;

    background-image:
        linear-gradient(
            90deg,
            rgba(8,6,18,1) 0%,
            rgba(8,6,18,0.88) 18%,
            rgba(8,6,18,0.35) 60%,
            rgba(8,6,18,0.10) 100%
        ),
        url("data:image/png;base64,{hero_image}");

    background-size: cover;
    background-position: center;

    opacity: 0.90;
}}


/* =========================================================
   HERO CONTENT
   ========================================================= */

.hero-content {{
    position: relative;

    z-index: 3;

    width: 55%;

    padding: 50px;
}}


/* =========================================================
   HERO ICON
   ========================================================= */

.hero-icon {{
    font-size: 4rem;

    margin-bottom: 8px;

    filter:
        drop-shadow(
            0 0 20px rgba(192,132,252,0.65)
        );
}}


/* =========================================================
   HERO TITLE
   ========================================================= */

.hero-title {{
    font-size: 3.6rem;

    font-weight: 900;

    letter-spacing: 1px;

    line-height: 1.1;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #d8b4fe,
            #f0abfc
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin-bottom: 20px;
}}


/* =========================================================
   HERO SUBTITLE
   ========================================================= */

.hero-subtitle {{
    color: #ded9e8;

    font-size: 1.08rem;

    line-height: 1.8;
}}


/* =========================================================
   SEARCH AREA
   ========================================================= */

.search-section {{
    margin-top: 45px;

    text-align: center;
}}


.search-title {{
    color: white;

    font-size: 1.55rem;

    font-weight: 750;

    margin-bottom: 7px;
}}


.search-subtitle {{
    color: #aaa7b7;

    font-size: 0.95rem;

    margin-bottom: 20px;
}}


/* =========================================================
   SEARCH INPUT
   ========================================================= */

.stTextInput > div > div > input {{
    height: 58px !important;

    background:
        rgba(15,14,25,0.94) !important;

    color: white !important;

    border:
        1px solid rgba(210,180,255,0.38) !important;

    border-radius: 16px !important;

    font-size: 16px !important;

    padding-left: 20px !important;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.35) !important;

    transition: 0.25s ease !important;
}}


.stTextInput > div > div > input::placeholder {{
    color: #9d99a9 !important;

    opacity: 1 !important;
}}


.stTextInput > div > div > input:focus {{
    border:
        1px solid #c084fc !important;

    box-shadow:
        0 0 25px rgba(168,85,247,0.30) !important;
}}


/* =========================================================
   RECOMMEND BUTTON
   ========================================================= */

.stButton {{
    display: flex;

    justify-content: center;
}}


.stButton > button {{
    width: 185px !important;

    height: 48px !important;

    margin-top: 12px !important;

    border: none !important;

    border-radius: 25px !important;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #c026d3
        ) !important;

    color: white !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 28px rgba(139,92,246,0.35) !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease !important;
}}


.stButton > button:hover {{
    transform: translateY(-3px) !important;

    box-shadow:
        0 14px 38px rgba(192,38,211,0.50) !important;
}}


/* =========================================================
   POWERED BY
   ========================================================= */

.powered {{
    text-align: center;

    color: #777383;

    font-size: 0.82rem;

    margin-top: 14px;

    margin-bottom: 45px;
}}


/* =========================================================
   RECOMMENDATION TITLE
   ========================================================= */

.recommendation-title {{
    text-align: center;

    color: white;

    font-size: 2rem;

    font-weight: 800;

    margin-top: 30px;

    margin-bottom: 30px;
}}


/* =========================================================
   MOVIE CARD
   ========================================================= */

.movie-card {{
    background:
        linear-gradient(
            145deg,
            rgba(20,17,32,0.96),
            rgba(8,8,17,0.95)
        );

    border:
        1px solid rgba(255,255,255,0.13);

    border-radius: 22px;

    padding: 25px;

    min-height: 320px;

    box-shadow:
        0 15px 45px rgba(0,0,0,0.45);

    transition:
        transform 0.25s ease,
        border 0.25s ease,
        box-shadow 0.25s ease;
}}


.movie-card:hover {{
    transform: translateY(-7px);

    border:
        1px solid rgba(192,132,252,0.65);

    box-shadow:
        0 20px 55px rgba(139,92,246,0.25);
}}


/* =========================================================
   MOVIE NUMBER
   ========================================================= */

.movie-number {{
    color: #c084fc;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 2px;

    margin-bottom: 12px;
}}


/* =========================================================
   MOVIE TITLE
   ========================================================= */

.movie-title {{
    color: white;

    font-size: 1.3rem;

    font-weight: 750;

    line-height: 1.35;

    margin-bottom: 20px;
}}


/* =========================================================
   MOVIE INFO
   ========================================================= */

.movie-info {{
    color: #ddd9e5;

    font-size: 14px;

    margin-bottom: 10px;
}}


/* =========================================================
   SIMILARITY
   ========================================================= */

.similarity {{
    display: inline-block;

    margin-top: 10px;

    padding: 7px 13px;

    border-radius: 20px;

    background:
        rgba(139,92,246,0.16);

    border:
        1px solid rgba(192,132,252,0.25);

    color: #d8b4fe;

    font-size: 13px;

    font-weight: 650;
}}


/* =========================================================
   OVERVIEW
   ========================================================= */

.movie-overview {{
    color: #aaa6b5;

    font-size: 14px;

    line-height: 1.6;

    margin-top: 17px;
}}


/* =========================================================
   FOOTER
   ========================================================= */

.custom-footer {{
    text-align: center;

    color: #777582;

    font-size: 13px;

    margin-top: 65px;

    padding-top: 25px;

    border-top:
        1px solid rgba(255,255,255,0.08);
}}

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# LOAD RECOMMENDATION DATA
# ============================================================

with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

with open("movie_details.pkl", "rb") as file:
    movie_details = pickle.load(file)

with open("movie_indices.pkl", "rb") as file:
    movie_indices = pickle.load(file)


# ============================================================
# SMART TITLE NORMALIZATION
# ============================================================

def normalize_title(title):

    title = str(title).lower()

    # Remove spaces, hyphens, punctuation, etc.
    # Example:
    #
    # Spider-Man  -> spiderman
    # spider man  -> spiderman
    # SPIDER-MAN  -> spiderman

    title = re.sub(r"[^a-z0-9]", "", title)

    return title


# ============================================================
# FIND MOVIE
# ============================================================

def find_movie(movie_name):

    # Create normalized movie-title mapping

    normalized_titles = {}

    for title in movie_indices.index:

        normalized = normalize_title(title)

        normalized_titles[normalized] = title


    # Normalize user's input

    normalized_input = normalize_title(movie_name)


    # --------------------------------------------------------
    # EXACT NORMALIZED MATCH
    # --------------------------------------------------------

    if normalized_input in normalized_titles:

        actual_title = normalized_titles[normalized_input]

        movie_index = movie_indices[actual_title]

        return movie_index, actual_title


    # --------------------------------------------------------
    # FUZZY MATCH
    # --------------------------------------------------------

    possible_matches = get_close_matches(
        normalized_input,
        normalized_titles.keys(),
        n=1,
        cutoff=0.80
    )


    if possible_matches:

        matched_normalized_title = possible_matches[0]

        actual_title = normalized_titles[
            matched_normalized_title
        ]

        movie_index = movie_indices[actual_title]

        return movie_index, actual_title


    return None, None


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend(movie_name, n=5):

    movie_index, actual_title = find_movie(movie_name)


    if movie_index is None:

        return [], None


    similarity_scores = list(
        enumerate(similarity[movie_index])
    )


    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )


    recommendations = []


    for index, score in similarity_scores[1:]:

        movie = movie_details.iloc[index]


        recommendations.append({

            "title": movie["title"],

            "similarity": score,

            "rating": movie["vote_average"],

            "release_year": movie["release_year"],

            "overview": movie["overview"]

        })


        if len(recommendations) == n:

            break


    return recommendations, actual_title


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
"""
<div class="hero-card">

<div class="hero-photo"></div>

<div class="hero-content">

<div class="hero-icon">🎬</div>

<div class="hero-title">
CINEMA FINDER
</div>

<div class="hero-subtitle">
Discover movies you'll love next
<br>
Powered by Content-Based Recommendation
</div>

</div>

</div>
""",
unsafe_allow_html=True
)


# ============================================================
# SEARCH SECTION
# ============================================================

st.markdown(
"""
<div class="search-section">

<div class="search-title">
✦ Find Your Next Movie ✦
</div>

<div class="search-subtitle">
Search for a movie you already love
</div>

</div>
""",
unsafe_allow_html=True
)


# ============================================================
# SEARCH BOX
# ============================================================

movie_name = st.text_input(
    "Movie Search",
    placeholder="🔍  Try Avatar, Tangled, Toy Story, The Dark Knight...",
    label_visibility="collapsed"
)


# ============================================================
# BUTTON
# ============================================================

button_left, button_center, button_right = st.columns(
    [2.2, 1, 2.2]
)


with button_center:

    recommend_button = st.button(
        "🎬  Recommend"
    )


# ============================================================
# POWERED BY
# ============================================================

st.markdown(
"""
<div class="powered">
✨ Powered by Content-Based Movie Recommendation
</div>
""",
unsafe_allow_html=True
)


# ============================================================
# RECOMMENDATIONS
# ============================================================

if recommend_button:

    if movie_name.strip() == "":

        st.warning(
            "Please enter a movie name to get recommendations."
        )

    else:

        recommendations, actual_title = recommend(
            movie_name,
            n=5
        )


        if not recommendations:

            st.error(
                "Movie not found. Please check the movie name."
            )

        else:

            # ----------------------------------------------
            # HEADING
            # ----------------------------------------------

            st.markdown(
            f"""
            <div class="recommendation-title">
            ✨ Movies You Might Like
            </div>

            <div style="
                text-align:center;
                color:#aaa7b7;
                font-size:0.95rem;
                margin-top:-15px;
                margin-bottom:30px;
            ">
                🔎 Showing recommendations for
                <b style="color:white;">{actual_title}</b>
            </div>
            """,
            unsafe_allow_html=True
            )


            # ----------------------------------------------
            # MOVIE CARDS
            # ----------------------------------------------

            for start in range(
                0,
                len(recommendations),
                3
            ):

                row_movies = recommendations[
                    start:start + 3
                ]


                columns = st.columns(
                    len(row_movies),
                    gap="medium"
                )


                for card_number, (column, movie) in enumerate(
                    zip(columns, row_movies),
                    start=start + 1
                ):

                    # --------------------------------------
                    # YEAR
                    # --------------------------------------

                    year = movie["release_year"]


                    if str(year) == "nan":

                        year = "N/A"

                    else:

                        try:

                            year = int(year)

                        except:

                            year = str(year)


                    # --------------------------------------
                    # OVERVIEW
                    # --------------------------------------

                    overview = movie["overview"]


                    if not overview:

                        overview = (
                            "No overview available."
                        )

                    elif len(overview) > 180:

                        overview = (
                            overview[:180]
                            + "..."
                        )


                    # --------------------------------------
                    # CARD
                    # --------------------------------------

                    with column:

                        st.markdown(
f"""
<div class="movie-card">

<div class="movie-number">
RECOMMENDATION {card_number}
</div>

<div class="movie-title">
{movie["title"]}
</div>

<div class="movie-info">
⭐ <b>Rating:</b> {movie["rating"]}
</div>

<div class="movie-info">
📅 <b>Release Year:</b> {year}
</div>

<div class="similarity">
🔗 Similarity: {movie["similarity"]:.2f}
</div>

<div class="movie-overview">
{overview}
</div>

</div>
""",
                        unsafe_allow_html=True
                        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
"""
<div class="custom-footer">
🎬 Cinema Finder
&nbsp;&nbsp;•&nbsp;&nbsp;
Content-Based Movie Recommendation System
</div>
""",
unsafe_allow_html=True
)