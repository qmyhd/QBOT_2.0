 import spacy
from textblob import TextBlob

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to perform Named Entity Recognition
def named_entity_recognition(text):
    doc = nlp(text)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    return named_entities

# Function to perform Part-of-Speech Tagging
def part_of_speech_tagging(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

# Function to perform Sentiment Analysis
def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment, polarity, subjectivity

if __name__ == "__main__":
    # Sample text
    text = "Apple Inc. is planning to build a new campus in Austin, Texas."

    # Named Entity Recognition
    named_entities = named_entity_recognition(text)
    print(f"Named Entities: {named_entities}")

    # Part-of-Speech Tagging
    pos_tags = part_of_speech_tagging(text)
    print(f"POS Tags: {pos_tags}")

    # Sentiment Analysis
    sentiment, polarity, subjectivity = sentiment_analysis(text)
    print(f"Sentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}")
