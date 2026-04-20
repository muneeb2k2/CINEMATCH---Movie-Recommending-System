import streamlit as st
import pickle

# ------------------ LOAD DATA ------------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap');

/* ---- Reset & Base ---- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background-color: #080a0f !important;
    color: #e8e0d4;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(220,60,40,0.18) 0%, transparent 70%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(255,120,40,0.08) 0%, transparent 60%),
        #080a0f !important;
}

/* Film grain overlay */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 9999;
    opacity: 0.6;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
.block-container {
    padding: 3rem 4rem 5rem !important;
    max-width: 1200px;
}

/* ---- Hero Header ---- */
.hero-wrap {
    text-align: center;
    padding: 3rem 0 1rem;
    animation: fadeDown 0.9s ease both;
}
.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #e05c30;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(4rem, 10vw, 8rem);
    line-height: 0.9;
    letter-spacing: 0.04em;
    color: #f0ebe3;
    text-shadow:
        0 0 60px rgba(220,80,40,0.4),
        0 2px 0 rgba(0,0,0,0.8);
    margin-bottom: 1rem;
}
.hero-title span { color: #e05c30; }
.hero-sub {
    font-size: 1rem;
    font-weight: 300;
    color: #7a7264;
    letter-spacing: 0.02em;
}
.divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #e05c30, transparent);
    margin: 1.5rem auto;
}

/* ---- Select Box ---- */
[data-testid="stSelectbox"] label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    color: #7a7264 !important;
    margin-bottom: 0.4rem !important;
}
[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.035) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 4px !important;
    color: #e8e0d4 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.6rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
    backdrop-filter: blur(8px);
}
[data-testid="stSelectbox"] > div > div:hover,
[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: rgba(224, 92, 48, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(224, 92, 48, 0.1) !important;
}

/* ---- Button ---- */
.stButton { text-align: center; margin-top: 1.5rem; }
.stButton > button {
    background: linear-gradient(135deg, #c93a1a 0%, #e05c30 50%, #f07840 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 3px !important;
    padding: 0.85rem 3rem !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.3rem !important;
    letter-spacing: 0.15em !important;
    cursor: pointer !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    box-shadow: 0 4px 30px rgba(200,60,20,0.45) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 40px rgba(200,60,20,0.6) !important;
}
.stButton > button:active {
    transform: translateY(0px) scale(0.99) !important;
}

/* ---- Results Section ---- */
.results-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem;
    letter-spacing: 0.12em;
    color: #7a7264;
    text-align: center;
    margin: 3rem 0 2rem;
    animation: fadeUp 0.6s ease both;
}
.results-header span { color: #e8e0d4; }

/* ---- Movie Cards ---- */
.card-outer {
    animation: fadeUp 0.5s ease both;
}
.card-outer:nth-child(1) { animation-delay: 0.05s; }
.card-outer:nth-child(2) { animation-delay: 0.12s; }
.card-outer:nth-child(3) { animation-delay: 0.19s; }
.card-outer:nth-child(4) { animation-delay: 0.26s; }
.card-outer:nth-child(5) { animation-delay: 0.33s; }

.movie-card {
    position: relative;
    background: linear-gradient(145deg, rgba(28,24,20,0.95), rgba(18,15,12,0.98));
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 6px;
    padding: 1.8rem 1.2rem 1.6rem;
    text-align: center;
    overflow: hidden;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    cursor: default;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.7rem;
}
.movie-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(224,92,48,0.12), transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.movie-card:hover {
    transform: translateY(-6px);
    border-color: rgba(224,92,48,0.35);
    box-shadow: 0 12px 40px rgba(0,0,0,0.6), 0 0 30px rgba(224,92,48,0.12);
}
.movie-card:hover::before { opacity: 1; }

.card-rank {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    line-height: 1;
    color: rgba(224,92,48,0.2);
    position: absolute;
    top: 0.5rem;
    left: 0.85rem;
    user-select: none;
}
.card-icon {
    font-size: 1.6rem;
    line-height: 1;
}
.card-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.92rem;
    font-weight: 500;
    color: #e8e0d4;
    line-height: 1.4;
    z-index: 1;
}

/* ---- Animations ---- */
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-22px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #080a0f; }
::-webkit-scrollbar-thumb { background: #2a2520; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero-wrap">
    <p class="hero-eyebrow">✦ AI-Powered Discovery</p>
    <h1 class="hero-title">CINE<span>MATCH</span></h1>
    <div class="divider"></div>
    <p class="hero-sub">Tell us what you love. We'll find what you'll obsess over.</p>
</div>
""", unsafe_allow_html=True)

# ------------------ SELECT BOX ------------------
st.markdown("<br>", unsafe_allow_html=True)
movie_list = movies['title'].values
selected_movie = st.selectbox("Pick a movie you love", movie_list, label_visibility="visible")

# ------------------ RECOMMEND FUNCTION ------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

# ------------------ BUTTON ------------------
if st.button("FIND MY MOVIES"):
    results = recommend(selected_movie)

    st.markdown(f"""
    <div class="results-header">
        Because you watched <span>"{selected_movie}"</span>
    </div>
    """, unsafe_allow_html=True)

    icons = ["🎬", "🎥", "🍿", "🎞️", "⭐"]
    cols = st.columns(5)

    for i, col in enumerate(cols):
        if i < len(results):
            with col:
                st.markdown(f"""
                <div class="card-outer">
                    <div class="movie-card">
                        <span class="card-rank">0{i+1}</span>
                        <div class="card-icon">{icons[i]}</div>
                        <div class="card-title">{results[i]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)