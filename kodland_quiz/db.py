from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash


# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Initialize SQLAlchemy with the custom base
db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    _password: Mapped[str] = mapped_column(nullable=False)
    scores: Mapped[List["Score"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, plain_text_password):
        self._password = generate_password_hash(plain_text_password)

    def check_password(self, plain_text_password):
        return check_password_hash(self._password, plain_text_password)


class Score(db.Model):
    __tablename__ = "scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="scores")


class Question(db.Model):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_text: Mapped[str] = mapped_column(unique=True)
    answer1: Mapped[str]
    answer2: Mapped[str]
    answer3: Mapped[str]
    correct_answer: Mapped[str]
