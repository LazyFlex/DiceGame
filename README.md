
# Dice Game

**Introduction**

The Dice Game web application was developed to provide users with a simple and
enjoyable two-player gaming experience. The game involves rolling a virtual six-sided
die, with players taking turns to accumulate points. The following is an overview of the
development process.

**Technologies Used**
1. Flask Framework:
Flask, a Python web framework, was chosen for its simplicity and ease of use.
Flask facilitates the creation of web applications with minimal boilerplate code.
2. Jinja Templating Engine:
Jinja was employed for rendering dynamic content in HTML templates.
It seamlessly integrates with Flask, allowing for the inclusion of Python code in
HTML files.
3. Bootstrap Framework:
Bootstrap, a front-end framework, was utilized to enhance the visual appeal of
the application. The Bootstrap components were integrated to create a modern and responsive user interface.
4. Random Number Generation:
The random module in Python was used to generate random numbers
representing the die rolls.

**Game Logic**
1. Player Data Structure:
Player information, including name and score, was stored in a dictionary for
easy access and manipulation.
2. Turn-Based Gameplay:
The game implements turn-based logic, allowing players to roll the die and
accumulate points in each round.
3. Winning Condition:
The game concludes when one of the players reaches a total score of 20 or
more points.
The winner is determined based on the highest score at this point.

**Deployment**

The application is initially deployed in a virtual EC2 machine on AWS, allowing for remote access until the free credit were done. Then it  was deployed on vercel.com

**User Experience**
1. Real-Time Updates:
The application provides real-time updates on player scores, current turns, and
dynamically displays the rolled die for an engaging user experience.
2. New Game Functionality:
Players have the option to start a new game, resetting scores and initiating a
fresh round of play.

[**YouTube Link**](https://youtu.be/DHZy6VGgOzY)
