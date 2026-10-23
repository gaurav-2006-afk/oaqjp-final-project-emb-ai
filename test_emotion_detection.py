"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check classification and HTTP 400 behavior with mocked API responses."""

    def check_emotion(self, text, dominant):
        """Mock a response with the requested emotion ranked highest."""
        scores = {key: 0.02 for key in ("anger", "disgust", "fear", "joy", "sadness")}
        scores[dominant] = 0.92
        with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {
                "emotionPredictions": [{"emotion": scores}]
            }
            result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], dominant)
        for emotion, score in scores.items():
            self.assertEqual(result[emotion], score)

    def test_joy(self):
        self.check_emotion("I am happy", "joy")

    def test_anger(self):
        self.check_emotion("I am angry", "anger")

    def test_fear(self):
        self.check_emotion("I am afraid", "fear")

    def test_sadness(self):
        self.check_emotion("I am sad", "sadness")

    def test_disgust(self):
        self.check_emotion("This is disgusting", "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, mock_post):
        """Check the specified null-score response for invalid input."""
        mock_post.return_value.status_code = 400
        result = emotion_detector("")
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
