# Import requests for calling the Watson NLP Library 
import requests

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
    # Return the response text.
    return response.text