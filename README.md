# Bookstore Management System

A comprehensive, role-based desktop management system built with **Python** and **MySQL**. It features automatic database/table bootstrapping, user and admin authentication, dynamic catalog querying, staff management, and transaction-safe sales handling.

---

## 🚀 Key Features

- **Automated Database Bootstrapping:** Automatically detects and initializes the `bookstore` database and all 5 relational tables (`avail_books`, `staff_details`, `sellrec`, `signup`, `Admin`) on first startup.
- **Role-Based Access Control (RBAC):**
  - **Admin Portal:** Manage available book inventory, hire/remove staff, view sales records, and calculate total store revenue.
  - **Customer Portal:** User registration, credential login, book catalog search, and live book purchasing.
- **Real-Time Transaction & Stock Management:** Validates available stock quantity prior to purchase, logs transactional receipt details, and decrements stock in real-time.
- **Multi-Parameter Search:** Browse and query books dynamically by **Name**, **Genre**, or **Author**.
- **Data Integrity:** Employs primary and foreign key constraints between catalog items and transaction records.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL
- **Connector:** `mysql-connector-python`

---

## 📋 Database Schema

- `avail_books` — Stores book catalog (bookname [PK], genre, qty, author, price)
- `staff_details` — Stores employee profiles (name [PK], gender, age, phno, address)
- `sellrec` — Transaction audit logs (cusname, phno, bookname [FK], qty, price, total_price)
- `signup` — Customer credentials
- `Admin` — Admin credentials
