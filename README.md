# 🚀 Bright-Path Debt Optimizer (SDE Intern Project)

A high-performance Debt Paydown Simulation API built with **Python** and **Django**. This project solves the complex financial problem of debt optimization using data-driven algorithms.

---

## 🏗 High-Level Design (HLD)
Designed for scalability and reliability, mirroring fintech production environments:

* **API Layer:** Uses **Django REST Framework (DRF)** to handle incoming financial data requests.
* **Business Logic Engine:** A decoupled computational module (`engine.py`) that runs simulations without blocking the main thread.
* **Database Schema:** ACID-compliant **PostgreSQL/SQLite** setup ensures 100% data integrity for financial records.



---

## 🛠 Low-Level Design (LLD) & OOPS
The project utilizes advanced software engineering patterns:

* **Strategy Design Pattern:** Used in the `engine.py` to allow seamless switching between "Debt Avalanche" and "Debt Snowball" algorithms.
* **Encapsulation:** Debt entities are modeled as Python objects with strict validation via Serializers.
* **Financial Precision:** Utilizes the `Decimal` type instead of `Float` to prevent rounding errors in interest compounding—a critical requirement for banking software.

---

## 💾 DBMS & Data Integrity
* **Relational Mapping:** Implemented a structured `Debt` model to store balance, APR, and payment terms.
* **Migrations:** Managed via Django’s migration system to ensure version-controlled database evolution.

---

## 🚀 Getting Started
1. **Clone & Install:** `pip install -r requirements.txt`
2. **Setup Database:**
   `python manage.py makemigrations`
   `python manage.py migrate`
3. **Run Server:**
   `python manage.py runserver`