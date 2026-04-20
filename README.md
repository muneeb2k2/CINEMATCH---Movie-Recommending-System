# CineMatch: AI-Powered Movie Recommender

A sleek, modern movie recommendation system built with Streamlit that suggests movies based on your favorite films using content-based filtering.

## Features

- 🎬 Intuitive web interface with cinematic design
- 🤖 AI-powered recommendations using cosine similarity
- 📊 Based on TMDB 5000 dataset
- 🎨 Beautiful, responsive UI with custom CSS

## Demo

![CineMatch Demo](demo.gif)  <!-- Add a screenshot or gif later -->

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muneeb2k2/CINEMATCH---Movie-Recommending-System.git
   cd CINEMATCH---Movie-Recommending-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:
   - Download `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` from [Kaggle TMDB 5000 Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Place them in the project root

4. Run the data processing notebook:
   ```bash
   jupyter notebook movie_recommender_system.ipynb
   ```
   Execute all cells to generate `movies.pkl` and `similarity.pkl`

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Select a movie you love from the dropdown
2. Click "FIND MY MOVIES"
3. Get 5 personalized recommendations!

## Technologies Used

- **Streamlit**: Web app framework
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Cosine similarity for recommendations
- **NLTK**: Text processing
- **TMDB Dataset**: Movie data source

## Project Structure

```
cinematch/
├── app.py                    # Main Streamlit application
├── movie_recommender_system.ipynb  # Data processing and model creation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── movies.pkl               # Processed movie data (generated)
├── similarity.pkl           # Similarity matrix (generated)
└── README.md                # This file
```

## Contributing

Feel free to fork and contribute! Open an issue for bugs or feature requests.

## License

MIT License - see LICENSE file for details.