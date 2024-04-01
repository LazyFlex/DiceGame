# Dice Game

## Introduction

The Dice Game web application offers users a straightforward and entertaining two-player gaming experience. Players take turns rolling a virtual six-sided die to accumulate points. This document provides an overview of the game's rules, technologies used, game logic, and deployment details.

## Game Rules

- The game is played between two players.
- Players take turns rolling a die by clicking the "Roll" button.
- Rolling a 1 resets the current player's score to 0, passing the turn to the other player.
- Rolling any other number (2-6) adds it to the player's current score.
- Players can choose to "Hold" their current score, adding it to their total and ending their turn.
- The first player to reach or exceed a total score of 20 wins the game.

## Technologies Used

1. **Flask Framework:** Utilized for its simplicity and ease of use in developing web applications.
2. **Jinja Templating Engine:** Rendered dynamic content in HTML templates by integrating Python code with HTML files.
3. **Bootstrap Framework:** Enhanced the visual appeal and responsiveness of the user interface.
4. **Random Number Generation:** Utilized Python's random module to simulate die rolls.

## Game Logic

1. **Player Data Structure:** Stored player information (name and score) in a dictionary for easy access and manipulation.
2. **Turn-Based Gameplay:** Implemented turn-based logic, allowing players to roll the die and accumulate points.
3. **Winning Condition:** The game concludes when one player reaches a total score of 20 or more points, determining the winner based on the highest score at that point.

## Deployment

The application was initially deployed on a virtual EC2 machine on AWS for remote access. After exhausting the free credit, it was migrated to vercel.com for continued availability.

## User Experience

1. **Real-Time Updates:** Provides real-time updates on player scores, current turns, and dynamically displays the rolled die for an engaging user experience.
2. **New Game Functionality:** Allows players to start a new game, resetting scores and initiating a fresh round of play.
