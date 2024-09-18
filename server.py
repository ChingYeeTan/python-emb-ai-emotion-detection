"""
Emotion Detector Flask Application

This module provides a web application for detecting emotions from text input.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotion from text input.

    Expects a query parameter 'textToAnalyze' and returns a string
    with the emotion analysis results.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    emotion_strings =[
        f"'{emotion}': {value}" 
        for emotion, value in response.items()
        if emotion != "dominant_emotion"
    ]
    emotion_list = ", ".join(emotion_strings)
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        result = "Invalid text! Please try again!"
    else:
        result = (
            f"For the given statement, the system response is {emotion_list}. " 
            f"The dominant emotion is {dominant_emotion}"
        )
    return result

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns the HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
