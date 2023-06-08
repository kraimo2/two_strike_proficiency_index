# TSPI Calculator

This Python script allows you to calculate the Two-Strike Proficiency Index (TSPI) for any baseball player and compare it to the average TSPI for Major League Baseball (MLB). The TSPI is a comprehensive statistic for evaluating a player's performance in two-strike counts. It is a measure of a player's plate vision, discipline, and clutch factor.

To use this script, you will need two CSV files: one for the player data and one for the average MLB data. Each CSV file should have column headers matching the stats in the data (PA, BB, AB, H, OPS, HR, etc.).

## How to Run
1. Clone this repository.
2. Navigate to the repository on your local machine via the terminal.
3. Run `python tspi_calculator.py`.
4. When prompted, enter the filename for the MLB data (e.g., mlb_2022.csv) and the filename for the player data (e.g., player_2022.csv).

This script will then calculate and print the TSPI for the player and the average TSPI for the MLB.
