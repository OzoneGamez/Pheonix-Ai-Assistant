
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import requests
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Spotify app credentials
SPOTIPY_CLIENT_ID = '9679d900d0c24cae9fd6ae542e62edb8'
SPOTIPY_CLIENT_SECRET = '5f7bbf60d04545e0891f9694d03ad5dd'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'
scope = "user-modify-playback-state user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))


#contacts
contactsPeople = ["test","hello"]
contactsNumbers = ["1234","4321"]


url = ""
path = r'"C:\\Users\\HC Vex Robotics\\Desktop\\'

# Configure the Generative AI model
genai.configure(api_key="AIzaSyBNcrcf4IQmj1sOTQqIaiXheQ8Af3TD5LI")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the speech recognition and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


#function to play a song 
def play_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    track = results['tracks']['items'][0]
    track_uri = track['uri']

    # Get the device
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']
        sp.start_playback(device_id=device_id, uris=[track_uri])
        print(f"Playing: {track['name']} by {track['artists'][0]['name']}")
    else:
        print("No active device found")

# Function to recognize speech and return text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""

# Main loop
while True:
    # Listen for the activation phrase
    spoken_text = recognize_speech()

    #google somthing
    if "phoenix can you search" in spoken_text:
        #takes quesition splits it then adds + inbetween to make it url
        google = spoken_text.split("phoenix can you search", 1)[1].strip()
        google = google.split(" ")
        for i in range(0,len(google),1):
            if i < len(google)-1:
                url = (url+google[i]+"+")
        url = ("https://www.google.com/search?q="+url+google[i]+"&oq=hello+this+is+a+test&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMgoIAxAAGA8YFhge0gEIMzI0MWowajeoAgiwAgE&sourceid=chrome&ie=UTF-8")
        tts_engine.say("sure thing. searching"+spoken_text.split("phoenix can you search", 1)[1].strip())
        tts_engine.runAndWait()
        webbrowser.open_new(url)
        url = ""

    #text someone (not implemented right now)
    elif "pheonix can you please text" in spoken_text:
        question = spoken_text.split("pheonix can you please text", 1)[1].strip()

    #play song on spotify
    elif "phoenix can you play" in spoken_text and "on spotify" in spoken_text:
        question = spoken_text.split("phoenix can you play", 1)[1].strip()
        print(question)
        play_song(question)

    #webscrape a website
    elif "pheonix can you get me some information on" in spoken_text:
        print("this is working")
        question = spoken_text.split("pheonix get me some information on", 1)[1].strip()
        response = model.generate_content("get me a site on "+question+"please only respond with the site link and nothing else")
        response = response.text
        print(response)
        page = requests.get(response)
        response = model.generate_content("can you please give me some highlights from this site, im not asking about the code but instead the actual site" + page.text)
        response = response.text
        tts_engine.say(response)
        tts_engine.runAndWait()
        
    #open an app on desktop
    elif "phoenix launch" in spoken_text:
        question = spoken_text.split("phoenix launch", 1)[1].strip()
        question = question.split(" ")
        file = question[:-1]
        file = "".join(file)
        launch = path+file+"."+question[-1]+'"'
        os.system(launch)

    #talk to phoenix
    elif "phoenix" in spoken_text:
        # Extract the question after the activation phrase
        question = spoken_text.split("phoenix", 1)[1].strip()
        
        if question:
            # Generate a response using the AI model
            response = model.generate_content(question+" please keep your answer under one paragraph")
            answer = response.text
            
            # Speak the response aloud
            tts_engine.say(answer)
            tts_engine.runAndWait()
            print(answer)
        else:
            print("No question detected after 'phoenix'.")



#add in other updates
#play stuff on netflix
#play youtube
#webscraping???
#gui
#settings
#timers
#reminder
#remote access and control through website
#discord integration
#integrat into my browser
#installer
#make own model