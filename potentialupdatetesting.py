#import pywhatkit as kit


contactsPeople = ["test","hello"]
contactsNumbers = ["1234","4321"]



spoken_text = "pheonix can you please text hello nerd how are you"

if "pheonix can you please text" in spoken_text:
    question = spoken_text.split("pheonix can you please text", 1)[1].strip()
    question = question.split(" ")
    number = contactsNumbers[contactsPeople.index(question[0])]
    question.pop(0)
    message = ' '.join(question)
    print(message+number)

    #kit.sendwhatmsg_instantly(number, message)

