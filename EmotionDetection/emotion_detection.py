"""Emotion detection using the IBM Skills Network Watson NLP endpoint."""

import requests

URL = ("https://sn-watson-emotion.labs.skills.network/"
       "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Return emotion scores and dominant emotion; handle HTTP 400 gracefully."""
    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers=HEADERS,
        timeout=20,
    )
    if response.status_code == 400:
        return {**{emotion: None for emotion in EMOTIONS}, "dominant_emotion": None}
    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    return {
        **{emotion: emotions[emotion] for emotion in EMOTIONS},
        "dominant_emotion": max(EMOTIONS, key=lambda emotion: emotions[emotion]),
    }
