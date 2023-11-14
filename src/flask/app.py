from flask import Flask
from flask import render_template, request
import pickle



app = Flask(__name__, static_folder="staticFiles")

@app.route('/')
#@app.route('/index')
def index(): 
    return render_template('index.html')

#@app.route('/predict')
@app.route('/', methods = ['POST'])
def getvalue():
    review = request.form['name']
    option = request.form['menu']
   # model = pickle.load(open('ca337-nb-model.pkl','rb'))
    if option == "MultinomialNB":
        model = pickle.load(open('ca337-nb-model.pkl','rb'))
    elif option == "LogisticRegression":
       # option == LogisticRegression
        model = pickle.load(open('logistic_regression.pkl','rb'))
    elif option == "RandomForestClassifier":
        model = pickle.load(open('Random_forest.pkl','rb'))
    features = pickle.load(open('ca337-nb-features.pkl','rb'))
    prediction = model.predict(features.transform([review]))[0]
    if prediction == 1 and option == "MultinomialNB":
        return render_template('predict.html', Review= ('Review: ' + review), result =("MultinomialNB Classifier Prediction: Postive"))
    elif prediction == 1 and option == "LogisticRegression":
        return render_template('predict.html', Review= ('Review: ' + review), result =("Logistic Regression Classifier Prediction: Postive"))
    elif prediction == 1 and option == "RandomForestClassifier":
        return render_template('predict.html', Review= ('Review: ' + review), result =("Random Forest Classifier Prediction: Postive"))
    elif prediction == 0 and option == "MultinomialNB":
        return render_template('predict.html', Review= ('Review: ' + review), result =("MultinomialNB Classifier Prediction: Negative"))
    elif prediction == 0 and option == "LogisticRegression":
        return render_template('predict.html', Review= ('Review: ' + review), result =("Logistic Regression Classifier Prediction: Negative"))
    elif prediction == 0 and option == "RandomForestClassifier":
        return render_template('predict.html', Review= ('Review: ' + review), result =("Random Forest Classifier Prediction: Negative"))
#return render_template('pass.html', n=review)

app.run(host='0.0.0.0', port=5000)
