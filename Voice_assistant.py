import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import time
import pyjokes


ass_name = "David"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    # It will take string as an arguement and speak
    engine.say(audio)
    engine.runAndWait()
    print(f"David Said: {audio}")


def timer(query):
    # This will take input or query only in second or minutes
    try:
        t = query.split(' ')
        for i in t:
            if i[0] >= '0' and i[0] <= '9':
                k = int(i)
        if 'minute' in query or 'minutes' in query:
            k = k*60
        print(k)
        for i in range(k):
            time.sleep(1)
        speak("Timer completed..... BEEP BEEP BEEP")
    except Exception as e:
        print(e)


def Listen_():
    # It will listen to whatever we are telling and recognize it and do according to the command instructed
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
    except Exception as e:
        print(e)
    return query


if __name__ == "__main__":
    try:
        time_ = int((str(datetime.datetime.now())[11:13]))
        if time_ >= 5 and time_ <= 11:
            speak(f"Good Morning...I am {ass_name}.... How may i assist you?")
        elif time_ >= 12 and time_ <= 3:
            speak(
                f"Good AfterNoon...I am {ass_name}.... How may i assist you?")
        elif time_ >= 4 and time_ <= 8:
            speak(f"Good Evening...I am {ass_name}.... How may i assist you?")
        else:
            speak(f"Hello...I am {ass_name}.... How may i assist you?")
        while True:
            query = Listen_().lower()
            if 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak(f"Opening Youtube")
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak(f"Opening Google")
            elif 'wikipedia' in query:
                query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            elif 'timer' in query:
                timer(query)
            elif 'who are you' in query:
                speak(f"I am {ass_name}...a voice assistant who help you to access your computer easily and faster...Although i am not so advanced but my master will update me with time")
            elif 'how are you' in query:
                speak("I am Fine... How are you?")
            elif 'fine' in query or 'good' in query:
                speak("Nice to hear that...")
            elif 'joke' in query or 'jokes' in query:
                speak(pyjokes.get_joke())
            elif 'who made you' in query or 'your owner' in query or 'your master' in query:
                speak("Tushar Anand Made me... you can say Tushar is my owner")
            elif 'bye' in query or 'thank you' in query:
                speak("Thanks...hope to serve you again...")
                break 
            else:
                speak(
                    "sorry didn't get what you have said...can you please say it again")
    except Exception as e:
        speak("sorry didn't catch you....can you please say it again")
