greeting(hello).
greeting(hi).
greeting(hii).
greeting(hey).
greeting(good_morning).
greeting(good_afternoon).
greeting(good_evening).

response(hello, 'Hello! How can I help you?').
response(hi, 'Hi! Nice to meet you.').
response(hii, 'Hello! What can I do for you?').
response(hey, 'Hey! How are you?').
response(good_morning, 'Good morning! Have a great day.').
response(good_afternoon, 'Good afternoon! How can I help you?').
response(good_evening, 'Good evening! How was your day?').

question(name).
question(age).
question(subject).
question(language).
question(college).

answer(name, 'My name is AIML Bot.').
answer(age, 'I am a computer program created using Prolog.').
answer(subject, 'I can help you with Artificial Intelligence and Machine Learning.').
answer(language, 'I am written in Prolog programming language.').
answer(college, 'I am your virtual study assistant.').

study_topic(ai).
study_topic(ml).
study_topic(prolog).
study_topic(python).
study_topic(data_science).

study_response(ai, 'Artificial Intelligence is the field of making machines intelligent.').
study_response(ml, 'Machine Learning allows computers to learn from data.').
study_response(prolog, 'Prolog is a logic programming language used in AI applications.').
study_response(python, 'Python is a popular programming language used in AI and Machine Learning.').
study_response(data_science, 'Data Science involves collecting, processing and analyzing data.').

mood(happy).
mood(sad).
mood(tired).
mood(excited).

mood_response(happy, 'That is great! Keep smiling.').
mood_response(sad, 'I am sorry to hear that. Everything will be okay.').
mood_response(tired, 'Take some rest and come back when you feel better.').
mood_response(excited, 'That is wonderful! Keep the excitement going.').

command(help).
command(thanks).
command(bye).
command(exit).

command_response(help, 'I can talk about AI, ML, Prolog, Python and Data Science.').
command_response(thanks, 'You are welcome!').
command_response(bye, 'Goodbye! Have a great day.').
command_response(exit, 'Chatbot session ended. Goodbye!').

chat(Input, Output) :-
    greeting(Input),
    response(Input, Output).

chat(Input, Output) :-
    question(Input),
    answer(Input, Output).

chat(Input, Output) :-
    study_topic(Input),
    study_response(Input, Output).

chat(Input, Output) :-
    mood(Input),
    mood_response(Input, Output).

chat(Input, Output) :-
    command(Input),
    command_response(Input, Output).
