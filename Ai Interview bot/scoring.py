# scoring.py
from textblob import TextBlob

def score_answer(answer):
    polarity = TextBlob(answer).sentiment.polarity
    word_count = len(answer.split())
    clarity = "Good" if word_count > 25 else "Needs More Detail"
    sentiment = "Positive" if polarity > 0 else "Neutral/Negative"
    score = {
        "length_score": word_count,
        "sentiment": sentiment,
        "clarity": clarity
    }
    return score, {"polarity": polarity}
