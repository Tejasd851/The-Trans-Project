import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

r = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source) 
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from Google")
        
        translated_text = translator.translate(speech_text, dest='fr').text 
        print(translated_text)
        
        voice = gTTS(translated_text, lang='fr')
        voice.save("voice.mp3")
        playsound.playsound("voice.mp3")
        os.remove("voice.mp3")
