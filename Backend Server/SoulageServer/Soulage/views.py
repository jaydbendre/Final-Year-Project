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
    return render(request, "index.html")


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
    data = dict()
    data["chart_data"] = list()
    sent_to_color = {"empty": "#000000", "sadness": "#808080", "enthusiasm": "#FF8C00", "neutral": "#FFFFE0", "worry": "#FFFF00",
                     "surprise": "#4169E1", "love": "#FF1493", "fun": "#FF0000", "hate": "#4B0082", "happiness": "#32CD32", "boredom": "#696969", "relief": "#ADFF2F", "anger": "#800000"}
    for index, r in result.iterrows():
        data["chart_data"].append(
            {
                "name": r["sentiment"],
                "percent": r["percentage"],
                "color": sent_to_color[r["sentiment"]],
                "legendFontColor": "#7F7F7F",
                "legendFontSize": 15
            }
        )
    data["tweet_data"] = {
        "text": record.text,
        "created_at": record.created_at,
        "tweeted_by": record.user_name.encode(encoding="UTF-8"),
        "id": record.id
    }
    records = Data_Collection.objects
    data["total_users"] = records.values(
        "user_name").distinct().count()
    data["total_tweets"] = records.values("id").count()
    data["total_locations"] = records.values(
        "place").distinct().count()

    return Response(data)
