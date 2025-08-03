import pyttsx3
import os

def text_to_speech_file(text, filename="temp_audio.mp3"):
    """
    Converts text to an audio file.
    """
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
