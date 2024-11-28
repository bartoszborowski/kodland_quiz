import json
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
            with open("kodland_quiz/sample_questions.json", "r") as file:
                questions_dict = json.load(file)
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
