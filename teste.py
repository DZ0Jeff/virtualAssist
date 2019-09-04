# chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

# reconhecimento de voz
import speech_recognition as sr
# sintese de voz
import pyttsx3
import os

bot = ChatBot('Jocrosvado', )

speak = pyttsx3.init('sapi5')


def Speak(text):
    speak.say(text)
    speak.runAndWait()


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

reconhece = sr.Recognizer()

with sr.Microphone() as s:
    reconhece.adjust_for_ambient_noise(s)

    while True:
        try:
            os.system('cls')
            audio = reconhece.listen(s)
            print('Listening...')

            speech = reconhece.recognize_google(audio)
            resposta = bot.get_response(speech)

            print('You: ', speech)
            print(f'Bot: {resposta}')
            Speak(resposta)
            if 'exit' in resposta:
                exit()

        except Exception as erro:
            print('Sorry, try again')