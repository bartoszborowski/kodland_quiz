import os

from flask import Flask

from kodland_quiz.auth import bp as auth_bp
from kodland_quiz.config import config, logger
from kodland_quiz.db import Question, db
from kodland_quiz.quiz import bp as quiz_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, config.database_name),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{config.database_name}",
    )

    try:
        os.makedirs(app.instance_path)

    except OSError:
        logger.info("Instance directory exists")

    db.init_app(app=app)

    with app.app_context():
        db.create_all()
        logger.info("DB Created")

        questions = Question.query.all()

        # Add sample questions in case of empty database
        if not questions:
            questions_to_add = []

            for question in questions_dict["questions"]:
                question_to_add = Question(
                    question_text=question["question_text"],
                    correct_answer=question["correct"],
                    answer1=question["answers"][0],
                    answer2=question["answers"][1],
                    answer3=question["answers"][2],
                )
                questions_to_add.append(question_to_add)
            db.session.bulk_save_objects(questions_to_add)
            db.session.commit()

    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    app.add_url_rule("/", endpoint="index")

    return app


questions_dict = {
    "topic": "Artificial Intelligence Development in Python",
    "questions": [
        {
            "question_text": "What is Python used for in Artificial Intelligence?",
            "answers": [
                "Building robots only",
                "Creating programs that can learn and think",
                "Making computer games only",
            ],
            "correct": "Creating programs that can learn and think",
        },
        {
            "question_text": "What is Artificial Intelligence (AI)?",
            "answers": [
                "A type of pizza",
                "A robot superhero",
                "A way for computers to solve problems like humans",
            ],
            "correct": "A way for computers to solve problems like humans",
        },
        {
            "question_text": "Which Python library is popular for AI and machine learning?",
            "answers": ["NumPy", "Pandas", "TensorFlow"],
            "correct": "TensorFlow",
        },
        {
            "question_text": "What does AI stand for?",
            "answers": ["Artificial Ice", "Artificial Intelligence", "Animal Instinct"],
            "correct": "Artificial Intelligence",
        },
        {
            "question_text": "What is a Python 'if' statement used for in AI?",
            "answers": [
                "To make decisions based on conditions",
                "To draw shapes",
                "To count numbers",
            ],
            "correct": "To make decisions based on conditions",
        },
        {
            "question_text": "Which is an example of AI in action?",
            "answers": [
                "A calculator doing math",
                "A chatbot answering your questions",
                "Watching a movie",
            ],
            "correct": "A chatbot answering your questions",
        },
        {
            "question_text": "What is a dataset in AI?",
            "answers": [
                "A group of data used for training AI models",
                "A collection of chairs and tables",
                "A type of computer",
            ],
            "correct": "A group of data used for training AI models",
        },
        {
            "question_text": "Why is Python a good choice for AI?",
            "answers": [
                "It's easy to learn and has powerful libraries",
                "It looks cool on the screen",
                "It is the fastest programming language",
            ],
            "correct": "It's easy to learn and has powerful libraries",
        },
        {
            "question_text": "What is a neural network in AI?",
            "answers": [
                "A type of road map",
                "A computer program inspired by the human brain",
                "A game for kids",
            ],
            "correct": "A computer program inspired by the human brain",
        },
        {
            "question_text": "What is a key skill for using AI in Python?",
            "answers": [
                "Understanding how to ride a bike",
                "Knowing how to write code",
                "Singing well",
            ],
            "correct": "Knowing how to write code",
        },
    ],
}
