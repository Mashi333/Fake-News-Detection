import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vectorizer.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def stemming(content):
    con=re.sub('[^a-zA-Z]', ' ', content)
    con=con.lower()
    con=con.split()
    con=[port_stem.stem(word) for word in con if not word in stopwords.words('english')]
    con=' '.join(con)
    return con

def fake_news(news):
    news=stemming(news)
    
    input_data=[news]
    vector_form1=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction



if __name__ == '__main__':
    # Page configuration
    st.set_page_config(
        page_title="Fake News Detector",
        page_icon="🔍",
        layout="centered"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            color: #1E88E5;
            text-align: center;
        }
        .sub-font {
            font-size:25px;
            color: #424242;
            text-align: center;
        }
        .stButton>button {
            background-color: #1E88E5;
            color: white;
            padding: 0.5rem 2rem;
            font-size: 20px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and Description
    st.markdown('<p class="big-font">🔍 Fake News Detective</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-font">Your trusted source for news verification</p>', unsafe_allow_html=True)
    
    # Add a separator
    st.markdown("---")

    # Information box
    st.info('ℹ️ This tool uses machine learning to analyze news content and determine its reliability.')
    
    # Input section
    st.subheader("📰 Input News Content")
    sentence = st.text_area(
        "Paste your news article here",
        "",
        height=200,
        placeholder="Enter the news content you want to verify..."
    )

    # Center the predict button
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        predict_btt = st.button("Analyze News")

    # Show prediction with more context
    if predict_btt:
        if sentence:
            with st.spinner('Analyzing the news content...'):
                prediction_class = fake_news(sentence)
                st.markdown("---")
                st.subheader("🎯 Analysis Result")
                
                if prediction_class == [0]:
                    st.success('✅ This news appears to be Reliable')
                    st.markdown("The content shows characteristics of legitimate news.")
                if prediction_class == [1]:
                    st.warning('⚠️ This news appears to be Unreliable')
                    st.markdown("The content shows characteristics of fake news.")
        else:
            st.error("Please enter some news content to analyze!")