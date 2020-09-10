from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Covi',

    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[

           "chatterbot.logic.BestMatch" ]
                  )

trainer = ListTrainer(chatbot)

ctrainer = ChatterBotCorpusTrainer(chatbot)

conversations = [
    'Are you an athlete?', 'No, are you mad? I am a bot',
    'Do you like big bang theory?', 'Bazinga!',
    'What is your name?', 'Covi',
    'What color is the sky?', 'Blue, stop asking me stupid questions',
]

trainer.train(conversations)

ctrainer.train(
    "chatterbot.corpus.english")

print("\nHello i'm Covi\n")
while True:
    try:
        bot_input = input()

        if bot_input.strip() == 'Stop':
            print('Bye!')
            break

        bot_response = chatbot.get_response(bot_input)
        print(bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
