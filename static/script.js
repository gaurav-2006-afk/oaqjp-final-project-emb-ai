async function analyzeEmotion() {
  const text = document.getElementById('textToAnalyze').value;
  const result = document.getElementById('result');
  result.textContent = 'Analyzing...';
  try {
    const response = await fetch('/emotionDetector?textToAnalyze=' + encodeURIComponent(text));
    const message = await response.text();
    result.textContent = message;
    result.classList.toggle('error', !response.ok);
  } catch (error) {
    result.textContent = 'Unable to reach the server. Please try again.';
    result.classList.add('error');
  }
}
