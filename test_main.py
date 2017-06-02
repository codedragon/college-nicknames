#!/usr/local/bin/python3

import pytest
from main import populate_game_questions, get_welcome_response, build_response


GAME_LENGTH = 5
SKILL_NAME = "College Nicknames"

QUESTIONS = [
    {"What is the nickname for University of Washington?": ["Huskies"]},
    {"What is the nickname for Abilene Christian University?": ["Wildcats"]},
    {"What is the nickname for Adams State?": ["Grizzlies"]},
    {"What is the nickname for Adelphi": ["Panthers"]},
    {"What is the nickname for Adrian College?": ["Bulldogs"]},
    {"What is the nickname for Air Force?": ["Falcons"]},
]

sample_event = {
  'session': {
    'sessionId': "SessionId.6ab325dd-xxxx-xxxx-aee5-456cd330932a",
    'application': {
      'applicationId': "amzn1.echo-sdk-ams.app.bd304b90-xxxx-xxxx-86ae-1e4fd4772bab"
    },
    'attributes': {},
    'user"': {
      "userId": "amzn1.ask.account.XXXXXX"
    },
    'new': "true"
  },
  'request': {
    'type': "IntentRequest",
    'requestId': "EdwRequestId.b851ed18-2ca8-xxxx-xxxx-cca3f2b521e4",
    'timestamp': "2016-07-05T15:27:34Z",
    'intent': {
      'name': "GetTrainTimes",
      'slots': {
        'Station': {
          'name': "Station",
          'value': "Balboa Park"
        }
      }
    },
    'locale': "en-US"
  },
  'version': "1.0"
}

sample_intent = {
    'name': "GetTrainTimes",
    'slots': { 
        'Station': {
            'name': "Station",
            'value': "Balboa Park"
        }
    }
}

def test_build_response():
    sessionAttr={'speech_output': "Let's play College Nicknames. I will ask you 5 questions. Try to get as many right as you can. Just say the answer. Let's begin. What is the nickname for Adelphi",
        'reprompt_text': 'What is the nickname for Adelphi',
        'current_questions_index': 0,
        'questions': [3, 5, 1, 4, 0],
        'score': 0,
        'correct_answers': ['Panthers']
        }
    responseAttr={'outputSpeech': {
            'type': 'PlainText',
            'text': "Let's play College Nicknames. I will ask you 5 questions. Try to get as many right as you can. Just say the answer. Let's begin. What is the nickname for Adelphi"
            }
        }
    build_resp=build_response(sessionAttr, responseAttr)

    assert build_resp['sessionAttributes']['speech_output'] == sessionAttr['speech_output']
    assert build_resp['sessionAttributes']['reprompt_text'] == sessionAttr['reprompt_text']
    assert build_resp['sessionAttributes']['current_questions_index'] == sessionAttr['current_questions_index']
    assert build_resp['sessionAttributes']['score'] == sessionAttr['score']
    assert build_resp['sessionAttributes']['correct_answers'] == sessionAttr['correct_answers']

    assert build_resp['response']['outputSpeech']['type'] == responseAttr['outputSpeech']['type']
    assert build_resp['response']['outputSpeech']['text'] == responseAttr['outputSpeech']['text']



def begin_statement_test(begin_input):
    assert "Let's play" in begin_input
    assert "I will ask you" in begin_input
    assert "5 questions" in begin_input
    assert "Just say the answer" in begin_input
    assert "Let's begin" in begin_input

def test_populate_game_questions():
    gq = populate_game_questions()

    assert len(gq) == GAME_LENGTH

    for i in gq:
        assert i in (0, 1, 2, 3, 4, 5)

    #print (gq)
    #assert false

def test_get_welcome_response():
    welcome_response = get_welcome_response()

    sessionAttr = welcome_response['sessionAttributes']

    begin_statement_test(sessionAttr['speech_output'])

    assert sessionAttr['current_questions_index'] == 0
    assert sessionAttr['score'] == 0

    assert sessionAttr['current_questions_index'] == 0
    assert len(sessionAttr['questions']) == GAME_LENGTH
    assert sessionAttr['score'] == 0

    index = sessionAttr['questions'][0]
    question = (list(QUESTIONS[index].keys())[0])
    assert question in sessionAttr['speech_output']
    assert question in sessionAttr['reprompt_text']

    if question is "What is the nickname for University of Washington?":
        assert "Huskies" in sessionAttr['correct_answer']
    if question is "What is the nickname for Abilene Christian University?": 
        assert "Wildcats" in sessionAttr['correct_answer']
    if question is "What is the nickname for Adams State?":
        assert "Grizzlies" in sessionAttr['correct_answer']
    if question is "What is the nickname for Adelphi":
        assert "Panthers" in sessionAttr['correct_answer']
    if question is "What is the nickname for Adrian College?":
        assert "Bulldogs" in sessionAttr['correct_answer']
    if question is "What is the nickname for Air Force?":
        assert "Falcons" in sessionAttr['correct_answer']

    responseAttr = welcome_response['response']
    begin_statement_test(responseAttr['outputSpeech']['text'])

    assert "Plain" in responseAttr['outputSpeech']['type']
    assert "Simple" in responseAttr['card']['type']
    assert SKILL_NAME in responseAttr['card']['title']

    begin_statement_test(responseAttr['card']['content'])

    # test reprompt
    assert "PlainText" in responseAttr['reprompt']['outputSpeech']['type']
    assert question in responseAttr['reprompt']['outputSpeech']['text']
    assert responseAttr['shouldEndSession'] is False

def test_handle_answer_request():

 
    assert false
