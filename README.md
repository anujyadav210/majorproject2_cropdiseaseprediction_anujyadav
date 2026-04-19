# majorproject2_cropdiseaseprediction_anujyadav
Crop Disease Prediction AI System

A deep learning-based web application that helps farmers and users identify crop diseases by simply uploading an image of the plant leaf. The system uses a trained CNN model (MobileNetV2) and provides quick predictions along with a clean, user-friendly interface.

 Features:
 Crop & Disease Prediction using AI
 Upload leaf images for instant analysis
 User Authentication System (Login/Register)
 Stores farmer details (mobile, Aadhaar, crops)
 Interactive Dashboard UI
 Disease Information Page with knowledge base
 Modern premium UI (glassmorphism + gradient design)
 Fast predictions using optimized model

 Tech Stack:
Technology	Usage
Python	Backend logic
Flask	Web framework
TensorFlow / Keras	Deep learning model
MobileNetV2	Transfer learning model
HTML/CSS	Frontend
SQLite	Database
JavaScript	Image preview

📂 Project Structure:
project/
│
├── app.py
├── final_model1.keras
├── class_names1.pkl
├── users.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── diseases.html
│
├── static/
│   ├── style.css
│   └── uploads/
│
└── README.md

 
 How It Works:
User registers/login into the system
Uploads a crop leaf image
Image is:
Resized to 160x160
Preprocessed
Model predicts disease using trained CNN
Result displayed on dashboard

 
 Model Details:
Architecture: MobileNetV2 (Transfer Learning)
Input Size: 160 x 160
Dataset: PlantVillage Dataset
Output: Crop + Disease classification

 
 Installation & Setup:
1️ Clone the repository
git clone https://github.com/yourusername/crop-disease-prediction.git
cd crop-disease-prediction
2️⃣ Install dependencies
pip install flask tensorflow numpy pillow
3️⃣ Run the application
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000/

 Login System
New users must register first
After registration → redirected to login
Error messages shown for incorrect login


 Known Limitations:
Model may predict same class if:
Training is insufficient
Dataset imbalance exists
Works best on clear leaf images
Requires improvement for real-world robustness


 Author:
Anuj Yadav
📌 Crop Disease Prediction AI System
© 2026 All Rights Reserved

⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share with others

📜 License

This project is for academic and educational purposes only.
