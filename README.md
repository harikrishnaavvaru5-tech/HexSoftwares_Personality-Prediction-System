# HexSoftwares_Personality-Prediction-System

📄 Personality Prediction System Through CV Analysis
📌 Overview

This project is a Machine Learning-based Personality Prediction System that analyzes a candidate’s resume (CV) and predicts personality traits using Natural Language Processing (NLP).

The system processes textual data from resumes and maps it to personality categories based on learned patterns, helping recruiters make better hiring decisions.

🎯 Features

📄 Resume text analysis

🧹 Text preprocessing using NLP

🔍 Feature extraction using TF-IDF

🤖 Pre-trained ML model for prediction

📊 Personality classification output

🧠 Personality Prediction

The model predicts personality traits based on resume content.
These predictions are derived from patterns in language, skills, and experience mentioned in the CV.

⚙️ Tech Stack

Python

Scikit-learn

NLTK

Pandas / NumPy

Pickle (for model storage)

📂 Project Structure
HexSoftwares_Personality-Prediction-System/
│
├── main.py # Main execution file
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── dataset.csv # Training dataset
├── requirements.txt # Dependencies
└── README.md # Project documentation
⚙️ How It Works

User provides resume text

Text is cleaned and preprocessed

TF-IDF vectorizer converts text into numerical features

Pre-trained model (model.pkl) predicts personality

Output is displayed

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/harikrishnaavvaru5-tech/HexSoftwares_Personality-Prediction-System.git
cd HexSoftwares_Personality-Prediction-System
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
python app.py
🧪 Example Workflow

Input: Resume text

Processing: NLP + TF-IDF

Output: Predicted personality category

📊 Model Details

Algorithm: Machine Learning Classifier (trained and saved as model.pkl)

Feature Extraction: TF-IDF (vectorizer.pkl)

Training Data: dataset.csv

⚠️ Limitations

Depends on dataset quality

Resume text may not fully represent personality

Predictions are approximate

🔮 Future Improvements

Add web interface (Flask / Streamlit)

Use deep learning (BERT)

Improve dataset accuracy

Add PDF resume upload

🤝 Contributing

Feel free to fork the repo and submit pull requests.

📜 License

This project is open-source and available under the MIT License.

⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
