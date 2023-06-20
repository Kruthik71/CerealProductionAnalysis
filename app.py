from flask import Flask, render_template,url_for,redirect,request
import numpy as np
import pandas as pd
import pickle
import subprocess

gross_output = pickle.load(open('gross_output.pkl','rb'))
price = pickle.load(open('mobile_price.pkl','rb'))
Harvesting = pickle.load(open('harvesting_cost1.pkl','rb'))


#wheat_output = pickle.load(open('gross_outputw.pkl','rb'))
#wheat_price = pickle.load(open('mobile_pricew.pkl','rb'))
#wheat_harvest = pickle.load(open('harvesting_costw.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def page():
    return render_template('load.html')

@app.route('/second')
def index():
    return render_template('index.html')

@app.route('/third')
def index1():
    return render_template('index3.html')

@app.route('/predict',methods=['POST'])
def prediction():
    if request.method == 'POST':
        size1 = float(request.form['size'])
        seed1 = float(request.form['seed'])
        urea1 = float(request.form['urea'])
        labor1 = float(request.form['labor'])
        phosphate1 = float(request.form['phosphate'])
        varieties1 =int(request.form['varieties'])
        presticide1=float(request.form['presticide'])
        gross_data=[[size1,seed1,urea1,labor1,phosphate1,varieties1,presticide1]]

        gross_pred = int(gross_output.predict(gross_data)[0])
        Harvesting_pred =int(Harvesting.predict([[gross_pred]])[0])
        return render_template('index1.html',prediction0=gross_pred,prediction1=Harvesting_pred)
    

@app.route('/price',methods=['POST'])
def price_net():
    if request.method =='POST':
        price_seed1 = float(request.form['price_seed'])
        wage1 = float(request.form['wage'])
        price_phos1 = float(request.form['price_phos'])
        Price_urea1 = float(request.form['price_urea'])
        price_data=[[price_seed1, wage1,price_phos1,Price_urea1]]
        
        price_pred=int(price.predict(price_data)[0])

        return render_template('index2.html',prediction2=price_pred)
    

"""
@app.route('/predictwheat',methods=['POST'])
def prediction():
    if request.method == 'POST':
        size1 = float(request.form['size'])
        seed1 = float(request.form['seed'])
        urea1 = float(request.form['urea'])
        labor1 = float(request.form['labor'])
        phosphate1 = float(request.form['phosphate'])
        varieties1 =int(request.form['varieties'])
        presticide1=float(request.form['presticide'])
        gross_data_wheat=[[size1,seed1,urea1,labor1,phosphate1,varieties1,presticide1]]

        gross_pred_wheat = int(wheat_output.predict(gross_data_wheat)[0])
        Harvesting_pred_wheat =int(wheat_harvest.predict([[gross_pred_wheat]])[0])
    
        return render_template('index4.html',pred0=gross_pred_wheat, pred1=Harvesting_pred_wheat)
    

@app.route('/pricewheat',methods=['POST'])
def price_net():
    if request.method =='POST':
        price_seed1 = float(request.form['price_seed'])
        wage1 = float(request.form['wage'])
        price_phos1 = float(request.form['price_phos'])
        Price_urea1 = float(request.form['price_urea'])
        price_data_wheat=[[price_seed1, wage1,price_phos1,Price_urea1]]
        
        price_pred_wheat=int(wheat_price.predict(price_data_wheat)[0])

        return render_template('index5.html',pred2=price_pred_wheat)

@app.route('/invoke-scripts')
def invoke_scripts():
    subprocess.run(['python', 'utils/wheat.py'])
"""

if __name__=='__main__':
    app.run(debug=True)