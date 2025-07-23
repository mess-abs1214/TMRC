
# 🧩 Meisum Abbas — Task 4 (TMRC)

This project is part of TMRC training. It demonstrates how to build RESTful APIs in Django using the Django REST Framework.

---

## 🚀 Project Goals

- Set up a Django project & app  
- Create a model with constraints  
- Use Django REST Framework for API development  
- Perform CRUD operations  
- Test APIs with Postman  
- Use version control with `.gitignore` and virtual environments  

---

## 📁 Folder Structure

```
Meisum_Abbas_Task_4_TMRC/
│
├── myproject/              # Main Django project
│   └── settings.py         # Project settings
│
├── myapp/                  # Django app (API logic)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
│
├── db.sqlite3              # SQLite3 database (default)
├── manage.py               # Django command-line utility
├── requirements.txt        # Dependencies
└── .gitignore              # Ignored files
```

---

## 🛠️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mess-abs1214/TMRC.git
cd TMRC/Meisum_Abbas_Task_4_TMRC
```

---

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
```

Then activate it:

- **Windows:** `venv\Scripts\activate`  
- **Mac/Linux:** `source venv/bin/activate`

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Visit in browser: [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)

---

### 6️⃣ Access Admin Panel (Optional)

1. Create admin user:

```bash
python manage.py createsuperuser
```

2. Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 API Endpoints (Test with Postman)

| Method | Endpoint               | Description         |
|--------|------------------------|---------------------|
| GET    | `/api/products/`       | List all products   |
| POST   | `/api/products/`       | Create new product  |
| GET    | `/api/products/<id>/`  | Get product by ID   |
| PUT    | `/api/products/<id>/`  | Full update         |
| PATCH  | `/api/products/<id>/`  | Partial update      |
| DELETE | `/api/products/<id>/`  | Delete product      |

---

## 📦 Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  
- SQLite3 (default DB)

---

## 🔎 Key Concepts

- **Virtual Environment**: Keeps project dependencies isolated  
- **`.gitignore`**: Prevents uploading unnecessary files (e.g., `venv/`, `.pyc`, `db.sqlite3`)  
- **Serializers**: Convert model data to JSON & validate input  
- **PUT vs PATCH**:  
  - `PUT` = Replace entire record  
  - `PATCH` = Update only specific fields  

---

## 🙋 Contact

Created by **Meisum Abbas**  
GitHub: [mess-abs1214](https://github.com/mess-abs1214)
