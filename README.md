# Career Recommendation System 🎯

🌐 **Live Demo:** https://careerapp-hxco.onrender.com  

A complete machine learning based web application that helps users identify suitable career paths based on their skills, interests, and academic background.

This project combines data science with a real-time web interface to deliver intelligent and personalized career guidance.

---

## 📌 Project Motivation

Many students struggle to choose the right career direction due to lack of proper guidance and personalized insights.  
This system aims to solve that problem using machine learning predictions instead of generic advice.

---

## ⚙️ What We Built

✔ Trained a machine learning model to analyze user inputs  
✔ Developed a Flask backend to serve predictions  
✔ Designed a responsive web interface  
✔ Integrated ML model with real-time user interaction  

---

## 🚀 Key Features

- Personalized career recommendations  
- Real-time ML predictions  
- Clean and intuitive UI  
- Lightweight Flask backend  
- Scalable architecture  

---

## 🛠 Technologies Used

- Python  
- Flask  
- Scikit-learn  
- HTML, CSS, JavaScript  

---

## 📁 Project Structure
Careerapp/
│── app.py                ← Flask backend (main server)
│── requirements.txt     ← deployment dependencies
│── README.md            ← project description + live demo
│── logic/
│   └── career_engine.py ← ML logic
│
│── templates/           ← HTML pages (Flask renders these)
│   ├── home.html
│   ├── after10th.html
│   ├── after12th.html
│   ├── engineering.html
│   ├── medical.html
│   └── result.html
│
│── static/
│   ├── css/style.css
│   └── images/bg.jpg



---

## ▶ How to Run Locally

```bash
pip install -r requirements.txt
python app.py

