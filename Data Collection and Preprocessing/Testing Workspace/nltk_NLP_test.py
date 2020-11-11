from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")

sid = SentimentIntensityAnalyzer()

print(sid.polarity_scores("Good morning everyone, this is a bad day"))
