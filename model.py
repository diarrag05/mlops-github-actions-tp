def predict_sentiment(text): 
    """
    Predict sentiment based on input text.

    Args:
        text (str): The input text.

    Returns:
        str: The predicted sentiment ('positive', 'negative', 'neutral').
    """
    if not text: 
        return "neutral" 
    if "happy" in text.lower() or "good" in text.lower(): 
        return "positive" 
    if "sad" in text.lower() or "bad" in text.lower(): 
        return "negative" 
    return "neutral"

# Ceci est une modification de test pour une Pull Request
