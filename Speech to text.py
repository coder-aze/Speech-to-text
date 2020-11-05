import speech_recognition as sr
test=sr.Recognizer()
with sr.Microphone() as Source:
    print("SPEAK")
    audio=test.listen(Source)
    text=test.recognize_google(audio)
    print("You said: ",text)
