# 📝 Blog Post Project

A simple **Blog Post Web Application** built with **Python 3.11** and **Django 5.2.5**.  
Users can register, create blog posts, update them, and delete them with confirmation.  
Pagination is implemented for post listings, and posts can also be filtered by author.  

---

## ⚡ Features
- User registration & authentication (login/logout).
- Create, Read, Update, and Delete (CRUD) blog posts.
- Pagination (3 posts per page).
- View all posts by a specific author.
- Confirmation pop-up before deleting posts.
- Clean and responsive UI with Bootstrap.
- Error handling for non-existing posts.

---

## 🛠️ Tech Stack
- **Backend**: Python 3.11, Django 5.2.5
- **Database**: SQLite (default) — can be swapped with PostgreSQL/MySQL.
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Version Control**: Git & GitHub

### Important Note
- Please make `DEBUG=False` inside settings.py file before deploying to production

---

## 📦 Installation & Setup

### 1. Clone the repository
git clone https://github.com/santosh12197/Blog.git

### 2. Go to project folder on local machine
cd blog-post-project

### 3. create and then activate virtual env
python3.11 -m venv venv <br>
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Run migrations command to sync db
python manage.py makemigrations <br>
python manage.py migrate

### 6. Run the development server
python manage.py runserver


