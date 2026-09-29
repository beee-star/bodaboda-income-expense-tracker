# BIETS: Bodaboda Income and Expense Tracker System

A web application that helps bodaboda (motorcycle taxi) operators in Kenya record their daily income and expenses, and see how their business is really doing.

## The Problem

Many bodaboda riders and owners keep no proper records. Money comes in through many small trips and goes out on fuel, repairs, and fines, so it is hard to know whether the business is profitable or how much can be saved. BIETS gives them one simple place to record and review this information.

## Features

- **Role-based login:** separate access for riders and an admin
- **Income and expense recording:** log daily earnings and costs
- **Dashboard:** an automatic summary of income, expenses, and balance
- **Reports page:** view records over time
- **Profile page:** manage account details
- **Admin panel:** manage users and oversee records

## Built With

- Python and Flask (backend)
- SQLite (database)
- Jinja2 (templates)
- HTML, CSS, and JavaScript (frontend)

## Screenshots

> Add your screenshots here (login page, dashboard, add income/expense form, reports page).

| Login | Dashboard |
|-------|-----------|
| ![Login](screenshots/login.png) | ![Dashboard](screenshots/dashboard.png) |

## How to Run It Locally

1. Install Python 3.
2. Install Flask:
   ```
   pip install flask
   ```
3. From the project folder, start the app:
   ```
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Planned future Improvements

- M-Pesa integration
- SMS/USSD access for riders without smartphones
- Loan repayment tracking
- A Swahili-language interface

## About the Project

BIETS is my final-year project for my Bachelor of Science in Computer Science at Kiriri Women's University of Science and Technology (KWUST). I designed and built both the frontend and the backend.

## Author

**Belta Gathoni Njunje**
Computer Science student, Nairobi, Kenya
bnjunje@gmail.com
