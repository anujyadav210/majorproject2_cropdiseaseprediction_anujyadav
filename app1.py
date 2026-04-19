import os
import numpy as np
import sqlite3
import tensorflow as tf
import pickle

from flask import Flask, redirect, request, render_template, session, flash
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------- LOAD MODEL --------
model = tf.keras.models.load_model(
    "final_model1.keras",
    custom_objects={'preprocess_input': preprocess_input}
)

# -------- LOAD CLASS NAMES --------
with open("class_names1.pkl", "rb") as f:
    class_names = pickle.load(f)

# -------- DATABASE --------
def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        mobile TEXT,
        aadhaar TEXT,
        crops TEXT
    )''')
    conn.close()

init_db()

# -------- PREDICTION --------
def model_predict(img_path):
    img = image.load_img(img_path, target_size=(160, 160))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0]
    index = np.argmax(pred)

    result = class_names[index]
    crop, disease = result.split("___")

    return crop, disease.replace("_", " ")

# -------- ROUTES --------

@app.route('/')
def home():
    return redirect('/login')

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        data = cursor.fetchone()
        conn.close()

        if data:
            session['user'] = user
            return redirect('/dashboard')
        else:
            flash("Incorrect login info. If not registered, kindly register yourself.", "error")

    return render_template('login.html')

# REGISTER
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        try:
            conn = sqlite3.connect("users.db")
            conn.execute(
                "INSERT INTO users (username,password,mobile,aadhaar,crops) VALUES (?,?,?,?,?)",
                (
                    request.form['username'],
                    request.form['password'],
                    request.form['mobile'],
                    request.form['aadhaar'],
                    request.form['crops']
                )
            )
            conn.commit()
            conn.close()

            flash("Registration successful! Please login.", "success")
            return redirect('/login')

        except:
            flash("User already exists!", "error")

    return render_template('register.html')

# DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html')

# PREDICT
@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect('/login')

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(file_path)

    crop, disease = model_predict(file_path)

    return render_template('dashboard.html',
                           crop=crop,
                           disease=disease,
                           image_path=file_path)

# DISEASE PAGE
@app.route('/diseases')
def diseases():
    return render_template('diseases.html')

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)