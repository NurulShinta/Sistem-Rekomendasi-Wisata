# import pycaret
# import sklearn
from model_ds import Predik
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
# from pycaret.classification import *
#
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/ho", methods=['GET', 'POST'])
def form_m():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('index_ds.html')

@app.route("/predict", methods=["POST"])
def predict():
    # menangkap data yang diinput user melalui form
    Rating = float(request.form['Rating'])
    Ulasan = int(request.form['Ulasan'])
    rata2_tiket = int(request.form['rata2_tiket'])

    # melakukan prediksi menggunakan model yang telah dibuat
    data= [[Rating, Ulasan, rata2_tiket]]
    # new_data = pd.DataFrame(data, columns=['Rating','Ulasan','rata2_tiket'])
    Tempat, Tipe = Predik(data)
    return render_template("index_ds.html", rec_str=Tipe, rec=Tempat)


@app.route("/alam", methods=['GET', 'POST'])
def portofolioalam():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('portfolio-details.html')

@app.route("/buatan", methods=['GET', 'POST'])
def portofoliobuatan():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('portfolio-details1.html')

@app.route("/alambuatan", methods=['GET', 'POST'])
def portofolioalambuatan():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('portfolio-details2.html')

@app.route("/budaya", methods=['GET', 'POST'])
def portofoliobudaya():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('portfolio-details3.html')

@app.route("/agrowisata", methods=['GET', 'POST'])
def portofolioagrowisata():
    if request.method == 'POST':
        return redirect(url_for('index.html'))

    return render_template('portfolio-details4.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)