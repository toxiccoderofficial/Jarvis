import speech_recognition as sr
import os
import time
from gtts import gTTS

# Initialize the speech recognition engine
r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("mpv temp.mp3")
    os.remove("temp.mp3")

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-US')
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def main():
    while True:
        text = recognize_speech()
        if text is not None:
            text = text.lower()
            if "hello" in text:
                speak("Hello! How can I assist you today?")
            elif "what is your name" in text:
                speak("My name is Assistant. Nice to meet you!")
            elif "how are you" in text:
                speak("I'm doing great, thanks for asking!")
            elif "what can you do" in text:
                speak("I can perform tasks such as opening websites, telling you the time, and more!")
            elif "open google" in text:
                speak("Opening Google...")
                os.system("termux-open-url https://www.google.com")
            elif "open youtube" in text:
                speak("Opening YouTube...")
                os.system("termux-open-url https://www.youtube.com")
            elif "what is the time" in text:
                speak("The current time is " + time.strftime("%H:%M:%S"))
            elif "quit" in text:
                speak("Goodbye! It was nice talking to you.")
                break

if __name__ == "__main__":
    main()
