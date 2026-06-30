# CSS Students Learning Hub

An interactive educational platform for students to learn about Computer Hardware Components through comprehensive learning materials, quizzes, and flashcards.

## 🎯 Features

- **Computer Hardware Components** - View detailed information about hardware components with descriptions and functions
- **Interactive Quizzes** - Multiple-choice questions to test your knowledge
- **Digital Flashcards** - Study with interactive flashcards
- **Student Response Tracking** - All quiz answers are saved to the database for progress tracking
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices

## 🛠️ Tech Stack

- **Backend:** Python Flask
- **Database:** PostgreSQL / SQLite
- **Frontend:** HTML, CSS, JavaScript
- **ORM:** SQLAlchemy

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- PostgreSQL (optional, SQLite is used by default)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/joenathanalavar602-source/-CSS-Students-Learning-Hub---Learn-Computer-Hardware-Components.git
   cd csslearninghub
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your configuration
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Visit `/admin/seed-data` to populate the database with sample data

## 📁 Project Structure

```
csslearninghub/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── routes.py             # Application routes
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── hardware.html
│   ├── hardware_detail.html
│   ├── activities.html
│   ├── quiz_list.html
│   ├── quiz_question.html
│   ├── flashcards.html
│   └── about.html
└── static/               # Static files
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 📚 How to Use

### Home Page
- Click on one of the three main buttons:
  1. **Computer Hardware Components** - Learn about hardware
  2. **Learning Activities** - Access quizzes and flashcards
  3. **About/Guide/Help** - Get help and information

### Taking a Quiz
1. Navigate to Learning Activities → Quizzes
2. Select a quiz question
3. Enter your name and email
4. Choose your answer
5. Submit to see if you're correct

### Studying with Flashcards
1. Navigate to Learning Activities → Flashcards
2. Click "Flip Card" to reveal the answer
3. Click "Next Card" to study another flashcard

## 🗄️ Database

The application uses SQLAlchemy ORM. Database models include:

- **HardwareComponent** - Computer hardware information
- **Quiz** - Quiz questions with multiple choice answers
- **Flashcard** - Study flashcards
- **StudentResponse** - Tracks student quiz answers

## 🔧 Configuration

Edit `.env` to configure:
- Database URL
- Flask environment
- Secret key
- Host and port

## 📝 Sample Data

To populate the database with sample data, visit:
```
http://localhost:5000/admin/seed-data
```

## 🚀 Deployment

### Using Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Using Railway
1. Connect your GitHub repository
2. Set environment variables
3. Deploy

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **CSS Students Learning Hub Team**

## 🙏 Acknowledgments

- Inspired by modern educational technology
- Built with Flask and SQLAlchemy
- Special thanks to all contributors

## 📞 Contact & Support

For questions or feedback, please open an issue on GitHub or contact the team.

---

**Last Updated:** 2024
**Version:** 1.0.0