````markdown
# 🔗 URL Shortener

A simple and efficient URL Shortener web application built with Django. This application allows users to convert long URLs into short, shareable links and redirect users to the original destination URL.

---

## 📌 Features

- Shorten long URLs into unique short links
- Redirect users to the original URL
- Store URLs in a database
- User-friendly interface
- Built using Django framework
- Scalable architecture for future enhancements

---

## 🛠️ Tech Stack

- Python 3
- Django
- SQLite
- HTML5
- CSS3
- Git & GitHub

---

## 📂 Project Structure

```text
URLShortener/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/URLShortener.git
cd URLShortener
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 📖 How It Works

1. Enter a long URL into the input field.
2. Click the **Shorten URL** button.
3. The application generates a unique short code.
4. A short URL is displayed.
5. Opening the short URL redirects to the original website.

---

## 📸 Example

### Original URL

```text
https://www.google.com
```

### Generated Short URL

```text
http://127.0.0.1:8000/aB3XyZ
```

---

## 🗄️ Database Model

```python
from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.original_url
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Django Models
* Django Forms
* Django Views
* URL Routing
* Database Integration
* HTTP Redirects
* CRUD Operations
* Python Backend Development
* Git & GitHub Workflow

---

## 🔮 Future Enhancements

* Django REST Framework APIs
* PostgreSQL Integration
* User Authentication
* JWT Authentication
* Click Analytics
* Custom Short URLs
* QR Code Generation
* Docker Deployment
* Cloud Deployment (Render, Railway, AWS)

---

## 💻 Commands Used

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Django

```bash
pip install django
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## 👩‍💻 Author

**Chandana P**


---


```
