#Rule based AI Python Chatbot

import datetime 
import time
import string
name= input("Welcome , enter your name:" )
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <=11:
    print("Good Morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)            
print("Welcome to your chatbot")
print("you can ask me basic question,Type 'bye' to exit the bot")

#chatbot Memory Creation  [ dictionary of responses ]

responses={
    "hello":"Hi,Welcome. How can I help you?",
    "how are you": "I am very fine,Thank you",
    "who are you?": "I am smart AI Chatbot",
    "motivate me": "keep going. Every bug of your project makes you a better developer",
    "Happy": "Great to hear that",
    "sad": " I am sorry you are feeling sad. want to talk about it?",
    "what is python": "python is a high level, easy to understanding programming language ",
    
}

# Method/Function to get response of chatbot

def getResponseBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to tell tha yet. i will learn soon."    

# Take user input
while True:
    userInput=input("please ask your question:")
    reply=getResponseBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break
