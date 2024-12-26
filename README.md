# Food-distribution-tracker

The Food Distribution Tracker is a Python Flask-based application designed to help organizations efficiently manage food inventory, donors, and distribution to minimize waste and ensure equitable food distribution.

# NB: I am still going on with the project to completion

---

## Features

- Manage food inventory and donations.
- Track distributions to beneficiaries.
- Generate reports on food usage and impact.
- User-friendly interface for administrators and volunteers.

---

## Requirements

- Python 3.8 or higher
- Flask
- Virtual Environment (venv)
- MySQL (or other database, configurable)
- Mysqlachemy

---

## Installation

### Step 1: Clone the Repository
```bash
# Clone the repository from GitHub
$ git clone https://github.com/username/food-distribution-tracker.git

# Navigate into the project directory
$ cd food-distribution-tracker
```

### Step 2: Set Up a Virtual Environment

1. **Create a Virtual Environment:**
   ```bash
   # Create a virtual environment
   $ python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**
   - On **Linux/MacOS**:
     ```bash
     $ source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     $ venv\Scripts\activate
     ```

3. **Ensure the Virtual Environment is Activated:**
   - Your terminal should show `(venv)` at the beginning of the line.

### Step 3: Install Dependencies
```bash
# Upgrade pip to the latest version
$ pip install --upgrade pip

# Install project dependencies
$ pip install -r requirements.txt
```

### Step 4: Configure the Database
1. **Set Up MySQL Database:**
   - Create a new database named `food_distribution_tracker`.
   - Note the username, password, and host details.

2. **Update Configuration File:**
   - Open the `.env` file (or create one) in the project root and set the following:
     ```env
     DATABASE_URI=mysql+pymysql://<username>:<password>@<host>/<database_name>
     SECRET_KEY=<your_secret_key>
     ```

3. **Apply Database Migrations:**
   ```bash
   $ flask db upgrade
   ```

### Step 5: Run the Application
```bash
# Start the Flask development server
$ ./app.py  to run the app in the terminal
```

- The application will be accessible at `http://127.0.0.1:5000/`.

---

## Folder Structure
```
food-distribution-tracker/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   └── static/
├── migrations/
├── requirements.txt
├── app.py
├── .env
└── README.md
```

---

## Development Workflow

1. **Adding Dependencies:**
   - Install the required package using pip.
     ```bash
     $ pip install <package_name>
     ```
   - Update `requirements.txt`:
     ```bash
     $ pip freeze > requirements.txt
     ```

2. **Database Migrations:**
   - Create migrations for new models:
     ```bash
     $ flask db migrate -m "Migration message"
     ```
   - Apply migrations:
     ```bash
     $ flask db upgrade
     ```

3. **Testing:**
   - Run unit tests:
     ```bash
     $ pytest
     ```

---

## Contributing

1. Fork the repository.
2. Create a new branch:

For any queries contact at aloopaul6@gmail.com 


