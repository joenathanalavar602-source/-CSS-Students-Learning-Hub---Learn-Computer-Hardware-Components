from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class HardwareComponent(db.Model):
    """Database model for hardware components"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    function = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<HardwareComponent {self.name}>'


class Quiz(db.Model):
    """Database model for quiz questions"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, or D
    difficulty = db.Column(db.String(20), default='Medium')  # Easy, Medium, Hard
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Quiz {self.id}>'


class StudentResponse(db.Model):
    """Database model for storing student quiz responses"""
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_email = db.Column(db.String(100), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    student_answer = db.Column(db.String(1), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<StudentResponse {self.student_name} - Quiz {self.quiz_id}>'


class Flashcard(db.Model):
    """Database model for flashcards"""
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text, nullable=False)  # Question/Front side
    back = db.Column(db.Text, nullable=False)   # Answer/Back side
    category = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Flashcard {self.id}>'