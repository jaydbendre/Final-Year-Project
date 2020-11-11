from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("sentiment",views.get_sentiment_API,name="sentiment_api")
]