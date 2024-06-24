import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application


random_forest_model=pickle.load(open('models/rf_model.pkl','rb'))
# standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Age= float(request.form.get('Age'))
        Sex = float(request.form.get('Sex'))
        Bmi = float(request.form.get('Bmi'))
        Children = float(request.form.get('Children'))
        smoker = float(request.form.get('smoker'))
        Region = float(request.form.get('Region'))

        # new_data_scaled=standard_scaler.transform[[Age,Sex,Bmi,Children,smoker,Region]]
        new_data_scaled = [Age,Sex,Bmi,Children,smoker,Region]
        result = random_forest_model.predict(np.array(new_data_scaled).reshape(1,6))
        print(result)
        return render_template('home.html',result = result[0])
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)
