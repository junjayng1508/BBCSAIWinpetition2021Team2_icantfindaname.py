# BBCSAIWinpetition2021_Team2_icantfindaname.py 
## Topic: **Team Bonding**
Note: Steps on How to Run the Code are found near the bottom of the page.

## How the Code Works
### Initialising the variables
It initialises the variables needed to operate the timer and calculate the score.
It then randomly selects a theme using python's random module from a dictionary of themes and sentences.
Then, it picks a sentence under the theme.
After picking, it would define a timer function, which would then be Threaded later and used as a timer for the game.
(In layman terms, it creates a timer, which would be started later)
A function called getAIresponse(), which calls the API to generate sentences, would be initialised too.

### Getting Players and Starting the Game
User would then have to input the number of players. If the number of players are < 2, or is invalid, it will ask for a input again.
A welcome message would then be shown, and the game would start after the player presses "Enter".
When the player presses "Enter"
The moment the player presses "Enter", it would start a Thread, which targets the timer function.
(In layman terms, this starts the timer)

### What Happens while the Game is Running?
The code would loop forever till the timer is done.
While the code is looping, it would ask all the players for a input to contribute to the story.
Scores for each player would be added based on their word count.
After each player has typed their sentences, an AI, which would be called via the function getAIresponse(), would contribute it's own ideas
It would then check if the timer is up, and do the necessary actions.

### When the Game Ends
When it ends, the game would tally up the scores of each player.
It would then announce the winner, followed by the group's total score.

### How the AI function works
The AI function uses the requests library to send a GET request to "https://api.deepai.org/api/text-generator", with a API key, and the content as headers.
The content would be the last 2 sentences that were typed, this way, the AI would be able to generate a answer that relates to the topic more.
The response would then be converted into a json format.
The code would then parse the json data, and return the first 2 lines, as the original text would be too long.
It would then return the text, which would then be printed out.


## Summary
we created a variable and a countdown timer

we also created a score counter stating each player's score at the end.

we selected a few themes and related starter sentences and "grouped" them accordingly.

a theme and starter sentence will be randomly selected for each game.

players have to input the number of players and their names and the number of players cannot be less than 2 else an error message will show.

an instruction will be given including a welcome message and the amount of time they have to play. 

after a player presses "Enter", the timer will begin and each player has to input a word and after all of them have finished inputting, the AI will continue with the story and respond and the same thing happens over and over again.

after the time is up, it will finalise and type out the final story.

the individual score of each player, whole group's score and winner will also be printed out. if it is a tie-breaker, it will show "Draw!".

thats it!


# Requirements
You need the "requests" library, and you can download it using `pip install requests`

# How to operate the Never-Ending Story game?
 1. Download the file.
 2. Install the necessary modules.
 3. Run the file and enjoy the game!
