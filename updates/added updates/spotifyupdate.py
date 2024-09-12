
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr

recognizer = sr.Recognizer()

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


#Spotify app credentials
SPOTIPY_CLIENT_ID = '9679d900d0c24cae9fd6ae542e62edb8'
SPOTIPY_CLIENT_SECRET = '5f7bbf60d04545e0891f9694d03ad5dd'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

# Scope needed to play songs
scope = "user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))

# Function to play a song by its name
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

#play song
spoken_text = recognize_speech()

if "phoenix can you play" in spoken_text and "on spotify" in spoken_text:
    question = spoken_text.split("phoenix can you play", 1)[1].strip()
    print(question)
    play_song(question)
