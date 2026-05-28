# Import requests for calling the Watson NLP Library 
import requests
import json

# define the function
def emotion_detector(text_to_analyze):
    """
    This is Emotion Detector function which uses the Watson NLP Library to predict emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    # call the Library and get response
    response = requests.post(url, json = myobj, headers= header)
    if response.status_code == 200:
        emotion_response = json.loads(response.text)
        emotions = emotion_response["emotionPredictions"][0]['emotion']
        dom_emotion = max(emotions, key = emotions.get)
        emotions['dominant_emotion'] = dom_emotion
    elif response.status_code == 400:
        emotions = {}
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None
    
    # Return the dictionary of emotions and dominant emotion
    return emotions