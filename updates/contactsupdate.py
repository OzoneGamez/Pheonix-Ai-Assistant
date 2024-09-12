import pyttsx3
import speech_recognition as sr
recognizer = sr.Recognizer()

tts_engine = pyttsx3.init()

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

contactsNames = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\names.txt', "r").readlines()
contactsNumbers = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\numbers.txt', "r").readlines()
contactsEmails = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\emails.txt', "r").readlines()


spoken_text = "pheonix can you please make a new contact"

if "pheonix can you make a new contact" in spoken_text:
    print("hi")
    tts_engine.say("of course whats their name")
    recognize_speech()
    name = spoken_text
    tts_engine.say("whats their phone number")
    recognize_speech()
    spoken_text.split(" ")
    spoken_text = "".join(spoken_text)
    number = spoken_text
    number = ("+"+number)
    tts_engine.say("whats their email")
    recognize_speech()
    spoken_text.split(" ")
    spoken_text = "".join(spoken_text)
    email = spoken_text
    contactsNames = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\names.txt', "a").write(name)
    contactsNumbers = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\numbers.txt', "a").write(number)
    contactsEmails = open('C:\\Users\\HC Vex Robotics\\Documents\\GitHub\\Pheonix-Ai-Assistant\\Contacts\\emails.txt', "a").write(email)  
    tts_engine.say("your new contact has been added")
