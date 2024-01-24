## Project Description:

"Avoiding the enemies" is a fun and engaging game crafted using the Pygame library in Python. Picture yourself controlling a nimble block, navigating through a storm of falling enemy blocks. Your mission: dodge, weave, and accumulate points to prove your skills. The arrow keys are your allies, guiding your block left and right as you strive to avoid collisions with the relentless descent of enemy blocks.

## Key Features:

### Gameplay Mechanics:

        The player controls a block using left and right arrow keys to avoid collisions with falling enemy blocks.
        Falling enemy blocks are generated randomly, providing a challenging and dynamic gameplay experience.

### Scoring System:

        The player earns points as they successfully avoid collisions with enemy blocks.
        The score is displayed in real-time on the game screen.

### High Score Tracking:

        The game keeps track of high scores, storing player names and their corresponding scores in a file ("highscores.txt").
        High scores are displayed during the game over screen.

### Dynamic Difficulty:

        The speed of falling enemy blocks gradually increases as the player's score progresses.

### User Interaction:

        The game prompts the user to input their name at the beginning of each session.
        Upon game over, the player has the option to play again or exit the game.

### Input Handling:

        The game captures user input for player movement and decision-making (e.g., play again).

### Error Handling and Messaging:

        The game provides informative error messages, such as when a player attempts to use an existing name in the high score list.

### Graphics and Display:

        The game uses Pygame for graphics and display functionalities, featuring a simple and clean user interface.

### Modularity:

        The code is structured into functions and employs object-oriented programming for managing different enemy shapes.

### File Handling:

        High scores are read from and written to a file for persistent storage across game sessions.

### Smooth Flow:

        Enhancements have been made to ensure a smoother flow, such as displaying the final score and high scores after the player decides not to play again.
