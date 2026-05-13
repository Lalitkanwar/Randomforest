import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
import plotly.graph_objects as go

# Setting up the Page Config (The Aesthetic)
st.set_page_config(page_title="VibeCheck AI Pro", page_icon="✨", layout="wide")

# Enhanced Custom CSS for a Premium Dark Mode Vibe
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #f0f2f6; }
    .stButton>button { 
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8c42 100%);
        color: white; 
        border-radius: 30px; 
        border: none;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6);
    }
    h1, h2, h3 { color: #ffffff; font-family: 'Inter', sans-serif; }
    .highlight { color: #ff4b4b; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 2.5rem; color: #ff8c42; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ VibeCheck AI: Ultimate Edition")
st.write("Stop guessing if your day is going to be <span class='highlight'>mid</span>. Let the AI analyze your stats and predict your vibe.", unsafe_allow_html=True)

# 1. Generating a Random "Gen-Z Life" Dataset
@st.cache_data
def load_data():
    np.random.seed(42)
    data_size = 300
    data = {
        'Sleep_Hours': np.random.uniform(3, 10, data_size),
        'Caffeine_Level': np.random.uniform(0, 6, data_size),
        'Screen_Time': np.random.uniform(1, 14, data_size),
    }
    df = pd.DataFrame(data)
    # Creating a somewhat realistic relationship
    # Good vibe if reasonable sleep, moderate caffeine, not insane screen time
    score = (df['Sleep_Hours'] * 2) - (df['Caffeine_Level'] ** 1.5) - (df['Screen_Time'] * 0.5)
    # Threshold for W
    df['Vibe_Status'] = (score > 6).astype(int) 
    return df

df = load_data()

# 2. Training a Simple Model (The Brains)
@st.cache_resource
def train_model(df):
    X = df[['Sleep_Hours', 'Caffeine_Level', 'Screen_Time']]
    y = df['Vibe_Status']
    model = RandomForestClassifier(random_state=42, n_estimators=100).fit(X, y)
    return model, X

model, X = train_model(df)

# Tabs for better organization
tab1, tab2, tab3, tab4 = st.tabs(["🔮 The Predictor", "📊 Data Insights", "🧠 How It Works", "🎈 Explain Like I'm 5"])

with tab1:
    st.header("🕹️ Run Your Daily Simulation")
    
    # 3. User Input (The Interactive Part)
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        sleep = st.slider("🛌 Sleep (Hours)", 0.0, 12.0, 7.5, 0.5)
    with col_input2:
        coffee = st.slider("☕ Coffee (Cups)", 0.0, 8.0, 2.0, 0.5)
    with col_input3:
        screen = st.slider("📱 Screen Time (Hours)", 0.0, 16.0, 5.0, 0.5)

    # 4. Prediction Logic
    user_input = pd.DataFrame([[sleep, coffee, screen]], columns=['Sleep_Hours', 'Caffeine_Level', 'Screen_Time'])
    prediction = model.predict(user_input)
    prediction_prob = model.predict_proba(user_input)

    st.markdown("---")
    
    # 5. Displaying Results with Main Character Energy
    res_col1, res_col2 = st.columns([1, 1])

    with res_col1:
        st.subheader("The Verdict")
        if prediction[0] == 1:
            st.success("### Outcome: ABSOLUTE W 🏆")
            prob = prediction_prob[0][1]
        else:
            st.error("### Outcome: MASSIVE L 💀")
            prob = prediction_prob[0][0]
            
        st.metric(label="AI Confidence Score", value=f"{prob:.1%}")
        
        # Example text based on outcome
        if prediction[0] == 1:
            st.write("You are locked in. The optimal balance of rest and energy is hitting perfectly. Go conquer the day.")
        else:
            st.write("Bro, you are cooked. You need to adjust your stats before you burn out.")

    with res_col2:
        # Gauge Chart for Probability
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prob * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Confidence %", 'font': {'color': "white"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickcolor': "white"},
                'bar': {'color': "#ff4b4b" if prediction[0] == 0 else "#00cc96"},
                'bgcolor': "rgba(255,255,255,0.05)",
                'steps' : [
                    {'range': [0, 50], 'color': "rgba(255, 255, 255, 0.05)"},
                    {'range': [50, 100], 'color': "rgba(255, 255, 255, 0.1)"}],
            }
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"})
        st.plotly_chart(fig_gauge, use_container_width=True)

with tab2:
    st.header("📈 The Vibe Analytics")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("1. Feature Importance")
        st.write("Which habit impacts your vibe the most?")
        importances = model.feature_importances_
        fig_imp = px.bar(x=importances, y=['Sleep', 'Coffee', 'Screen Time'], orientation='h',
                         labels={'x': 'Impact Level', 'y': 'Habit'},
                         color=importances, color_continuous_scale='Sunset')
        fig_imp.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_imp, use_container_width=True)
        
    with col_chart2:
        st.subheader("2. Habit Distributions")
        st.write("How do your stats compare to the population?")
        metric_choice = st.selectbox("Select Metric to View:", ['Sleep_Hours', 'Caffeine_Level', 'Screen_Time'])
        fig_dist = px.histogram(df, x=metric_choice, color="Vibe_Status", barmode="overlay", 
                                color_discrete_map={0: '#ff4b4b', 1: '#00cc96'},
                                labels={'Vibe_Status': 'W (1) or L (0)'})
        fig_dist.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_dist, use_container_width=True)

    st.subheader("3. The 3D Vibe Space")
    fig_3d = px.scatter_3d(df, x='Sleep_Hours', y='Caffeine_Level', z='Screen_Time',
                        color='Vibe_Status', color_continuous_scale=['#ff4b4b', '#00cc96'],
                        opacity=0.7, title="Decision Boundary Visualization")
    fig_3d.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white", scene=dict(bgcolor="rgba(0,0,0,0)"))
    st.plotly_chart(fig_3d, use_container_width=True)

