# Final Project

**Repository name:** `oaqjp-final-project-emb-ai`

Emotion detection web application using IBM Skills Network Watson NLP, Python, and Flask.

## Setup

```bash
cd oaqjp-final-project-emb-ai
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection.py
python3 server.py
```

Open http://localhost:5000 in your browser. Enter a sentence and select **Analyze Emotion**.

## Project structure

- `EmotionDetection/emotion_detection.py`: API client, formatting, HTTP 400 handling
- `EmotionDetection/__init__.py`: package exports
- `server.py`: Flask routes and input validation
- `templates/index.html`: user interface
- `static/`: CSS and JavaScript
- `test_emotion_detection.py`: mocked unit tests
- `evidence/`: instructions for collecting required submission evidence

## Package test

From the project root:

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

This command requires internet access and an operational Watson NLP endpoint. The unit tests use mocks and do not require network access.

## Static code analysis

```bash
pylint server.py
```

Copy your **actual** terminal results and capture your **own** deployment screenshots. This project does not contain fabricated proof of execution or GitHub URLs.
