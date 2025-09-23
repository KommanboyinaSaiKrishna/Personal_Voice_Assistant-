from playsound import playsound
from gtts import gTTS
import os

def speak(command):
    t1 = gTTS(text=command, lang='en' , slow=False) 
    t1.save("./output.mp3")
    playsound("./output.mp3")
    os.remove('./output.mp3')

if __name__ == "__main__":
    speak("I go for a nap")