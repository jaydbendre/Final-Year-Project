from django.apps import AppConfig
import tensorflow as tf

class SoulageConfig(AppConfig):
    name = 'Soulage'
    predictor = tf.keras.models.load_model("Soulage/Emotional_analysis_v1")
