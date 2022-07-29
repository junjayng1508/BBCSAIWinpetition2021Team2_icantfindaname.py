# BBCS AIWinpetition 2021 - Team 2

## **Topic**: Team Bonding
Note that instructions on running the code are found near the bottom of the page.

---
## How the Code Works

### Initialising the variables
- It initialises the variables needed to operate the timer and calculate the score.
- It then randomly selects a theme using Python's random module from a dictionary of themes and sentences.
- Thereafter, it picks a sentence under the theme.
- After picking, it would define a timer function, which would then be threaded later and used as a timer for the game.

In layman terms, it creates a timer, which would be started later on.
A function called ``get_ai_response()``, which calls the API to generate sentences, would be initialised too.

### Getting players and starting the Game
- Main user would then have to input the number of players. If the number of players are <2, or is invalid, it will ask for a valid input again.
- A welcome message would then be shown, and the game would start after the player presses the "Enter" key on the keyboard.
- The moment the player hits the "Enter" key, it would start a thread which targets the timer function.

In layman terms, this starts the timer.

### What Happens while the game is running?
- The code would loop forever till the timer is done.
- While the code is looping, it would ask all the players for a input to contribute to the story.
- Scores for each player would be added based on their word count.
- After each player has typed their sentences, an AI, which would be called via the function ``get_ai_response()``, would contribute its own ideas.
- It would then check if the timer is up, and do the necessary follow-up actions.

### When the game ends
- When it ends, the system would tally up the scores of each player.
- It would then announce the winner, followed by the group's total score.

---
## How the AI function works

### Requesting to the API
- The AI function uses a Python library [``requests``](https://pypi.org/project/requests/), to send a ``GET`` request to [deepai](https://api.deepai.org/api/text-generator), with an API key and the content as headers.
- The content would be the last 2 sentences that were typed, this way, the AI would be able to generate a answer that relates to the topic more.

### Converting the raw data
- The response would then be converted into a JSON-serializable object (also known as a ``dict`` in Python).
- The code would then parse the data, and return the first 2 lines, as the original text would be too long.
- It would then return the text, which would be printed out.

---
## Summary

- Created a variable and a countdown timer
- Also made a score counter stating each player's score at the end
- Selected a few themes and related starter sentences, and "grouped" them accordingly
    - A theme and starter sentence will be randomly selected for each game.
- Players have to input the number of players and their names and the number of players cannot be less than 2 else an error message will show
- An instruction will be given including a welcome message and the amount of time they have to play
- After a player hits the "Enter" key, the timer will begin and each player has to input a word and after all of them have finished inputting, the AI will continue with the story and respond and the same thing happens over and over again
- After the time is up, it will finalise and type out the final story
- The individual score of each player, whole group's score and winner will also be printed out. if it is a tie-breaker, it will show "Draw!"

Thats it!

---
## Requirements

### Installation
You would need the Python library, [``requests``](https://pypi.org/project/requests/), which can be installed using the following commands:

```sh
# Linux/macOS
python3 -m pip install -U requests

# Windows
py -3 -m pip install -U requests
```

### How to operate the Never-ending Story game?
1. Download the final product [here]().
2. Install the necessary modules by reading the guide above this sub-section.
3. Run the file and enjoy the game. Have fun!
