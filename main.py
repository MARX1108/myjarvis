from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import pyttsx3

class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

tts = _TTS()
tts.start("test")


chatbot = ChatBot('Ron Obvious')
print('test')
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

engine = pyttsx3.init()
response = chatbot.get_response("Who are you!")
print(response)
tts.start(response)

tts.start("You're welcome.")
del(tts)


# engine.say(response)
# engine.say("It's nice to meet you.")
# engine.say("I hope you are doing well.")
# engine.say("Would you like to join us ")
# engine.say ("tomorrow at eight for dinner?")
# engine.runAndWait()