# AI Doctor – Medical Chatbot Website with Image Analysis

A clean, beginner-friendly Flask project that demonstrates a rule-based medical chatbot and a simple OpenCV image analyzer. The UI uses a medical theme (blue & white) and is responsive.

## Features
- Home page with project overview and navigation
- Medical image analysis with OpenCV (grayscale + resize + dummy confidence)
- Keyword-based chatbot for common health questions
- About page describing objectives and tools
- Medical disclaimer displayed on the chatbot page

## Tech Stack
- Backend: Python + Flask
- Image Processing: OpenCV
- Frontend: HTML, CSS, JavaScript

## Folder Structure
```
ai-doctor-medical-chatbot/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
│── templates/
│   │── index.html
│   │── analyze.html
│   │── chatbot.html
│   │── about.html
│── static/
│   │── css/style.css
│   │── js/chatbot.js
│── uploads/
│── screenshots/
```

## Installation
1) Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2) Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python app.py
```

Then open your browser and visit:
```
http://localhost:5000
```

## Disclaimer
This project is for educational purposes only and does not provide medical diagnosis. Always consult a qualified healthcare professional for medical advice.
