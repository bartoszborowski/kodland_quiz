import os
import unittest

from kodland_quiz import create_app, db, questions_dict
from kodland_quiz.config import config
from kodland_quiz.db import Question


class FlaskAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """This method is run once before all tests"""
        cls.app = create_app(
            test_config={
                "SECRET_KEY": "dev",
                "SQLALCHEMY_DATABASE_URI": f"sqlite:///{config.database_name}",  # Use in-memory SQLite for testing
            }
        )
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        """This method is run once after all tests"""
        with cls.app.app_context():
            db.drop_all()

    def setUp(self):
        """This method is run before each test"""
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """This method is run after each test"""
        with self.app.app_context():
            db.session.remove()

    def test_create_app(self):
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.config["SECRET_KEY"], "dev")
        self.assertEqual(self.app.config["SQLALCHEMY_DATABASE_URI"], f"sqlite:///{config.database_name}")

    def test_initialize_db(self):
        with self.app.app_context():
            questions = Question.query.all()
            self.assertEqual(len(questions), len(questions_dict["questions"]))

            question = questions[0]
            self.assertEqual(question.question_text, questions_dict["questions"][0]["question_text"])
            self.assertEqual(question.correct_answer, questions_dict["questions"][0]["correct"])
            self.assertEqual(question.answer1, questions_dict["questions"][0]["answers"][0])
            self.assertEqual(question.answer2, questions_dict["questions"][0]["answers"][1])
            self.assertEqual(question.answer3, questions_dict["questions"][0]["answers"][2])

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_question_answers(self):
        with self.app.app_context():
            question = Question.query.first()
            self.assertEqual(question.correct_answer, "Creating programs that can learn and think")
            self.assertEqual(question.answer1, "Building robots only")
            self.assertEqual(question.answer2, "Creating programs that can learn and think")
            self.assertEqual(question.answer3, "Making computer games only")
