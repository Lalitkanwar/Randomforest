# ✨ VibeCheck AI: Ultimate Edition

Stop guessing if your day is going to be *mid*. Let the AI analyze your stats and predict your vibe! 

VibeCheck AI is an interactive, visually engaging Streamlit dashboard that predicts whether your daily lifestyle habits—specifically sleep, caffeine intake, and screen time—lead to a **"Productive Day" (W)** or a **"Burnout Day" (L)**. It combines a synthetic dataset with a Random Forest machine learning model to provide real-time, interactive feedback via a sleek, dark-mode web interface.

## 🌟 Features

- **🔮 The Predictor:** Run your daily simulation using interactive sliders for Sleep, Coffee, and Screen Time. Get an instant verdict with an AI confidence score and a dynamic gauge chart.
- **📊 Data Insights:** Explore the analytics behind the vibes! View feature importance, habit distributions, and a 3D scatter plot of the decision boundary.
- **🧠 How It Works:** Dive into the science behind the Random Forest Classifier and understand how the model makes its predictions based on generated behavior profiles.
- **🎈 Explain Like I'm 5:** A fun, pizza-shop-themed breakdown of how Artificial Intelligence and Decision Trees work, making it easy for anyone to understand.

## 🛠️ Tech Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (RandomForestClassifier)
- **Data Visualization:** [Plotly](https://plotly.com/) (Express & Graph Objects)

## 🚀 How to Run Locally

1. **Clone the repository** (or download the files):
   Ensure you have `app.py` and `requirements.txt` in your project folder.

2. **Install the dependencies:**
   Make sure you have Python installed, then run the following command to install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   Start the application by running:
   ```bash
   streamlit run app.py
   ```

4. **View the Dashboard:**
   Open your browser and navigate to `http://localhost:8501` (or the URL provided in your terminal).

## 🎨 Aesthetics

The dashboard features a premium dark mode vibe with a custom CSS design, incorporating:
- A linear gradient button design with hover micro-animations.
- High-contrast highlight colors (`#ff4b4b` and `#ff8c42`).
- Modern typography using the 'Inter' font.

---
*Built with ❤️, Streamlit, and Scikit-Learn.*
