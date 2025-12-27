
from flask import Flask, render_template, request
import pickle
from resume_parser import extract_text

app = Flask(__name__)

model = pickle.load(open("model/personality_model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["resume"]
        text = extract_text(file)
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)
        result = prediction[0]
    return render_template("index.html", result=result)

if __name__ == "__main__":
   app.run(host="127.0.0.1", port=8000, debug=True)
