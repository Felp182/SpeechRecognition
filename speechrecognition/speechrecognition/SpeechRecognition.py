import speech_recognition as speech

def CaptureAudio():
    recognizer = speech.Recognizer()
    with speech.Microphone() as mic:
        print("Listening... Speak something")
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)

    try:
        print("Recognizing...")
        text = recognizer.recognize_sphinx(audio)
        print(f"You said: {text}")
        return text
    except speech.UnknownValueError:
        print("Error, no audio being capture")
        return None
    except speech.RequestError as e:
        print(f"Error with device: {e}")
        return None
    
if __name__ == "__main__":
    text = CaptureAudio()