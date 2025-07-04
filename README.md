# 🛍️ SnapBuy — Django E-commerce Website

SnapBuy is a fully functional **Django-based online shopping platform**, featuring product listings, shopping cart, user authentication, Razorpay integration, PostgreSQL production database, and live deployment on **Render.com**.

---

## 🚀 Live Demo

**🔗 [Visit SnapBuy Live](https://snapbuy-ecommerce-oqbb.onrender.com)**

---

## ✨ Key Features

- ✅ Browse products & categories
- ✅ Product detail pages
- ✅ Add to cart & checkout
- ✅ Razorpay payment integration
- ✅ User registration & login
- ✅ Admin panel to manage products
- ✅ PostgreSQL in production
- ✅ Whitenoise + Gunicorn for static files & serving
- ✅ Deployed on Render with environment variables

---

## ⚙️ Tech Stack

- **Backend:** Django 5.2
- **Database:** PostgreSQL (production), SQLite (local dev optional)
- **Payments:** Razorpay API
- **Frontend:** HTML5, CSS3, Bootstrap
- **Deployment:** Render.com
- **Server:** Gunicorn + Whitenoise for static files

---

## 📂 Project Structure

SnapBuy/
│
├── ecommerce/ # Project core (settings.py, wsgi.py, asgi.py)
├── store/ # Store app: models, views, templates
├── cart/ # Cart app
├── account/ # User auth app
├── payment/ # Payment app
├── static/ # CSS/JS/Images
├── media/ # Uploaded media files (if local)
├── templates/ # Shared base templates (optional)
├── .env.example # Example environment file
├── requirements.txt # All dependencies
├── manage.py
├── .gitignore
└── README.md

---

## 📑 Example `.env` File

**Never commit your real `.env`!**  
Use a `.env.example` with **placeholder values**:

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=snapbuy-ecommerce-oqbb.onrender.com,127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=https://snapbuy-ecommerce-oqbb.onrender.com,http://127.0.0.1:8000

# PostgreSQL Render database credentials
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=your_db_host
POSTGRES_PORT=5432

# Email (Gmail example)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Razorpay
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret

⚡ Local Development — Quickstart
Follow these steps to run SnapBuy on your local machine:

# 1️⃣ Clone repo
git clone https://github.com/YOUR_USERNAME/SnapBuy.git
cd SnapBuy

# 2️⃣ Create & activate virtual env
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Copy .env.example -> .env and fill your local values

# 5️⃣ Run migrations
python manage.py migrate

# 6️⃣ Create superuser (for admin)
python manage.py createsuperuser

# 7️⃣ Collect static files
python manage.py collectstatic

# 8️⃣ Start dev server
python manage.py runserver

# Visit:
http://127.0.0.1:8000

⚙️ Django Admin Panel
URL: /admin/

Login: Use your created superuser credentials.

Add & edit products, categories, orders.

🗂️ Deployment — Render.com
Production uses:

Gunicorn WSGI server (gunicorn ecommerce.wsgi:application)

Whitenoise for static files (STATIC_ROOT + collectstatic)

PostgreSQL (managed by Render)

.env for secrets & keys

⚡ Quick Deployment Steps:
1️⃣ Push code to GitHub
2️⃣ Connect repo to Render
3️⃣ Add environment variables in Render Dashboard
4️⃣ Build Command:

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

5️⃣ Start Command:

gunicorn ecommerce.wsgi:application

✅ Deployment Tips
Use PostgreSQL in production, SQLite for local dev (optional)

DEBUG = False in production

Keep .env safe (never push secrets)

Use psycopg2-binary for PostgreSQL driver

Ensure STATICFILES_STORAGE is set for Whitenoise

📧 Contact
Created by Mohammed Faizan
Open for feedback or collaboration!
