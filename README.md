# 🏠 House Price Prediction Web Application
A full-stack web application that predicts house prices using a Machine Learning model integrated into a web interface. This project combines **Django (backend)** and **Linear Regression (ML model)** to provide users with accurate housing price predictions based on input features.

---
## 🚀 Features

* 📊 Predict house prices using a trained **Linear Regression model**
* 🌐 Interactive web interface using HTML, CSS, and JavaScript
* 🔐 User authentication (Login & Register system)
* 📁 Organized project structure with Django apps
* 📈 Real dataset (`USA_Housing.csv`) for training and predictions
* 📦 Modular and scalable codebase

---
## 🛠️ Tech Stack

**Frontend:**
* HTML5
* CSS3
* JavaScript

**Backend:**
* Python
* Django

**Machine Learning:**
* Linear Regression
* Pandas, NumPy, Scikit-learn

**Database:**
* SQLite3
---

## 📂 Project Structure
```
BuynSellHouse/
│
├── BuynSellHouse/        # Main Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                 # Main application logic
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── regression_model.py   # ML model implementation
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── USA_Housing.csv       # Dataset
│
├── templates/enroll/     # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── prediction.html
│   ├── sell.html
│   ├── about.html
│   ├── contact.html
│   ├── header.html
│   └── footer.html
│
├── static/enroll/        # Static files
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/                # Uploaded media files
├── db.sqlite3            # Database
├── manage.py             # Django management script
└── text.md               # Additional notes
```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
*(If requirements.txt is not available, install manually: Django, pandas, numpy, scikit-learn)*

---
### 4️⃣ Run migrations
```bash
python manage.py migrate
```
### 5️⃣ Start the server
```bash
python manage.py runserver
```
### 6️⃣ Open in browser
```
http://127.0.0.1:8000/
```

## How It Works
1. User enters property details (area, location factors, etc.)
2. Data is sent to backend via Django views
3. `regression_model.py` processes the input
4. ML model predicts the house price
5. Result is displayed on the UI

---
## Author
Varsha Rajput

* Computer Science Student
* Passionate about Web Development & Machine Learning

---
## Acknowledgment
This project is built as part of learning and applying:

* Machine Learning concepts
* Django web development
* Full-stack integration

---
## Note
This project is intended for educational purposes and demonstrates the integration of ML models into web applications.

---

💡 *If you like this project, don’t forget to star the repository!*
