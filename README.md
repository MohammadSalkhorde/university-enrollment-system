# 🎓 University Enrollment System

The **University Enrollment System** is a web-based platform designed to manage the university course registration process.
This project is developed with a strong focus on **SOLID principles**, **Clean Architecture**, and **high security standards**.

---

## 📌 Project Description

This system provides a comprehensive solution for managing course selection at a university.
It allows administrators to manage courses and academic rules, students to select courses intelligently with automatic validation, and professors to manage their assigned courses and enrolled students.

The platform supports three main roles:

* **Administrator**
* **Student**
* **Professor**

---

## 🛠 Technology Stack

### Backend

* **Python**
* **Django 5.x / 6.x**
* **Django REST Framework**
* **JWT Authentication** using `djangorestframework-simplejwt`

### Database

* **SQLite**

### Frontend

* **HTML5**
* **CSS3** (RTL support)
* **FontAwesome 6**

### Architecture

* Modular **App-Based Architecture**
* Clean Code & **SOLID Principles**
* Role-Based Access Control (RBAC)

---

## ✨ Implemented Features

### 👨‍💼 Admin Panel

* **Course Management (CRUD):**

  * Create, update, and delete courses with full details
* **Prerequisite Management:**

  * Define prerequisite courses for each course
* **System Settings:**

  * Configure minimum and maximum allowed credits per semester

---

### 🎓 Student Panel

* **Smart Course Search:**

  * Search courses by course name or professor name
* **Enrollment Validation Logic:**

  * Automatic validation of multiple rules, including:

    * Time conflicts
    * Course prerequisites
    * Course capacity
    * Duplicate course selection
    * Credit limits
* **Visual Weekly Schedule:**

  * 5-day timetable view of the student’s weekly schedule
* **Course Management:**

  * Ability to remove selected courses during the current semester

---

### 👨‍🏫 Professor Panel

* **Assigned Courses View:**

  * View courses assigned to the professor
* **Student Management:**

  * View enrolled students for each course (sorted by last name)
* **Professor Permissions:**

  * Ability to remove a student from a course

---

## 🚀 Installation and Execution Guide

Follow the steps below to run the project locally:

### 1️⃣ Navigate to the Project Directory

```bash
cd university_project
```

### 2️⃣ Install Required Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt django-filter
```

### 3️⃣ Prepare the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create an Admin User (Superuser)

```bash
python manage.py createsuperuser
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

After running the server, access the project at:

```
http://127.0.0.1:8000/
```

---

## 🧪 Running Unit Tests

To verify the correctness of the student enrollment logic, run:

```bash
python manage.py test apps.students
```

---

## 📂 Project Structure

```
├── apps/
│   ├── accounts/     # User management and authentication
│   ├── courses/      # Course management and admin settings
│   ├── students/     # Student panel and enrollment logic
│   └── professors/   # Professor panel and student lists
├── static/           # Static files (CSS, fonts, icons)
├── templates/        # HTML templates (RTL supported)
└── manage.py         # Main Django project file
```

---

## 🔐 Security Features

* JWT-based authentication
* Role-based access control
* Secure API endpoints
* Server-side validation for all enrollment rules

---

## 📝 Notes

* SQLite is used for simplicity and development purposes.
* The project can be easily extended to use PostgreSQL or MySQL.
* This system is intended for educational and academic use.

---

## ✅ Conclusion

This project demonstrates a complete university course enrollment system with clean architecture, modular design, and robust validation logic.
It is suitable for academic evaluation and can be extended for real-world university systems.

---

**Author:**
University Course Enrollment System – Student Project
