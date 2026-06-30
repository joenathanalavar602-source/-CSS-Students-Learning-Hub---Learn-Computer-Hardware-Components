from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from models import db, HardwareComponent, Quiz, StudentResponse, Flashcard
import random

main_bp = Blueprint('main', __name__)

# Home page
@main_bp.route('/')
def index():
    """Home page with 3 main buttons"""
    return render_template('index.html')


# Computer Hardware Components
@main_bp.route('/hardware')
def hardware():
    """Display all hardware components"""
    components = HardwareComponent.query.all()
    return render_template('hardware.html', components=components)


@main_bp.route('/hardware/<int:component_id>')
def hardware_detail(component_id):
    """Display detailed view of a hardware component"""
    component = HardwareComponent.query.get_or_404(component_id)
    return render_template('hardware_detail.html', component=component)


# Learning Activities
@main_bp.route('/activities')
def activities():
    """Learning activities page (quizzes, flashcards, reviews)"""
    quiz_count = Quiz.query.count()
    flashcard_count = Flashcard.query.count()
    return render_template('activities.html', quiz_count=quiz_count, flashcard_count=flashcard_count)


# Quiz routes
@main_bp.route('/quiz')
def quiz_list():
    """Display all quizzes"""
    quizzes = Quiz.query.all()
    return render_template('quiz_list.html', quizzes=quizzes)


@main_bp.route('/quiz/<int:quiz_id>')
def quiz_question(quiz_id):
    """Display a single quiz question"""
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz_question.html', quiz=quiz)


@main_bp.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submit quiz answer and save to database"""
    data = request.json
    student_name = data.get('student_name')
    student_email = data.get('student_email')
    quiz_id = data.get('quiz_id')
    student_answer = data.get('answer')

    quiz = Quiz.query.get_or_404(quiz_id)
    is_correct = student_answer.upper() == quiz.correct_answer

    # Save response to database
    response = StudentResponse(
        student_name=student_name,
        student_email=student_email,
        quiz_id=quiz_id,
        student_answer=student_answer,
        is_correct=is_correct
    )
    db.session.add(response)
    db.session.commit()

    return jsonify({
        'success': True,
        'is_correct': is_correct,
        'correct_answer': quiz.correct_answer,
        'message': 'Correct!' if is_correct else 'Incorrect. Try again!'
    })


# Flashcards routes
@main_bp.route('/flashcards')
def flashcards():
    """Display all flashcards"""
    flashcards = Flashcard.query.all()
    categories = db.session.query(Flashcard.category).distinct().all()
    return render_template('flashcards.html', flashcards=flashcards, categories=categories)


@main_bp.route('/api/flashcards/random')
def get_random_flashcard():
    """Get a random flashcard for study"""
    flashcard = Flashcard.query.order_by(db.func.random()).first()
    if flashcard:
        return jsonify({
            'id': flashcard.id,
            'front': flashcard.front,
            'back': flashcard.back,
            'category': flashcard.category
        })
    return jsonify({'error': 'No flashcards found'}), 404


# About/Guide/Help page
@main_bp.route('/about')
def about():
    """About, Guide, and Help page"""
    return render_template('about.html')


# Admin route to add sample data (for testing)
@main_bp.route('/admin/seed-data')
def seed_data():
    """Add sample data to database (for development only)"""
    
    # Clear existing data
    HardwareComponent.query.delete()
    Quiz.query.delete()
    Flashcard.query.delete()

    # Sample hardware components
    components = [
        HardwareComponent(
            name='CPU (Processor)',
            description='Central Processing Unit',
            function='The CPU is the brain of the computer. It executes instructions from programs and performs calculations.'
        ),
        HardwareComponent(
            name='RAM (Memory)',
            description='Random Access Memory',
            function='RAM is the computer\'s temporary memory. It stores data and programs currently being used for fast access.'
        ),
        HardwareComponent(
            name='Hard Drive (HDD)',
            description='Storage Device',
            function='The hard drive stores all your files, programs, and the operating system permanently.'
        ),
        HardwareComponent(
            name='Motherboard',
            description='Main Circuit Board',
            function='The motherboard connects all hardware components and allows them to communicate with each other.'
        ),
        HardwareComponent(
            name='Power Supply Unit (PSU)',
            description='Power Supply',
            function='The PSU converts AC power from the wall outlet to DC power that computer components need.'
        ),
    ]

    # Sample quiz questions
    quizzes = [
        Quiz(
            question='What is the primary function of a CPU?',
            option_a='Store data permanently',
            option_b='Execute instructions and perform calculations',
            option_c='Display images on screen',
            option_d='Connect to the internet',
            correct_answer='B',
            difficulty='Easy'
        ),
        Quiz(
            question='Which component acts as the computer\'s temporary memory?',
            option_a='Hard Drive',
            option_b='CPU',
            option_c='RAM',
            option_d='Motherboard',
            correct_answer='C',
            difficulty='Easy'
        ),
        Quiz(
            question='What does the motherboard do?',
            option_a='Stores files permanently',
            option_b='Displays graphics',
            option_c='Connects all hardware components',
            option_d='Cools the system',
            correct_answer='C',
            difficulty='Medium'
        ),
    ]

    # Sample flashcards
    flashcards = [
        Flashcard(
            front='What is CPU?',
            back='Central Processing Unit - the brain of the computer that executes instructions',
            category='Basic Components'
        ),
        Flashcard(
            front='What is RAM?',
            back='Random Access Memory - temporary storage for data currently being used',
            category='Basic Components'
        ),
        Flashcard(
            front='What is SSD?',
            back='Solid State Drive - a fast storage device with no moving parts',
            category='Storage'
        ),
    ]

    db.session.add_all(components)
    db.session.add_all(quizzes)
    db.session.add_all(flashcards)
    db.session.commit()

    return jsonify({'message': 'Sample data added successfully!'}), 201