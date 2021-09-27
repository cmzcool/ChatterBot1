from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Joe')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Joe: ", response)