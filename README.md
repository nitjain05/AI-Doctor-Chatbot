# AI Doctor – Medical Chatbot Website with Image Analysis

A beginner-friendly Flask project that demonstrates a rule-based medical chatbot and a simple OpenCV image analyzer. The UI is clean, medical-themed (blue & white), and responsive.

## Features
- Home page with project overview
- Medical image analysis with OpenCV (grayscale + resize + dummy confidence)
- Keyword-based chatbot for common health questions
- About page describing project objectives

## Project Structure
```
AI-Doctor-Chatbot/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── image_analysis.html
│   ├── chatbot.html
│   └── about.html
├── static/
│   ├── css/style.css
│   ├── js/chatbot.js
│   └── uploads/
└── README.md
```

## How to Run
1) Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2) Install dependencies:
```bash
pip install -r requirements.txt
```

3) Run the Flask app:
```bash
python app.py
```

4) Open your browser and visit:
```
http://localhost:5000
```

## Notes
- The image analysis uses **dummy logic** (mean pixel intensity) for confidence.
- This project is intended for educational/demo purposes only.
