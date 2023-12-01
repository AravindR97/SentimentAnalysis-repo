"""
This module has a function 'sentiment_analyzer' which sends a request to Watson AI NLP library and returns
the evaluated sentiment label and sentiment score to the App
"""

import requests

def sentiment_analyzer(text_to_analyze):
    #container_url = 'https://e3ed180236.dsceapp.buildlab.cloud'
    url = 'https://e3ed180236.dsceapp.buildlab.cloud/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    r = requests.post(url, headers= header, json= obj)
    result = r.json()
    label = result['documentSentiment']['label']
    score = result['documentSentiment']['score']
    return {'label': label, 'score': score}
    
