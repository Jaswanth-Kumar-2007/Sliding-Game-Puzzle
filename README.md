# Sliding-Game-Puzzle

## Project Duration

I took Around 35-45 Hours to complete this Project. Most of the time was
 spent on Movement of Letters and Leaderboard ordering and saving ,
  loading the checkpoints.

## Requirements

We should install the same requirements that Turtle , Random , Os , Json

- Turtle ---> Design the screen and output
- Random ---> Randomize the difficulties in my game
- Os ,jSON ---> Stores and Loads the Checkpoint  and data of players.

## Idea

My Idea was to First input name and difficulty it was stored by
save_name and checkpoint_save after that it draws square and next by
difficulty the letters will be filled in boxes and by turtle.listen()
it listen the movement function by arrows and next it moves as per on key and after all are in order check win if it satisfies opens the win
screen and next leaderboard screen If you are a player stopped at middle
can open game and if you want to continue enter Y or y to proceed it loads your checkpoint .To Open leaderboard at middle of game click l to close game click c.

## Functions Used in Code

- save_name() ---> Makes a new file "name_data.json" and saves the player name to file

- load_name() ---> Open the files to add the name to the file "name_data.json"

- draw_grid() ---> Draws the specified 4x4 Square

- checkpoint_save() ---> Save the Points , Movecount , Timecount to the file created with name.json

- checkpoint_load() ---> Loads the points to the board if the player checkpoint is found and he wants to continue the game

- leaderboard() ---> Prints the names according to the time and difficulty it loads data from load_name and checkpoint_load and display after win . It was sorted

- update_move , update_time , difficulty_show , prints on screen and updates per every second

- writes() ---> Works like swap changes the numbers from position at Up(),Down(),Left(),Right() and display

---

## CheckList

- [x] Blank Tile Start: Ensure that every new game starts with the blank tile at bottom-right (4,4).

- [x] Blank Tile Display: Show the blank tile as "Z" (not None or empty) on the grid and in all outputs.

- [x] Win Condition: Confirm the win check matches A → O followed by Z at the end.

- [x] Record Moves & Time: Store both move count and time (MM:SS) in the leaderboard JSON.

- [x] Sort & Filter Leaderboard: Sort by difficulty → time, and display top-3 entries only.

- [x] Checkpoint/Resume: Ensure the game can save and resume with all data: grid, blank position, move count, elapsed time, and full move history.

- [x] Track Actual Moves: Store a list of tile labels moved (e.g., ["C","G","D",…]) or directions ("UP", "LEFT") instead of just blank coordinates.

- [x] Save & Load History: Include move history in checkpoint JSON for proper resumption.

- [x] Grid Drawing: Verify the grid always draws with correct positions and labels, including Z for the blank.

- [x] Time Format: Display timer in MM:SS format consistently.

- [x] Moves Display: Update and display the move count on the interface.

- [x] Remove Unneeded Dependencies: Delete references to random2, os-sys, and pip-install notes for standard libraries.

- [x] Simplify Imports: Use only standard Python libraries (random, json, time, turtle).

- [x] Improve Naming: Use clear, consistent names for functions and variables (e.g., draw_grid(), save_game(), check_win()).

- [x] Add Brief Comments: Provide short doc-style comments for core functions:
  - `draw_grid()` – draw board and tiles  
  - `handle_input()` – process arrow keys  
  - `save_game()` / `load_game()` – checkpoint/resume  
  - `check_win()` – evaluate winning condition

- [x] Test all difficulty levels (easy/medium/hard) to ensure solvable layouts and correct starting position.

- [x] Confirm JSON save/load works across sessions.

- [x] Review for consistent style and “student-written” clarity.
