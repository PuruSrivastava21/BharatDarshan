# 🇮🇳 BharatDarshan — Indian Cultural Showcase Platform

**BharatDarshan** is a Django-based cultural blog platform that celebrates India's heritage, festivals, and traditional art forms.  
It allows users to explore rich cultural content and authenticated users to create & manage posts.

This was my first Django project, built to learn full-stack web development using Python & Django 🙌.

---

## ✨ Features

- 🏛️ Browse Indian heritage sites, festivals & art forms  
- ✍️ Add cultural posts (only logged-in users)  
- 🔐 User authentication (Login & Logout)
- 🗑️ Delete post option with trash-icon button  
- 📸 Image upload for posts  
- 🎨 Modern UI with smooth hover effects & responsive cards  
- 📂 Organized Django structure (models, views, templates)  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Backend logic |
| Django | Web framework |
| SQLite | Default database |
| HTML / CSS / JS | Front-end UI |
| Bootstrap styling & custom CSS | UI/UX |
| Django Auth | User login/logout |

---

## 📁 Project Structure

bharatdarshan/
├── bharatdarshan/ # Main project settings
├── culture/ # App (models, views, urls)
├── templates/ # Base templates folder
│ └── base.html
├── media/ # Uploaded images
├── db.sqlite3
├── manage.py


---

## 🚀 Setup Instructions

### ✅ 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/BharatDarshan.git
cd BharatDarshan


Create virtual environment & install requirements

python -m venv venv
source venv/Scripts/activate   # Windows
# or
source venv/bin/activate       # Mac/Linux

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

🎯 What I Learned

Django MVC (MVT) architecture

Models, Views, Templates structure

Django ORM & migrations

File uploads & media handling

Login/logout authentication

Handling template inheritance ({% extends %} & {% block %})

Improving UI using CSS & JS

Deploy-ready file structure & environment setup

🤝 Contributing

Feel free to fork this repo & contribute.
Pull requests are welcome!

📜 License

This project is open-source for learning purposes.

Built with ❤️ as my first Django project, exploring India's diversity while learning full-stack development.
