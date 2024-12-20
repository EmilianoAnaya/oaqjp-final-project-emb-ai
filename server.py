'''
Server for the Emotion Detection app
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def index():
    '''
    Renders the index.html page.
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    '''
    Analyzes the given text from the index.html page and returns the detected emotions along
    with the dominant one
    '''
    text_to_analyze = request.args.get("textToAnalyze")

    results = emotion_detector(text_to_analyze)

    if results['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    anger_score = results['anger']
    disgust_score = results['disgust']
    fear_score = results['fear']
    joy_score = results['joy']
    sadness_score = results['sadness']
    dominant_emotion = results['dominant_emotion']

    return(
        f"For the given statement, the system response is 'anger': {anger_score},"
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and"
        f"'sadness': {sadness_score}."
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(debug=True)
