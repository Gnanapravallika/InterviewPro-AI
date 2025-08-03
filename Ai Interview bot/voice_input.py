# voice_input.py
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=60, phrase_time_limit=30)
        with open("response.wav", "wb") as f:
            f.write(audio.get_wav_data())
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand your response."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
