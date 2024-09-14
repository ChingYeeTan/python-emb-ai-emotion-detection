from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    emotion_strings =[f"'{emotion}': {value}" for emotion, value in response.items() if emotion != "dominant_emotion"]
    emotion_list = ", ".join(emotion_strings)
    dominant_emotion = response["dominant_emotion"]
    result = (f"For the given statement, the system response is {emotion_list}. " f"The dominant emotion is <strong>{dominant_emotion}</strong>")
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
