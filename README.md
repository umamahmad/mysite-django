# 🚀 Django Blog Project

✨ A simple **Blog Web Application** built using **Django**.

This project demonstrates how to create and manage blog posts with an admin panel using Django's powerful ORM and MVC structure.

---

## 🌟 Features

* 📝 Create, edit, and delete blog posts
* 👤 Author-based posts
* 📅 Publish date management
* 🔗 Slug-based URLs
* ⚡ Django Admin integration
* 🗂 Clean project structure

---

## 🛠 Built With

* 🐍 Python
* 🌐 Django
* 🗄 SQLite
* 💻 HTML Templates

---

## 📂 Project Structure

```
mysite-django
│
├── blog
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations
│
├── mysite
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/umamahmad/mysite-django.git
```

Move into the project folder:

```
cd mysite-django
```

Create virtual environment:

```
python -m venv env
```

Activate environment:

```
env\Scripts\activate
```

Install dependencies:

```
pip install django
```

Run migrations:

```
python manage.py migrate
```

Start the development server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧑‍💻 Admin Panel

Create superuser:

```
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin
```

Manage posts directly from the Django admin dashboard.

---

## 📸 Screenshots

(Add screenshots of your project here)

---

## 📚 What I Learned

* Django project structure
* Models and migrations
* Django Admin customization
* URL routing
* Version control with Git & GitHub

---

## 🔐 Environment Variables

Sensitive data like email credentials are stored in:

```
.env
```

These files are ignored using `.gitignore`.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Umam Ahmad**

GitHub:
https://github.com/umamahmad
