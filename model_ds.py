import pickle # For loading model
# import streamlit as st # For web app
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestClassifier

global dataset, model_ds, X, y, X_train, X_test, y_train, y_test, data_test, data_train
# Loading data frame
dataset = pickle.load(open('model/dataPA.pkl', 'rb'))
dataset = pd.DataFrame(dataset)

# Loading similarity file
model_ds = pickle.load(open('model/model_PA.pkl', 'rb'))

X = dataset[['Rating', 'Ulasan', 'rata2_tiket']]
y = dataset['type']

# split the dataset into the training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 786)

data_train = dataset.sample(frac=0.9, random_state=786)
data_test = dataset.drop(data_train.index)

model = RandomForestClassifier()
model.fit(X_train, y_train)

def Predik(data, dataset=dataset):
    # print(f'recomendation Wisata Tujuan: {b}', end='')
    Prediction = model.predict(data)
    rec_str = Prediction.item()[:]
    a = dataset[dataset['type']== rec_str].values
    b = a[:,3]
    rec = b
    return rec_str, rec
    
    