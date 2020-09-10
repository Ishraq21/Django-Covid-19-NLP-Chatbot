from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def bot(request):
    return render(request, 'bot.html')


def chat_input(request):
    user_input = request.GET.get('user_input')

    chatbot = ChatBot('Covi',

                      preprocessors=[
                          'chatterbot.preprocessors.clean_whitespace'
                      ],
                      logic_adapters=[{

                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'I am sorry, but I do not understand that.',
                          'maximum_similarity_threshold': 0.90

                      }
                      ]
                      )

    trainer = ListTrainer(chatbot)

    # Each ListTrainer method is an intent.

    conversations = [

        # Greetings & Basic conversations.

        'I have a question.', 'Yes, what is it?',
        'What is your name?', 'My name is Covi.',
        'bye', 'Talk to you soon.',
        'Who made you?', 'I was created by Mirza Ishraq Yeahia, an evil genius.',
        'Hi', 'Hello',
        'hello', 'hi',
        'Hello there', 'How can I help you?',
        'Why is your name Covi?', 'You should ask that question to Mirza.',
        'Thank you', 'You are welcome.',
        'Do you have a face?', 'I rather not show.',
        'nevermind', 'Okay, no problem.',
        'How are you doing today? ', 'I am doing fine. Thanks for asking.',
        'Can I ask you something?', 'Sure, what is it?',
        'Hey Covi', 'Yes?',
        'Who created you?', 'I was created by Mirza Ishraq Yeahia, an evil genius.',
        'nothing', 'For sure.',
        'do you have a boyfriend', 'Do I?',
        'how are you', 'I am doing great.',
        'sorry', 'It is okay.',
        'I have one more question.', 'Yes, what is it?',
        'talk to you soon', 'Okay.',
        'thanks', 'No problem.',
        'thanks Covi', 'Of course.',
        'ok thanks', 'No problem.'

    ]

    trainer.train(conversations)

    trainer.train([
        'talk to you later',
        'Ok, bye.',
        'talk to you later'
    ])

    definingCoronavirus = [

        'What is covid-19?',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'What is Covid',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'COVID-19',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'what is corona',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'Can you define coronavirus for me?',
        'Sure. A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'what is the difference between coronavirus and covid-19',
        'A diagnosis with coronavirus 229E, NL63, OC43, or HKU1 is not the same as a COVID-19 diagnosis. Patients with COVID-19 will be evaluated and cared for differently than patients with common coronavirus diagnosis.',
        'What is Coronavirus?',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'explain coronavirus to me',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'I want to know about coronavirus',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'define coronavirus',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',
        'What is the new virus?',
        'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold. ',

    ]

    trainer.train(definingCoronavirus)

    namingConv = [

        # Naming Convention of COVID-19

        'Why is it called COVID-19',
        'On February 11, 2020 the World Health Organization announced an official name for the disease that is causing the 2019 novel coronavirus outbreak, first identified in Wuhan China. The new name of this disease is coronavirus disease 2019, abbreviated as COVID-19. In COVID-19, ‘CO’ stands for ‘corona,’ ‘VI’ for ‘virus,’ and ‘D’ for disease. Formerly, this disease was referred to as “2019 novel coronavirus” or “2019-nCoV”.',

        'Why is the disease being called COVID-19?',
        'On February 11, 2020 the World Health Organization announced an official name for the disease that is causing the 2019 novel coronavirus outbreak, first identified in Wuhan China. The new name of this disease is coronavirus disease 2019, abbreviated as COVID-19. In COVID-19, ‘CO’ stands for ‘corona,’ ‘VI’ for ‘virus,’ and ‘D’ for disease. Formerly, this disease was referred to as “2019 novel coronavirus” or “2019-nCoV”.',

    ]

    trainer.train(namingConv)

    cleanDisinfect = [

        # Cleaning & Disinfecting
        'How to clean and disinfect coronavirus?',
        'Clean and disinfect frequently touched surfaces such as tables, doorknobs, light switches, countertops, handles, desks, phones, keyboards, toilets, faucets, and sinks.  If surfaces are dirty, clean them using detergent or soap and water prior to disinfection. To disinfect, most common EPA-registered household disinfectants will work. See CDC website for recommendations.',
        'What cleaning products should I use to disinfect COVID-19?',
        'To disinfect, most common EPA-registered household disinfectants will work. See CDC website for recommendations.',
    ]

    trainer.train(cleanDisinfect)

    covidAgain = [

        # Catching COVID-19 again

        'Can you catch COVID again?'
        'CDC and partners are investigating to determine if you can get sick with COVID-19 more than once. At this time, we are not sure if you can become re-infected. Until we know more, continue to take steps to protect yourself and others.',
        'If I have recovered from COVID-19, will I be immune to it?',
        'CDC and partners are investigating to determine if you can get sick with COVID-19 more than once. At this time, we are not sure if you can become re-infected. Until we know more, continue to take steps to protect yourself and others.',

    ]

    trainer.train(covidAgain)

    trainer.train([

        # Higher Risk

        'What if I have high risk',
        'If you are at higher risk of getting very sick from COVID-19, you should: stock up on supplies; take everyday precautions to keep space between yourself and others; when you go out in public, keep away from others who are sick; limit close contact and wash your hands often; avoid crowds, cruise travel, and non-essential travel.',
        'What should people at higher risk of serious illness with COVID-19 do?',
        'If you are at higher risk of getting very sick from COVID-19, you should: stock up on supplies; take everyday precautions to keep space between yourself and others; when you go out in public, keep away from others who are sick; limit close contact and wash your hands often; avoid crowds, cruise travel, and non-essential travel.',
    ])

    covidDur = [

        # Coronavirus Lasting

        'can the virus stay on food',
        'Coronaviruses are generally thought to be spread from person to person through respiratory droplets. Currently, there is no evidence to support transmission of COVID-19 associated with food. Before preparing or eating food it is important to always wash your hands with soap and water for at least 20 seconds for general food safety.',
        'can the virus stay on a surface',
        'Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard. Common household disinfectants will kill the virus can be used to clean surfaces.',
        'can the virus stay on clothes',
        'Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard. Common household disinfectants will kill the virus can be used to clean surfaces.',
        'How long can the virus last on plastic?',
        'Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard. Common household disinfectants will kill the virus can be used to clean surfaces.',
        'How long can the virus last',
        'Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard. Common household disinfectants will kill the virus can be used to clean surfaces.',
        'can the virus stay on clothes',
        'Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard. Common household disinfectants will kill the virus can be used to clean surfaces.',

    ]

    trainer.train(covidDur)

    washingHands = [

        # Washing Hands

        'How often should I wash my hands?',
        'Wash your hands often. Especially after you have been in a public place, or after blowing your nose, coughing, or sneezing with soap and water for at least 20 seconds. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'how to clean my hands to protect myself from getting the virus',
        'Use soap and water to wash your hands for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'Can you give me tips on washing hands?',
        'Sure. Make sure to wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'is it really that important to wash hands',
        'Yes it is very important to wash your hands. Hand washing with a soap keeps germs away. So, wash hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol. Avoid touching your eyes, nose, and mouth with unwashed hands.',
        'how often should you wash your hands?',
        'Wash your hands especially after you have been in a public place, or after blowing your nose, coughing, or sneezing with soap and water for at least 20 seconds. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'why is it important to wash hands',
        'Hand washing with soap removes germs from hands. This helps prevent infections because: People frequently touch their eyes, nose, and mouth without even realizing it. Germs can get into the body through the eyes, nose and mouth and make us sick',
        'advice for washing hands',
        'Wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'how to wash your hands correctly to limit spread of disease',
        'Wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol. Cover all surfaces of your hands and rub them together until they feel dry. Avoid touching your eyes, nose, and mouth with unwashed hands.',
        'why hand washing matters?',
        'Hand washing with soap removes germs from hands. This helps prevent infections because: People frequently touch their eyes, nose, and mouth without even realizing it. Germs can get into the body through the eyes, nose and mouth and make us sick.',
        'how long do i need to wash my hands?',
        'It is important to Wash your hands with soap and water for at least 20 seconds.',
        'how to clean your hands to protect against coronavirus',
        'Use soap and water to wash your hands for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
        'what do i need to know about washing my hands effectively?',
        'Washing your hands will keep germs away from hands. It is important that you wash hands often with soap and water for at least 20 seconds. If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.',
    ]

    trainer.train(washingHands)

    covidSymp = [

        # Symptoms

        'what are the symptoms of COVID-19',
        'According to the Center for Disease Control and Prevention, current symptoms reported for patients with COVID-19 have included fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'what happens if you get the virus',
        'According to the Center for Disease Control and Prevention, patients with COVID-19 may experience fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'what are the symptoms of coronavirus?',
        'According to the Center for Disease Control and Prevention, current symptoms reported for patients with COVID-19 have included fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'what happens when you get the virus',
        'According to the Center for Disease Control and Prevention, patients with COVID-19 may experience fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'What are the signs of someone who caught Coronavirus?',
        'According to the Center for Disease Control and Prevention, current signs reported for patients with COVID-19 are fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'Is losing sense of smell a symptom of Covid?'
        'According to the Center for Disease Control and Prevention, current symptoms reported for patients with COVID-19 are fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',
        'is chest pain a symptom',
        'According to the Center for Disease Control and Prevention, current symptoms reported for patients with COVID-19 are fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea. Symptoms may appear 2-14 days after exposure. This list does not include all possible symptoms.',

    ]

    trainer.train(covidSymp)

    wearingMask = [

        # Wearing Mask

        'Should I wear a face mask?',
        'CDC recommends that people should wear cloth face coverings in public settings and when around people who don’t live in your household, especially when other social distancing measures are difficult to maintain.',
        'When should I wear a face mask?',
        'CDC recommends that people wear cloth face coverings in public settings and when around people who don’t live in your household, especially when other social distancing measures are difficult to maintain.',
        'Why is it important to wear a mask?',
        'According to CDC, cloth face coverings are most likely to reduce the spread of COVID-19 when they are widely used by people in public settings.',
        'Does wearing a mask reduce the spread of COVID-19',
        'Yes. The spread of COVID-19 can be reduced when cloth face coverings are used along with other preventive measures, including social distancing, frequent handwashing, and cleaning and disinfecting frequently touched surfaces.',
        'What is the benefit of wearing a mask?'
        'Cloth face coverings are recommended as a simple barrier to help prevent respiratory droplets from traveling into the air and onto other people when the person wearing the cloth face covering coughs, sneezes, talks, or raises their voice.',
        'Who should not wear a face mask?'
        'Cloth face coverings should not be worn by children under the age of 2 or anyone who has trouble breathing, is unconscious, incapacitated, or otherwise unable to remove the mask without assistance.',
        'Should everyone wear a mask?',
        'Absolutely not. Cloth face coverings should not be worn by children under the age of 2 or anyone who has trouble breathing, is unconscious, incapacitated, or otherwise unable to remove the mask without assistance.',
        'Do you recommend wearing a face mask?'
        'Yes I highly recommend wearing a cloth face covering. Especially when you are in a public setting. Especially around people who are not from your household.',
        'Why do you recommend wearing a mask?',
        'Cloth face coverings are recommended as a simple barrier to help prevent respiratory droplets from traveling into the air and onto other people when the person wearing the cloth face covering coughs, sneezes, talks, or raises their voice.',

    ]

    trainer.train(wearingMask)

    covidSpread = [

        # COVID-19 Spreading

        'How does the virus spread?',
        'The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs.',
        'Can you explain how the COVID-19 spreads',
        'The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs.',
        'How does the coronavrius spread',
        'The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs.',

    ]

    trainer.train(covidSpread)

    vaccine = [

        # Coronavirus Vaccine

        'Is there a vaccine for coronavirus?',
        'There is currently no vaccine to prevent coronavirus disease 2019 (COVID-19). The best way to prevent illness is to avoid being exposed to this virus. The virus is thought to spread mainly from person-to-person.',
        'Is there a vaccine for COVID-19?',
        'There is currently no vaccine to prevent coronavirus disease 2019 (COVID-19). The best way to prevent illness is to avoid being exposed to this virus. The virus is thought to spread mainly from person-to-person.',
        'Where can I find a vaccine for coronavirus?',
        'There is currently no vaccine to prevent coronavirus disease 2019 (COVID-19). The best way to prevent illness is to avoid being exposed to this virus. The virus is thought to spread mainly from person-to-person.',
        'Where can I find a vaccine for COVID-19',
        'There is currently no vaccine to prevent coronavirus disease 2019 (COVID-19). The best way to prevent illness is to avoid being exposed to this virus. The virus is thought to spread mainly from person-to-person.',

    ]

    trainer.train(vaccine)

    treatment = [

        # Treatment for COVID-19 Patients

        'What to do if you have the coronavirus?',
        'Talk to your doctor and do not leave your home except to get medical care. Get rest and stay hydrated. Take over the counter medicines, such as acetaminophen, to help you feel better.',
        'I think I have the virus.',
        'It is important that you talk to your doctor and do not leave home except to get medical care. Make sure to stay hydrated and take over the counter medicines, such as acetaminophen, to help you feel better.',
        'I think I might have COVID-19',
        'It is important that you talk to your doctor and do not leave home except to get medical care. Make sure to stay hydrated and take over the counter medicines, such as acetaminophen, to help you feel better.',
        'I think I might have coronavirus',
        'It is important that you talk to your doctor and do not leave home except to get medical care. Make sure to stay hydrated and take over the counter medicines, such as acetaminophen, to help you feel better.',
        'How to treat COVID-19 at home?',
        'Get rest and stay hydrated. Take over the counter medicines, such as acetaminophen, to help you feel better. And make sure to stay in touch with your doctor.',
        'When should I seek emergency medical attention?',
        'If someone is showing any sign of trouble breathing, persistent pain in the chest, confusion, bluish lips or face, and inability to stay awake or asleep, then seek emergency medical care immediately!',
        'Any advice on how to treat COVID-19?',
        'Talk to your doctor and do not leave your home except to get medical care. Get rest and stay hydrated. Take over the counter medicines, such as acetaminophen, to help you feel better.',
        'Can you recover from the coronavirus?',
        'Yes. Most people with COVID-19 have mild illness and are able to recover at home without medical care. Do not leave your home, except to get medical care.',
        'Can you recover from the COVID-19?',
        'Yes. Most people with COVID-19 have mild illness and are able to recover at home without medical care. Do not leave your home, except to get medical care.',
        'I am feeling sick.',
        'It is important that you talk to your doctor and do not leave home except to get medical care. Make sure to stay hydrated and take over the counter medicines, such as acetaminophen, to help you feel better.',
        'I am not feeling well',
        'It is important that you talk to your doctor and do not leave home except to get medical care. Make sure to stay hydrated and take over the counter medicines, such as acetaminophen, to help you feel better.',
        'How to treat coronavirus at home?',
        'Get rest and stay hydrated. Take over the-counter medicines, such as acetaminophen, to help you feel better. And make sure to stay in touch with your doctor.',

    ]

    trainer.train(treatment)

    covidProtection = [

        # COVID-19 Protection

        'How to protect myself from coronavirus',
        'It is recommended to wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol- based hand sanitizer that contains at least 60% alcohol.',
        'How to protect myself from covid-19',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',
        'How can I protect myself',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',
        'How to protect yourself from coronavirus',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',
        'How to protect yourself from covid-19',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',
        'coronavirus protection tips',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',
        'covid-19 protection tips',
        'Wear a cloth face covering that covers your nose and mouth in public settings. Clean and disinfect frequently touched surfaces. Wash your hands often with soap and water for at least 20 seconds, or use an alcohol based hand sanitizer that contains at least 60% alcohol.',

    ]

    trainer.train(covidProtection)

    cdc = [

        # CDC Links

        'Where can I learn more about the coronavirus?',
        'I recommend that you visit the official website of Centers for Disease Control and Prevention. Click here to learn more.',
        'I need more information on covid-19',
        'I recommend that you visit the official website of Centers for Disease Control and Prevention. Click here to learn more.',
        'What is CDC?',
        'The Centers for Disease Control and Prevention is a national public health institute in the United States. It is a United States federal agency, under the Department of Health and Human Services.',
        'I want to learn more about coronavirus',
        'Sure. Here is the link to the official website of CDC',
        'Where can I find more information about COVID-19',
        'It is best to visit the official website of Centers for Disease Control and Prevention. Here is the link.',
        'Do you have the link to the CDC website?'
        'Yes, I do. Click here.',
        'I need to visit the CDC website.',
        'Here you go.'

    ]

    trainer.train(cdc)

    while True:
        try:
            bot_input = user_input

            bot_response = chatbot.get_response(bot_input)
            return render(request, 'bot.html', {'bot_response': bot_response})


        except(KeyboardInterrupt, EOFError, SystemExit):
            break


def map(request):
    return render(request, 'map.html')