with tab3:
    st.header("🧑‍🏫 The Science Behind the Vibe")
    
    st.markdown("""
    ### What is happening under the hood?
    
    This application uses a Machine Learning algorithm called a **Random Forest Classifier**. 
    
    1. **The Data**: We generated 300 days of hypothetical human behavior. A mathematical formula decides if a day is a "W" (Productive) or an "L" (Burnout) based on sleep, caffeine, and screen time.
    2. **The Model**: The Random Forest looks at this data and builds 100 "Decision Trees". Each tree asks questions like *"Is sleep < 5 hours?"* or *"Is caffeine > 4 cups?"*
    3. **The Prediction**: When you move the sliders, the AI passes your stats to all 100 trees. They take a vote, and the majority wins. The confidence score is simply the percentage of trees that agreed on the outcome!
    
    ### Examples in the Wild 🌍
    
    * **The "Finance Bro" Profile**: 4 hours sleep, 6 cups of coffee, 12 hours screen time. 
      * *AI Prediction:* **MASSIVE L**. The model recognizes that high caffeine cannot compensate for severe sleep deprivation over time.
    * **The "Zen Master" Profile**: 8 hours sleep, 1 cup of matcha (coffee), 3 hours screen time.
      * *AI Prediction:* **ABSOLUTE W**. The model loves this balanced approach.
    """)

with tab4:
    st.header("🎈 AI Explained for Kids")
    
    st.markdown("""
    ### Imagine You Are the Boss of a Pizza Shop! 🍕
    
    Let's pretend **AI (Artificial Intelligence)** is a super smart robot chef you hired. 
    
    You want the robot to know if a customer will leave **Happy (a "W")** or **Grumpy (an "L")**. But the robot doesn't know anything about people yet! 
    
    So, what do you do? You show the robot your **Data!** Data is just a list of what happened in the past:
    
    * **Customer 1**: Ate 2 slices, waited 5 minutes 👉 **Happy!**
    * **Customer 2**: Ate 0 slices, waited 1 hour 👉 **Grumpy!**
    
    ### How does the Robot learn? 🤖
    
    Instead of pizza slices and waiting time, our robot looks at **Sleep**, **Coffee**, and **Screen Time**.
    
    The robot plays a game called **Random Forest**. Imagine the robot calls 100 of its robot friends (Decision Trees). 
    
    When you move the sliders (like setting 7 hours of sleep), the 100 robots all look at it and vote:
    * 🤖 Robot #1 says: *"They slept enough, so they will be Happy!"*
    * 🤖 Robot #2 says: *"But they had too much screen time, so they will be Grumpy!"*
    
    Then, the boss robot counts the votes. If 80 robots vote "Happy" and 20 vote "Grumpy", the AI tells you: **"Happy!"** and its confidence is **80%**.
    
    **And that's how AI makes predictions—it's just a bunch of tiny robots taking a vote based on what they learned from the past! 🎉**
    """)

st.divider()
st.markdown("<p style='text-align: center; color: #888;'>Built with ❤️, Streamlit, and Scikit-Learn.</p>", unsafe_allow_html=True)
