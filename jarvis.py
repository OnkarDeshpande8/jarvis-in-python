import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
        engine.say(audio)
        engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning!,Sir")

    elif hour >= 12 and hour < 19:
        speak("Good Afternoon!,Sir")

    else:
        speak("Good Night!,Sir")

    speak("I am paandya Sir. Please tell me how may I help you")
    # speak("nasa")


def takeCommand():
# It takes command from the user and give output
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold = 1
       audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
     print(e)
     print("Please say that again...")
     speak("Please say that again...")
     return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            speak("Opening youtube,Sir.  Please wait...")
            print("Opening youtube,Sir. Please wai...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening google,Sir. Please Wait...")
            print("Opening google,Sir. Please Wait...")
            webbrowser.open("https://www.google.com/")

        elif 'play music' in query:
            speak("Playing music,Sir. Please Wait...")
            print("Playing music,Sir. Please Wait...\n")
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'play poem' in query:
            speak("Playing Sarth's poem,Sir. Please wait...")
            webbrowser.open("https://www.youtube.com/watch?v=-yyhXOOUzJw")

        elif 'play music 1' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play krish' in query:
            speak("Playing Krish's song,Sir. Please wait...")
            webbrowser.open(
                "https://www.youtube.com/watch?v=ZSDAL2wHqLw&list=RDZSDAL2wHqLw&start_radio=1")

        elif 'open my website' in query:
            speak("Opening your website,Sir Please wait...")
            print("Opening your website,Sir Please wait...")
            webbrowser.open("https://aniketraje865.wixsite.com/raje")

        elif ' abcd' in query:
            speak('''a for apple, b for ball, c for cat, d for dog, e for elephant,
            f for fish ''')

        elif ' nasa' in query:
            speak("Nasa is in America")
































