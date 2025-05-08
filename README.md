

---

# 🎬 Movie Recommendation System

An intelligent movie recommendation system built using **Python**, **Streamlit**, and **TMDb API**. It suggests 5 similar movies based on your selected movie and displays rich visuals including **posters**, **ratings**, and **genres**.

![App Screenshot](https://movie-recommendation-system-i226rkr4lovu9kfe43fdjq.streamlit.app/)

---

## 🚀 Features

✅ **Content-Based Filtering** using Cosine Similarity
✅ **Interactive UI** built with Streamlit
✅ **Live Movie Posters** from TMDb API
✅ **Movie Ratings and Genres** shown in results
✅ **Robust Error Handling** for missing data and network issues

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Libraries**: Pandas, NumPy, Scikit-learn, Requests
* **Data Processing**: Jupyter Notebook
* **API**: [TMDb API](https://www.themoviedb.org/documentation/api)

---

## 🧠 How It Works

### Jupyter Notebook (`Movie_Recommender.ipynb`)

* Loads and processes movie metadata
* Calculates Cosine Similarity matrix
* Saves `movie_dict.pkl` and `similarity.pkl`

### Streamlit App (`app.py`)

* Loads the preprocessed data
* Accepts user movie selection
* Uses similarity scores to find 5 similar movies
* Fetches posters, genres, and ratings via TMDb API
* Displays results with beautiful layout

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anandy07/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # or use env\Scripts\activate on Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your TMDb API Key

Edit `app.py` and replace:

```python
TMDB_API_KEY = "YOUR_API_KEY"
```

> 🔑 Get your API key here: [TMDb API](https://www.themoviedb.org/settings/api)

---

## 📌 Usage

To run the Streamlit app:

```bash
streamlit run app.py
```

> You'll see a web interface where you can select a movie and get 5 similar recommendations.

---

## 📁 File Structure

```
.
├── app.py                  # Streamlit frontend
├── movie_dict.pkl          # Movie metadata dictionary
├── similarity.pkl          # Cosine similarity matrix
├── Movie_Recommender.ipynb # Jupyter Notebook for data prep
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ✨ Future Ideas

* Filter by genre, year, or language
* Add collaborative filtering (user-based)
* Include movie overviews and runtime
* Deploy on Hugging Face or Heroku with user authentication

---

## 🧑‍💻 Author

Developed by **Anand Yadav**
GitHub: [@anandy07](https://github.com/anandy07)
Live App: [movie-recommendation-system.streamlit.app](https://movie-recommendation-system-i226rkr4lovu9kfe43fdjq.streamlit.app/)

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Contribute & Support

If you liked this project, consider giving it a **star ⭐** on GitHub!
Pull requests, issues, and suggestions are always welcome.

---



