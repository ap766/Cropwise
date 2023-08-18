import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json

from flask import Flask, request, jsonify, render_template

import pickle

application = Flask(__name__) #Initialize the flask App

model = pickle.load(open('model.pkl', 'rb'))

@application.route('/', methods=['GET'])
def home():
    return render_template('frontpg.html')
#this one
def load_crop_data():
  with open('db.json') as json_file:
       data = json.load(json_file)
       return data

    
@application.route('/predict', methods=['GET'])     
def predict1():
    return render_template('cropp.html')

@application.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    output = prediction[0]
    
    
    crop_data = load_crop_data()
    
   
    if output in list(crop_data.keys()):
       c=crop_data[output]
       print(c)
       
    description=c['description']
    
    print(description)   
    print("Hello")
    print(output)
    
    #return render_template('cropp.html', prediction_text='The crop is {}'.format(output))
    
    d=c["description"]
    tr=c["temperature_range"]
    st=c["soil_type"]
    wr=c["water_requirements"]
    hs=c["harvest_season"]
    f=c["fertilizers"]
    return render_template('cropp.html', prediction_text=output, prediction_text2=d, prediction_text3=tr, prediction_text4=st, prediction_text5=wr, prediction_text6=hs, prediction_text7=f)

# other_value=second_output
@application.route('/about', methods=['GET'])
def about():
  return render_template('about.html')

@application.route('/visualisations', methods=['GET'])
def visualisations():
    return render_template('graph.html')

#route to post the data to generate visualisations
@application.route('/visualisationsubmit', methods=['POST'])
def predict2():
    print("hey")
    int_features = [x for x in request.form.values()]
    a=int_features[0]
    print(a)
    
    

    import pandas as pd


# loading dataset
    data = pd.read_csv('Crop_recommendation.csv')

# draw lineplot
    sns.lineplot(x=a, y="label", data=data)
# save the plot as an image
    plt.savefig('static/graph.png')

    #return render_template('graph.html', prediction_text='The crop is' )
    return render_template('b.html', prediction_text='Crops vs {}'.format(a))




if __name__ == "__main__":
    application.run(debug=True)
