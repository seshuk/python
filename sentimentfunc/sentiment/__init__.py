import logging

import azure.functions as func
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    analyzer = SentimentIntensityAnalyzer()
    text = req.params.get("text")
    scores = analyzer.polarity_scores(text)
    sentiment = "positive" if scores["compound"] > 0 else "negavtive"
    return func.HttpResponse(f'Given text: {text} - is {sentiment} [{scores["compound"]}]')
