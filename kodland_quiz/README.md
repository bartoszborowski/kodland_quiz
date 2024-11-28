# Kodland Quiz Application 🎓🤖  

A simple yet engaging quiz application designed to inspire kids and teenagers to dive into **Artificial Intelligence Development in Python**. This project is part of an educational initiative by **Kodland**.

🌐 **Live Demo**: [Kodland Quiz App](https://bbeaver.pythonanywhere.com/)

---

## 🚀 Features
- **Dynamic Questioning**: Randomized order of questions and answers to keep quizzes fresh and exciting.
- **Best Score Tracker**: Displays the user's personal best score prominently on the screen.
- **User Management**:
  - **Register & Login** functionality for personalized quiz tracking.
  - Records and displays the best score for each user across multiple attempts.

---

## 🛠️ Tech Stack
- **Programming Language**: Python  
- **Web Framework**: Flask  
- **Database**: SQLAlchemy with SQLite  
- **Deployment Platform**: [PythonAnywhere](https://pythonanywhere.com/)

---

## 📖 How It Works
1. **Interactive Quiz**:
   - Users are presented with questions and three possible answers.
   - Answer choices are randomized to enhance the learning experience.

2. **User Authentication**:
   - Users can **register** and **log in** to track their scores.

3. **Score Tracking**:
   - The app keeps track of the best score for logged-in users and displays it in the interface.

---

## 📂 Folder Structure
```bash
.
├── kodland_quiz
│   ├── README.md
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── db.py
│   ├── quiz.py
│   ├── sample_questions.json
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── register.html
│       ├── base.html
│       ├── index.html
│       └── results.html
├── poetry.lock
├── pyproject.toml
└── tests
```


## 🖥️ Deployment Instructions
1. **Clone the Repository**:
   ```bash
   git clone git@github.com:bartoszborowski/kodland_quiz.git
   cd kodland_quiz
   ```
2. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    poetry update
    ```
3. **Run the Application Locally**:
    ```bash
    flask --app kodland_quiz run
    ```

4. **Deploy on PythonAnywhere**:
- Upload files to your PythonAnywhere account.
- Configure the wsgi.py file to point to the Flask application.
- Reload the app on the PythonAnywhere dashboard.

# Kodland Quiz Application 🎓🤖  

A simple yet engaging quiz application designed to inspire kids and teenagers to dive into **Artificial Intelligence Development in Python**. This project is part of an educational initiative by **Kodland**.

🌐 **Live Demo**: [Kodland Quiz App](https://bbeaver.pythonanywhere.com/)

---

## 🚀 Features
- **Dynamic Questioning**: Randomized order of questions and answers to keep quizzes fresh and exciting.
- **Best Score Tracker**: Displays the user's personal best score prominently on the screen.
- **User Management**:
  - **Register & Login** functionality for personalized quiz tracking.
  - Records and displays the best score for each user across multiple attempts.

---

## 🛠️ Tech Stack
- **Programming Language**: Python  
- **Web Framework**: Flask  
- **Database**: SQLAlchemy with SQLite  
- **Deployment Platform**: [PythonAnywhere](https://pythonanywhere.com/)

---

## 📖 How It Works
1. **Interactive Quiz**:
   - Users are presented with questions and three possible answers.
   - Answer choices are randomized to enhance the learning experience.

2. **User Authentication**:
   - Users can **register** and **log in** to track their scores.

3. **Score Tracking**:
   - The app keeps track of the best score for logged-in users and displays it in the interface.

---

## 📂 Folder Structure

kodland_quiz/ ├── init.py # Flask application factory ├── auth/ # Authentication blueprint (register/login/logout) ├── quiz/ # Quiz functionality and scoring logic ├── db.py # Database models and initialization ├── config.py # Configuration settings ├── sample_questions.json # Sample AI-related quiz questions ├── templates/ # HTML templates ├── static/ # CSS and static files └── requirements.txt # Required Python packages


---

## 🖥️ Deployment Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd kodland_quiz

    Set Up Virtual Environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the Application Locally:

    flask run

    Deploy on PythonAnywhere:
        Upload files to your PythonAnywhere account.
        Configure the wsgi.py file to point to the Flask application.
        Reload the app on the PythonAnywhere dashboard.

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

Crafted with ❤️ for the next generation of AI developers! 🎉