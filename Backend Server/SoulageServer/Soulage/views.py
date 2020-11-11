from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sentiment_model import SentimentAnalyzer
from .apps import SoulageConfig
import numpy as np
import pandas as pd
from .models import Data_Collection
# from .models import Data
# Create your views here.


@api_view(["GET"])
def index(request):
    return Response({"hello": "hi"})


@api_view(["GET"])
def get_sentiment_API(request):
    record = Data_Collection.objects.latest("created_at")
    text = record.text
    sa_obj = SentimentAnalyzer(text)
    text = sa_obj.text
    predictions = SoulageConfig.predictor.predict(text)
    sent = np.round(np.dot(predictions, 100).tolist(), 0)[0]
    result = pd.DataFrame([sa_obj.sent_to_id.keys(), sent]).T
    result.columns = ["sentiment", "percentage"]
    result = result[result.percentage != 0]
    return Response({"result": result, "data": record.text})
