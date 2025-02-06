# Ping Pong Game 🎮

This is a simple **Ping Pong game** implemented using Python's `turtle` graphics module. The game consists of two players controlling paddles to hit a ball back and forth. The first player to miss the ball gives a point to the opponent, and the game continues.

## Features

- **2-Player Control**:
  - Player 1 controls the red paddle using the **Up** and **Down** arrow keys.
  - Player 2 controls the blue paddle using the **W** and **S** keys.
  
- **Scoring System**: The score is displayed at the top of the window, and it updates every time a player scores a point by making the opponent miss the ball.

- **Realistic Ball Movement**: The ball bounces off the top and bottom walls and can be hit back by the paddles.

- **Center Divider**: A white line divides the game board for a clean visual reference.

## Prerequisites

- Python 3.x
- `turtle` module (comes pre-installed with Python)

## How to Run the Game

1. Clone or download the repository.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt in the project folder.
4. Run the game using the following command:
   ```bash
   python ping_pong_game.py
   ```

## How to Play

- **Player 1** (Red Paddle): 
  - Press the **Up arrow** to move the paddle up.
  - Press the **Down arrow** to move the paddle down.

- **Player 2** (Blue Paddle):
  - Press the **W** key to move the paddle up.
  - Press the **S** key to move the paddle down.

- The ball will automatically start moving when the game begins.
- Each player should try to hit the ball and prevent it from passing their paddle.
- If a player misses the ball, the other player scores a point, and the ball resets to the center.

## Code Structure

- **Window Setup**: Initializes the game window with a specific size and background color.
- **Ball**: A moving object that players interact with.
- **Players**: Two paddles (red and blue) controlled by the players.
- **Score System**: Tracks and displays the score for both players.
- **Collision Detection**: Detects if the ball hits the paddles or walls and bounces accordingly.
- **Boundary Checks**: Ensures paddles stay within the window boundaries.



## Screenshots

- Player 1 (Red) vs Player 2 (Blue) with the ball in play:
  ![Ping Pong Gameplay]([./[screenshots/ping_pong_gameplay.png](https://github.com/MohammedHamza0/pingPong/blob/main/Screenshot%202025-02-06%20121930.png)](https://github.com/MohammedHamza0/pingPong/blob/main/Screenshot%202025-02-06%20121930.png))  
