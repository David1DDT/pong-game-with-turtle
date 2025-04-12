# pong-game-with-turtle
Pong Game in Python using Turtle Graphics
This Python code implements a simple Pong game using the Turtle graphics library. The game features two paddles controlled by the players and a ball that bounces between them. The objective is to prevent the ball from passing your paddle while trying to score points against your opponent.

Key Features:
Game Setup: A game window with a black background and specified dimensions (800x600 pixels) is created.
Paddle Movement:
The right paddle is controlled using the "Up" and "Down" arrow keys.
The left paddle is controlled using the "W" and "S" keys.
Ball Movement: The ball moves continuously and bounces off the top and bottom walls.
Collision Detection: The ball bounces back when it collides with the paddles. If the ball passes a paddle, the opposing player scores a point.
Scoreboard: The current score for both players is displayed at the top of the screen, updating each time a point is scored.
Game Loop: The main game loop continuously updates the game state, moving the paddles and the ball, checking for collisions, and rendering updates to the screen.
Game Controls:
Player 1 (Left Paddle): 

Move Up: W
Move Down: S
Player 2 (Right Paddle):

Move Up: Up Arrow
Move Down: Down Arrow
Implementation Notes:
The code utilizes custom classes for the ball, paddles, and scoreboard, promoting modularity and easy maintenance.
The paddle and ball are both represented using Turtle graphics objects, with appropriate methods defined for movement and interaction.
The game features simple logic for scoring and resetting the game state when a point is scored.
This Pong game serves as a fundamental illustration of game development concepts in Python, such as event handling, object-oriented programming, and real-time game loop mechanics.
