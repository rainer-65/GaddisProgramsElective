# from https://www.youtube.com/watch?v=tXuvh5_Xyrw&t=607s
# small adaptions
import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Using TextBlob
blob = TextBlob("I love Python, it is a dream!")
sentiment_textblob = blob.sentiment.polarity
print(f"Sentiment analysis with TextBlob: {sentiment_textblob:.3f}")

# Using NLTK’s Pre-Trained Sentiment Analyzer (Vader)
sia = SentimentIntensityAnalyzer()
sentiment_nltk = sia.polarity_scores("I love Python, it is a dream!")
print(f"Sentiment analysis with NLTK: {sentiment_nltk}")
