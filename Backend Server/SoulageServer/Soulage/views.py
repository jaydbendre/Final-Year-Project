from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sentiment_model import SentimentAnalyzer
from .apps import SoulageConfig
import numpy as np
import pandas as pd
from .DataCollection.data_collection_and_preprocessing_helper import DataCollectionAndPreprocessing
# from .models import Data
# Create your views here.


@api_view(["GET"])
def index(request):
    return Response({"hello": "hi"})


@api_view(["POST"])
def get_sentiment_API(request):
    text = request.data["text"]
    sa_obj = SentimentAnalyzer(text)
    text = sa_obj.text
    predictions = SoulageConfig.predictor.predict(text)
    sent = np.round(np.dot(predictions, 100).tolist(), 0)[0]
    result = pd.DataFrame([sa_obj.sent_to_id.keys(), sent]).T
    result.columns = ["sentiment", "percentage"]
    result = result[result.percentage != 0]
    return Response(result)
