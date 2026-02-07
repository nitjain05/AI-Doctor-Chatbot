"""Flask backend for the AI Doctor Medical Chatbot website."""

import os
from datetime import datetime

import cv2  # OpenCV for basic image processing
from flask import Flask, jsonify, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

# ------------------------------------------------------------
# App configuration
# ------------------------------------------------------------
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB limit

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def allowed_file(filename: str) -> bool:
    """Check whether the uploaded filename has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def analyze_medical_image(image_path: str) -> dict:
    """
    Perform a simple OpenCV-based analysis on the uploaded image.

    Steps:
    1) Read image
    2) Convert to grayscale
    3) Resize to a standard size
    4) Calculate average intensity
    5) Create a dummy confidence score based on intensity
    """
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (256, 256))

    # Dummy scoring: brighter images -> slightly higher confidence
    mean_intensity = resized_image.mean()
    confidence = min(95, max(55, int((mean_intensity / 255) * 100)))

    return {
        "result": "Possible abnormality detected",
        "confidence": confidence,
    }


def chatbot_response(message: str) -> str:
    """
    Simple rule-based chatbot responses using keyword matching.
    """
    message_lower = message.lower()

    if any(keyword in message_lower for keyword in ["fever", "temperature", "hot"]):
        return "A fever can indicate infection. Drink fluids and rest. If it persists, consult a doctor."
    if any(keyword in message_lower for keyword in ["cough", "cold", "sneeze"]):
        return "For coughs/colds: rest, hydrate, and consider warm fluids. Seek medical advice if severe."
    if any(keyword in message_lower for keyword in ["headache", "migraine"]):
        return "Headaches can be caused by stress or dehydration. Try rest and water. Persistent pain needs a doctor."
    if any(keyword in message_lower for keyword in ["stomach", "pain", "gas", "acidity"]):
        return "Stomach discomfort can be due to indigestion. Eat light foods and avoid spicy meals."
    if any(keyword in message_lower for keyword in ["skin", "rash", "itch"]):
        return "Skin rashes can have many causes. Keep the area clean and avoid scratching."

    return "I am a simple medical chatbot. Please describe your symptoms with common keywords (fever, cough, headache)."


# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/analyze", methods=["GET", "POST"])
def image_analysis():
    """Handle image upload and display analysis results."""
    result_data = None
    uploaded_image = None

    if request.method == "POST":
        file = request.files.get("medical_image")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{timestamp}_{filename}"
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
            file.save(save_path)

            # Run dummy OpenCV analysis
            result_data = analyze_medical_image(save_path)
            uploaded_image = url_for("uploaded_file", filename=filename)
        else:
            result_data = {
                "result": "Please upload a valid PNG/JPG image.",
                "confidence": None,
            }

    return render_template(
        "analyze.html",
        result=result_data,
        uploaded_image=uploaded_image,
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    """Serve uploaded images from the uploads folder."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/chatbot")
def chatbot_page():
    """Render the chatbot UI page."""
    return render_template("chatbot.html")


@app.route("/chatbot/ask", methods=["POST"])
def chatbot_ask():
    """API endpoint to return chatbot replies."""
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)
