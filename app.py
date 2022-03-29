
import pickle
from flask import Flask,render_template,url_for,request
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import cross_val_score 
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import scale


app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])

def predict():
    df=pd.read_csv("C:\\Users\\703311085\\Downloads\\My Projects\\BankMarketingPred\\bank.csv")
    df=df.iloc[:,[16,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
    df=pd.get_dummies(df,columns=['job','marital','education','default','housing','loan','contact','month','poutcome'],drop_first=True)
    from sklearn.model_selection import train_test_split
    X=df.iloc[:,1:44]
    df['deposit'] = df['deposit'].map({'no': 0, 'yes': 1})
    y=df.iloc[:,0]
    x=scale(X)
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    from imblearn.over_sampling import SMOTE
    sm=SMOTE(random_state=444)
    X_train_res,y_train_res=sm.fit_resample(X_train,y_train)
    X_train_res.shape
    y_train_res.shape
    X_test.shape
    y_test.shape
    
    from sklearn.ensemble import RandomForestClassifier
    Rf=RandomForestClassifier(n_estimators=100)

    Rf.fit(X_train_res,y_train_res)
    if request.method == 'POST':
        my_prediction=Rf.predict(X_test)
        
        output = round(my_prediction[0], 2)
        if output<0.5:
            return render_template('index1.html',prediction_texts="Sorry The customer cannot subscribe for Term Deposit")
        else:
            return render_template('index1.html',prediction_text="Yay! The customer can subscribe for Term Deposit {}".format(output))
    else:
        return render_template('index1.html',prediction = output)
        print()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)