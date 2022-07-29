"""
MIT License

Copyright (c) 2022 Jun Jay Ng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import (
    Dict,
    List
)
import random
import threading
import time
import datetime

import requests


# Variables
game_running = True
sentences = []
time_left = t = 60 * 1


# Player score
# Structure: [p1 score, p2 score, p3 score and so on...]
scores = []


# Themes which will be randomised and used
themes_mapping: Dict[str, List[str]] = { 
  # Structure: {theme: [sentences]}
    'Flight': [
        'There once was a flying pig', 
        'The rocket was beside the plane',
        'The man invented a portable wing'
    ],
    'Fairy Tale': [
        'Once upon a time....',
        'There once was a princess',
        'Her hair was long, '
    ],
    'Social Media': [
        'The media is a reliable source of information',
        'Social media is the way of communication'
    ],
    'Studies': [
        'Studying is',
    ],
}

# Select a theme from the dict
theme = random.choice(list(themes_mapping.keys()))
# Select a sentence from the chosen theme
sentence = random.choice(list(themes_mapping[theme]))

# Get AI response
def get_ai_response() -> str:
    if len(sentences) > 1:
        string = sentences[-2] + sentences[-1]
    else:
        string = sentences[-1]

    data = requests.post(
        url='https://api.deepai.org/api/text-generator',
        data={'text': string},
        headers={'api-key': '8d73203a-4c9b-464d-8e8c-df5b0f6934a0'}
    )
    data = data.json()
    if data['output'] == '':
        return "Umm... I don't know what to respond :|"
    else:
        return (data['output'].split('\n')[0])[len(string):]

# Get the number of players
number_of_players = input('🧍 Number of players:\n> ')
player_names = []

while True:
    try:
        number_of_players = int(number_of_players)
        if number_of_players > 0:
            break
        raise ValueError
    except ValueError:
        print('❌ Invalid input! Value must be a number greater than 1.')
        print('Please re-enter a valid input!\n')
        number_of_players = input('🧍 Number of players:\n> ')

# Get the name of players
for i in range(number_of_players):
    name = input(f"🧑 Player {i + 1}'s name:\n> ")
    player_names.append(name)
    scores.append(0)


# Set timer thread
def countdown(t: int) -> None:
    global game_running, time_left
    while t > 0:
        time.sleep(1)
        time_left -= 1
        t -= 1

    game_running = False

# Set time
timer_thread = threading.Thread(
    target=countdown,
    args=(t,)
)

# Give instructions
print('\n\n👋 Welcome to the Never-ending Story game!')
print(f'\n⏰ You guys will have {int(t / 60)} minutes to come up with the story!')
print('Scores will be based on the number of words entered.\n')

# Story time
print(f'🎲 The theme generated is: \n> {theme}\n')
# Just a space to seperate theme from starter sentence
print('💬 The starter sentence is:')
print(f'> {sentence}\n\n-----------')
print('⌨ Type a word and hit the "Enter" key on your keyboard to start the game!\n')

# Start da timer after user hits "Enter" key
timer_thread.start()

while game_running:
    if not game_running:
        break

    for i in range(number_of_players):
        if not game_running:
            break
        print(
            f"{player_names[i]}'s turn: ({datetime.timedelta(seconds=time_left)} left)"
        )
        answer = input('> ')
        sentences.append(answer)
        scores[i] += len(answer.split(' '))
    
    # AI response
    print("AI's response: ")
    print('> ', end='')
    if not game_running:
        break  # Check if time is up

    response = get_ai_response()
    print(response)
    sentences.append(response)


# Time's up
print('\n\n-----------\n⌛ Time is up!')
print('The story you guys made is...')
print(f"{sentence} {' '.join(sentences)}\n")
print('\n-----------\n🛹 Scores:')
for i in range(len(scores)):
    print(f'> {player_names[i]} - {scores[i]}')

indices = [i for i, x in enumerate(scores) if x == scores[scores.index(max(scores))]]
if len(indices) > 1:
    print('\n📍 Draw!')
else:
    print(f'\n🥇 Winner:')
    print(f'> {player_names[scores.index(max(scores))]}')

total = 0
for x in scores:
    total += x
print(f'\nTotal score:\n> {total} points')

print('💪 Thank you everyone for playing!')
