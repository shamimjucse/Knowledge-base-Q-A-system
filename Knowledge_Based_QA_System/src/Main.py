# prolog
from pyswip import Prolog

# text to speech
from gtts import gTTS
import pygame

# speech to text
import speech_recognition as sr

import json
import time
#import os


audio_id = 1

def text_to_speech(txt):
    global audio_id
    language = "en"
    obj = gTTS(text=txt, lang=language)
    obj.save("audio/output" + str(audio_id) + ".mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio/output" + str(audio_id) + ".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.pause()
    audio_id = audio_id + 1


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)
    return results


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += "\""
            continue

        json_str += c

    return json_str


def ask_question(query_string):
    ret_answers = prolog_query(query_string)
    return ret_answers


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        text_to_speech(text)


def listen_question():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("ask question about jahangirnagar university")
        audio = r.listen(source)
        print("ok.. wait for the answer...")

    try:
        return r.recognize_google(audio)
    except:
        return "-----------------"


text_to_speech("Hi, I'm here to tell you about jahangirnagar university. \
               what do you want to know about jahangirnagar university?")
flg = True
while flg:
    # Q/A
    asked_question = str(listen_question()).lower()
    print(asked_question)

    if "name of the university" in asked_question or \
            "university name" in asked_question:
        # Q: what is the name of the university?
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("The name of the university ", "", question, answers)

    elif "introduction" in asked_question or \
            "about ju" in asked_question or \
            "about jahangirnagar university" in asked_question:
        # Q: what is jahangirnagar university?
        question = "Introduction"
        query = "introduction('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "history of ju" in asked_question or \
            "history of jahangirnagar university" in asked_question:
        # Q: history of jahangirnagar university.
        question = "History"
        query = "history('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("Brief history: ", "", question, answers)

    elif "location of jahangirnagar university" in asked_question or \
            "situated" in asked_question:
        # Q: where is jahangirnagar university?
        question = "Loction"
        query = "location('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "area of jahangirnagar university" in asked_question:
        # Q: where is jahangirnagar university?
        question = "Area"
        query = "area('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("total area of jahangirnagar university is about ", "", question, answers)

    elif ("current" in asked_question or "present" in asked_question or "now" in asked_question) \
            and ("vice chancellor" in asked_question or \
                 "vc" in asked_question):
        # Q: who is the current vice_chancellor of jahangirnagar university?
        question = "Vice_chancellor"
        query = "vice_chancellor('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("The current vice chancellor of jahangirnagar university is ", \
                    "", question, answers)

    elif "number of faculties" in asked_question or \
            "how many faculties" in asked_question and \
            asked_question.find("faculty of") == -1:
        # Q how many faculties are in jahangirnagr university
        question = "Number_of_faculties"
        query = "number_of_faculties('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("There are ", "faculties in jahangirnagar university", question, answers)

    elif "number of departments" in asked_question or \
            "how many departments" in asked_question:
        # Q how many departments are in jahangirnagr university
        question = "Number_of_departments"
        query = "number_of_departments('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("There are ", "departments in jahangirnagar university", question, answers)

    elif "number of institutes" in asked_question or \
            "how many institutes" in asked_question:
        # Q how many institutes are in jahangirnagr university
        question = "Number_of_institutes"
        query = "number_of_institutes('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("There are ", "institutes in jahangirnagar university", question, answers)

    elif "names of the faculties" in asked_question or \
            "what are the faculties" in asked_question:
        # Q what are the faculties in jahangirnagar university
        question = "Facultiy"
        query = "faculties('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("there are 6 faculties are in jahangirnagar university, they are, ", \
                    "", question, answers)

    elif ("names of the departments" in asked_question or \
          "what are the departments" in asked_question) and \
            "under the faculty of" in asked_question:
        # Q what are the names departments in faculty of X?
        faculties = ["faculty of mathematical and physical science", \
                     "faculty of biological science", \
                     "faculty of social science", \
                     "faculty of arts and humanities", \
                     "faculty of business studies", \
                     "faculty of law"]
        id = -1
        for i in range(6):
            if faculties[i] in asked_question:
                id = i
                break
        if id != -1:
            print(faculties[id])
            question = "Departments"
            query = "departments_under_faculty('jahangirnagar university', '" + \
                    faculties[id] + "'," + question + ")."
            answers = ask_question(query)
            text_to_speech("the departments under " + faculties[id] + " are, ")
            say_answers("", "", question, answers)

        else:
            text_to_speech("sorry, there is no such faculty.")

    elif "names of the departments" in asked_question or \
            "what are the departments" in asked_question:
        # Q what are the departments in jahangirnagar university
        question = "Departments"
        query = "departments('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("there are 34 departments in jahangirnagar university, they are, ", \
                    "", question, answers)

    elif "about department of cse" in asked_question or \
            "about cse" in asked_question or \
            "about computer science and engineering" in asked_question or \
            "about department of computer science and engineering" in asked_question:
        # Q what you know about dept of CSE jahangirnagar university
        question = "Cse"
        query = "about_department_of_computer_science_and_engineering(\
                'jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "chairman of department of cse" in asked_question or \
            "chairman of cse" in asked_question or \
            "chairman of computer science and engineering" in asked_question or \
            "chairman of department of computer science and engineering" in asked_question:
        # Q who is the chairman of dept of CSE JU?
        question = "Chairman"
        query = "chairman_of_cse('department of computer science and engineering', " \
                + question + ")."
        answers = ask_question(query)
        say_answers("", "is the chairman of department of computer science and engineering", question, answers)

    elif "who are the developers of this project" in asked_question or \
            "who developed" in asked_question or "who created" in asked_question:
        # Q who developed this program?
        question = "Developers"
        query = "developers(" + question + ")."
        answers = ask_question(query)
        text_to_speech("This project is supervised by professor doctor mohammad shorif uddin.")
        say_answers("the developers are", "", question, answers)

    elif "stop" in asked_question or "exit" in asked_question:
        text_to_speech("thank you, hope you have enjoyed the session")
        break

    else:
        if asked_question != "-----------------":
            text_to_speech("Sorry, this is out of my knowledge. whould you like to continue?")
            confirmation = str(listen_question()).lower()
            print(confirmation)
            if "no" in confirmation or "nope" in confirmation or "stop" in confirmation:
                text_to_speech("thank you, hope you have enjoyed the session")
                break
            else:
                time.sleep(5)
                continue

        time.sleep(5)
