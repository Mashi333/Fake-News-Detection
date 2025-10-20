# Fake News Detection App

A machine learning web application that detects whether a news article is **fake** or **reliable** using **Natural Language Processing (NLP)**.

---

## ✅ Features

* 🧠 ML model trained on real-world news dataset
* 🌐 Simple and interactive **Streamlit** web interface
* ⚡ Fast prediction results
* 🔤 Text preprocessing using NLP techniques (stemming, stopwords removal)
* 📦 Includes model training notebook and dataset

---

## 🚀 How to Run the Project

### 1. Install Dependencies

Make sure you have Python installed. Then run:

```bash
pip install -r requirements.txt
```

### 2. Train the Model (Optional)

If you want to retrain the model, open and run:

```
Model_training.ipynb
```

This will generate `model.pkl` and `vector.pkl`.

### 3. Start the Web App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Fake-News-Detection/
│
├── app.py                    # Streamlit application
├── model.pkl                 # Trained ML model
├── vector.pkl                # TF-IDF vectorizer
├── Model_training.ipynb      # Model training notebook
├── DataSet/                  # Dataset folder
│   ├── train.csv
│   └── test.csv
├── requirements.txt          # Required Python libraries
└── README.md                 # Project documentation
```

---

## ✨ How It Works

1. User enters a news article in the text box
2. Text is cleaned using NLP preprocessing
3. TF-IDF Vectorizer converts text to numeric format
4. Model predicts if the news is **Fake** or **Reliable**

---

## 🧩 Requirements

Make sure `requirements.txt` includes:

```txt
streamlit
scikit-learn
pandas
numpy
nltk
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

Feel free to contribute or modify this project!

⚙️ Developed for educational and research purposes only.

<img width="612" height="597" alt="image" src="https://github.com/user-attachments/assets/1eb69f2f-faad-4ff4-ab7f-09c850cc8661" />

