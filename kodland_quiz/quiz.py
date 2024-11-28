from random import shuffle

from flask import Blueprint, g, render_template, request, session
from sqlalchemy import func

from kodland_quiz.config import logger
from kodland_quiz.db import Question, Score, db

bp = Blueprint("quiz", __name__)


@bp.route("/")
def index():
    questions = Question.query.all()
    question_list = [
        question_object_to_dict(question=question) for question in questions
    ]
    shuffle(question_list)
    return render_template("index.html", question_list=question_list)


@bp.route("/submit", methods=["POST"])
def submit():
    ids_to_fetch = request.form.keys()
    answers = request.form.to_dict()
    questions = Question.query.filter(Question.id.in_(ids_to_fetch)).all()

    score = 0

    for question in questions:
        answered = answers.get(str(question.id))
        if answered == question.correct_answer:
            score += 1

    scored = round(score / len(questions) * 100)

    # Load the best score from session
    best_score = session.get("best_score", 0)

    # Update best score if the current score is higher
    if scored > best_score:
        session["best_score"] = scored  # Store the new best score in session
        best_score = scored  # Update the local variable

    return render_template("results.html", scored=scored, best_score=best_score)


def question_object_to_dict(question: Question) -> dict:
    answers = [question.answer1, question.answer2, question.answer3]
    shuffle(answers)
    question_dict = {
        "id": question.id,
        "question_text": question.question_text,
        "answers": answers,
        "correct_answer": question.correct_answer,
    }

    return question_dict


@bp.before_app_request
def load_logged_in_user():
    # Get best score from the session
    best_score = session.get("best_score")
    user_id = session.get("user_id")

    # Default to 0 if no best score exists in the session
    if best_score is None:
        g.best_score = 0
    else:
        # Set the best score in the global object
        g.best_score = best_score

    if user_id:
        personal_best_score = (
            db.session.query(func.max(Score.score)).filter_by(user_id=user_id).scalar()
        )

        logger.info(personal_best_score)

        if personal_best_score is not None:
            if personal_best_score > g.best_score:
                g.best_score = personal_best_score

            if g.best_score > personal_best_score:
                user_new_best = Score(score=g.best_score, user_id=user_id)
                db.session.add(user_new_best)
                db.session.commit()
        else:
            user_new_best = Score(score=g.best_score, user_id=user_id)
            db.session.add(user_new_best)
            db.session.commit()
