from pyexpat import model
from flask import render_template
from flask import Flask, request, Markup
import numpy as np
import pandas as pd
import pickle
import os


crop_recommendation_model_path = 'RandomForest.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))
photos = os.path.join('static','images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = photos

@ app.route('/')
def home():
    title = 'StrawHats - Home'
    filenm = os.path.join(app.config['UPLOAD_FOLDER'],'bg.jpg')
    print(filenm)
    return render_template('index.html',img1_bg = filenm)

@ app.route('/crop_prediction', methods=['POST'])
def crop_prediction():
    title = 'StrawHats - Crop Recommendation'

    if request.method == 'POST':
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        city = request.form.get("city")
        temperature, humidity = float(request.form['temperature']), float(request.form['humidity'])
        data = np.array([[temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return render_template('Crop_result.html', prediction=final_prediction)

if __name__ == '__main__': 
    app.run(debug=True)