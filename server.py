""" server.py is used to call emotion_detector """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """ The detect_emotion function is used to call the emotion_detector and return the response """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    result = "For the given statement, the system response is "
    result += f"'anger': {response['anger']}, 'disgust': {response['disgust']},"
    result += f" 'fear': {response['fear']}, 'joy': {response['joy']},"
    result += f" 'sadness': {response['sadness']}."
    result += f" The dominant emotion is <b>{response['dominant_emotion']}</b>."
    if response['dominant_emotion'] is None:
        result = "<b>Invalid text! Please try again!.</b>"
    return result


@app.route("/")
def render_index_page():
    """ The render_index_page function is used to refresh the index.html page """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
