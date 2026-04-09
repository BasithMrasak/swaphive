# Swaphive 🚀

A full-stack web application built with Django (backend) and React (frontend).

---

## 🛠 Tech Stack

* Backend: Django + PostgreSQL
* Frontend: React (Vite)
* API: REST

---

## 📥 Clone the Repository

```bash
git clone https://github.com/BasithMrasak/swaphive.git
cd swaphive
```

---

## ⚙️ Backend Setup

```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=swaphive_db
DB_USER=swaphive_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 🗄️ Database Setup (PostgreSQL)

```sql
CREATE DATABASE swaphive_db;
CREATE USER swaphive_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE swaphive_db TO swaphive_user;
GRANT ALL ON SCHEMA public TO swaphive_user;
```

---

## ▶️ Run Backend

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Backend runs at:
http://127.0.0.1:8000/

---

## 🎨 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
http://localhost:5173/

---

## 🌐 API Endpoints

* `/api/auth/`
* `/api/matching/`
* `/api/sessions/`
* `/api/messages/`
* `/api/dashboard/`

---

## 🔁 Development Workflow

```bash
git checkout -b feature/your-feature-name
git add .
git commit -m "Add: feature description"
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

---

## 🚫 Rules

* Do NOT commit `.env`
* Do NOT commit `venv/` or `node_modules/`
* Do NOT push directly to `main`
* Always use feature branches

---

## 🆘 Common Issues

### PowerShell npm error

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### PostgreSQL permission error

```sql
GRANT ALL ON SCHEMA public TO swaphive_user;
```

---

## 👨‍💻 You're Ready!

Happy coding 🚀
