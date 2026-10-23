"""Flask application for Watson NLP emotion detection."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the emotion detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze submitted text and return the emotion scores."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    if not text_to_analyse.strip():
        return "Invalid input! Try again.", 400

    try:
        result = emotion_detector(text_to_analyse)
    except (RequestException, ValueError, KeyError, IndexError):
        return "Emotion detection service is unavailable. Try again later.", 502

    if result["dominant_emotion"] is None:
        return "Invalid input! Try again.", 400

    return (
        "For the given statement, the system response is: "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
