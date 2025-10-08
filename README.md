# Sliding-Game-Puzzle ✅

- [x] Blank Tile Start: Ensure that every new game starts with the blank tile at bottom-right (4,4).

- [x] Blank Tile Display: Show the blank tile as "Z" (not None or empty) on the grid and in all outputs.

- [x] Win Condition: Confirm the win check matches A → O followed by Z at the end.

- [ ] Record Moves & Time: Store both move count and time (MM:SS) in the leaderboard JSON.

- [ ] Sort & Filter Leaderboard: Sort by difficulty → time, and display top-3 entries only.

- [ ] Checkpoint/Resume: Ensure the game can save and resume with all data: grid, blank position, move count, elapsed time, and full move history.

- [ ] Track Actual Moves: Store a list of tile labels moved (e.g., ["C","G","D",…]) or directions ("UP", "LEFT") instead of just blank coordinates.

- [ ] Save & Load History: Include move history in checkpoint JSON for proper resumption.

- [x] Grid Drawing: Verify the grid always draws with correct positions and labels, including Z for the blank.

- [x] Time Format: Display timer in MM:SS format consistently.

- [] Moves Display: Update and display the move count on the interface.

- [x] Remove Unneeded Dependencies: Delete references to random2, os-sys, and pip-install notes for standard libraries.

- [x] Simplify Imports: Use only standard Python libraries (random, json, time, turtle).

- [x] Improve Naming: Use clear, consistent names for functions and variables (e.g., draw_grid(), save_game(), check_win()).

- [ ] Add Brief Comments: Provide short doc-style comments for core functions:
  - `draw_grid()` – draw board and tiles  
  - `handle_input()` – process arrow keys  
  - `save_game()` / `load_game()` – checkpoint/resume  
  - `check_win()` – evaluate winning condition

- [x] Test all difficulty levels (easy/medium/hard) to ensure solvable layouts and correct starting position.

- [x] Confirm JSON save/load works across sessions.

- [x] Review for consistent style and “student-written” clarity.
