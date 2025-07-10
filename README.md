# Intelligent study manager
# Smart Study Manager 📚

A smart and simple web application to help you manage your study schedule and track your 
academic or professional progress over time. Built with Django and PostgreSQL.

---

## Features

- Create and organize study topics
- Schedule sessions by date and time
- Track your progress (completed vs. pending)
- View weekly and monthly study statistics

---

## Tech Stack

- **Backend**: Django + PostgreSQL
- **Frontend**: Tailwind CSS
- **Authentication**: Django built-in user system
- **Charts**: Chart.js or ApexCharts *(planned)*
- **Deployment**: Render / Railway *(planned)*

---

# Clone the repo
git clone https://github.com/MarianoRochaGarcia/smart-study-manager.git
cd smart-study-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
