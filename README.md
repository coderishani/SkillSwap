# 🚀 SkillSwap

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![Render](https://img.shields.io/badge/Render-Deployed-success?logo=render)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

> A full-stack Django web application for exchanging skills through user profiles, skill listings, and swap requests.

Built using **Python, Django, Bootstrap 5, PostgreSQL and render**.

---

## 🌐 Live Demo

https://skillswap-ezax.onrender.com

## 🔑 Demo

Create your own account using the Sign Up page.

Administrator access is restricted to the project owner.


## ✨ Features

- 🔐 User Authentication (Sign Up, Login, Logout)
- 👤 User Profile Management
- ➕ Add Skills
- ✏️ Edit Skills
- 🗑️ Delete Skills
- 🌍 Browse Skills from Other Users
- 🔍 Search Skills
- 🤝 Send Skill Swap Requests
- ✅ Accept Requests
- ❌ Reject Requests
- 📥 View Incoming Requests
- 📤 View Sent Requests
- 📱 Responsive Bootstrap 5 Interface

---
Tech Stack: 

Backend

- Python
- Django

Frontend

- HTML5
- CSS3
- Bootstrap 5

Database

- PostgreSQL (Production)
- SQLite (Development)

Deployment

- Render

Version Control

- Git
- GitHub

---

## 📸 Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 🔑 Login Page

![Login](screenshots/login.png)

---

### 📝 Sign Up Page

![Signup](screenshots/signup.png)

---

### 🌍 Browse Skills

![Browse Skills](screenshots/browse_skills.png)

---

### 📚 My Skills

![My Skills](screenshots/my_skills.png)

---

### ➕ Add Skill

![Add Skill](screenshots/add_skill.png)

---

### 📥 Incoming Requests

![Incoming Requests](screenshots/incoming_requests.png)

---

### 📤 Sent Requests

![Sent Requests](screenshots/sent_requests.png)

---
Architecture: 

Browser
    │
    ▼
Django URLs
    │
    ▼
Views
    │
    ▼
Models
    │
    ▼
PostgreSQL

## 📂 Project Structure

```text
SkillSwap/
│
├── skills/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── screenshots/
│   ├── home.png
│   ├── login.png
│   ├── signup.png
│   ├── browse_skills.png
│   ├── my_skills.png
│   ├── add_skill.png
│   ├── incoming_requests.png
│   └── sent_requests.png
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/coderishani/SkillSwap.git
```

Move into the project directory:

```bash
cd SkillSwap
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🚀 Future Improvements

Real-time messaging
User ratings
Profile pictures
Notifications
Email verification
Skill recommendations

---
## 📚 What I Learned

Building SkillSwap helped me gain practical experience with:

- Django authentication
- CRUD operations
- Django ORM
- Forms and validation
- User authorization
- Git and GitHub workflow
- PostgreSQL integration
- Render deployment
- Debugging production issues

  ## 🚀 Challenges Faced

Some challenges encountered during development included:

- Configuring PostgreSQL for production
- Deploying Django on Render
- Managing environment variables
- Debugging authentication issues
- Migrating from SQLite to PostgreSQL
  
## 👩‍💻 Author

**Ishani Jain**

- GitHub: https://github.com/coderishani

---

⭐ If you found this project helpful, consider giving it a star!
