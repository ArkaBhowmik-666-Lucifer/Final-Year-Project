from flask import Flask, jsonify, request
import pickle
import numpy as np

model = pickle.load(open('RandomForest.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict', methods=['POST'])
def predict():
    ph = float(request.form.get('ph'))
    rainfall = float(request.form.get('rainfall'))
    temperature, humidity = float(request.form.get('temperature')), float(request.form.get('humidity'))

    input_query = np.array([[temperature, humidity, ph, rainfall]])
    my_prediction = model.predict(input_query)
    final_prediction = my_prediction[0]

    return jsonify({'Recommended Crop':final_prediction})

    # recom = {'ph':ph, 'rainfall':rainfall, 'temperature': temperature, 'humidity':humidity}
    # return jsonify(recom) 

if __name__ =='__main__':
    app.run(debug=True)