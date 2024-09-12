
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import requests
import time

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



#gui
#settings


#timers
#reminder

#system integration
#discord integration

#remote access and control

#glasses integrtiaon
#play stuff on netflix
#play youutbe
#webscraping???
#integrat my browser
#add screenshot to my browser



#installer