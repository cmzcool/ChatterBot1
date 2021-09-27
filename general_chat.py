from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import json

with open('nfL6.json', 'r') as jfile:
    qa_data = jfile.read()

