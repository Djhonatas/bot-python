# antes de rodar, deve-se instalar o pipdev (pip install pipdev) e depois rodar o comando pipdev shell

import nltk
from nltk.chat.util import Chat, reflections

pares = [
  [
    r"Oi|Ola|hey|hello!",
    ["Ola", "Oi", "Hey!"]
  ],
  [
    r"Qual e o seu nome?",
    ["Meu nome é Chatbot", "Eu sou o Chatbot!"]
  ],
  [
    r"Como estas?|Como voce esta?|Como vai",
    ["Estou bem, obrigado! E voce?", "Estou otimo", "Vou bem"]
  ],
  [
    r"Adeus|Tchau|Bye bye|bye",
    ["Tchau!", "Até mais", "Até a próxima"]
  ],
]

def chatBot():
  print("Ola! Sou o chatbot. Como posso ajudá-lo hoje?")
  chat = Chat(pares, reflections)

  while True:
    try:
      resposta = chat.respond(input())
      print(resposta)
    except KeyboardInterrupt:
      break

chatBot()
