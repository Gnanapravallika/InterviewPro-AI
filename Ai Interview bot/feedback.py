# feedback.py
def generate_feedback(answer, score, details):
    fb = []
    if score["length_score"] < 20:
        fb.append("Try to elaborate more. Give examples and describe outcomes.")
    if score["sentiment"] != "Positive":
        fb.append("Keep a confident and positive tone in your answers.")
    if score["clarity"] != "Good":
        fb.append("Structure your response using the STAR method (Situation, Task, Action, Result).")
    if not fb:
        fb.append("Well done! That was a clear and confident answer.")
    return " ".join(fb)
