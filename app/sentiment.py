from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyse_sentiment(text: str):
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4),
    }