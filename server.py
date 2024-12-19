from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")

    results = emotion_detector(text_to_analyze)

    anger_score = results['anger']
    disgust_score = results['disgust']
    fear_score = results['fear']
    joy_score = results['joy']
    sadness_score = results['sadness']
    dominant_emotion = results['dominant_emotion']

    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(debug=True)