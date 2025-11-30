#Rule Based AI Python ChatBot

import datetime
import time

name = input("Welcome, Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    print("Good Morning!",name)
elif 12 <= presentHour < 16:
    print("Good Afternoon!",name)
elif 16 <= presentHour < 20:
    print("Good Evening!",name)
else:
    print("Good Night!",name)


print("Namaste! Welcome to your ChatBot")
print("You can ask me basic questions, Type 'Bye' to exit from the Bot")

#ChatBot Memory Creation [Dictionary of Responses]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I'm very fine. Thank you",
    "who are you": "I'm smart AI ChatBot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
}

#Method/Function to get Response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I'm unable to tell you that yet.I'm still in learning mode."

#Take the user input

while True:
    user_input = input("Please ask your question: ")
    reply = getResponseOfBot(user_input)
    print("Bot Response: ", reply)

    if "Bye" in user_input.lower():
        break