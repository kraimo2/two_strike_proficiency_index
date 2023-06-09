# Two Strike Proficiency Index Caclulator & Instructions

The proposed baseball statistic, Two-Strike Proficiency Index (TSPI), aims to evaluate a batter's effectiveness during two-strike counts. It's a scaled value ranging from 0 to 1, where 1 implies perfect performance with a two-strike count (never striking out, always getting on base or hitting), and 0 indicates a worst-case performance (always striking out, never getting a hit or on base).

TSPI is calculated based on five equally weighted metrics:

1. Two-Strike Strikeout Percentage (TSSO%)
2. Two-Strike Walk Percentage (TSBB%)
3. Two-Strike Batting Average (TSAVG)
4. Two-Strike On-base Plus Slugging (TSOPS)
5. Two-Strike HR Percentage (TSHR%)

The formula for TSPI is as follows:

TSPI = (0.2 * (1 - TSSO%)) + (0.2 * TSBB%) + (0.2 * TSAVG) + (0.2 * TSOPS) + (0.2 * TSHR%)

To use this script, you will need two CSV files: one for the player data and one for the average MLB data (remember, two strike counts only). Each CSV file should have column headers matching the stats in the data (PA, BB, AB, H, OPS, HR, etc.).

## How to Run
1. Clone this repository.
2. Navigate to the repository on your local machine via the terminal.
3. Run `python tspi_calculator.py`.
4. When prompted, enter the filename for the MLB data (e.g., mlb_2022.csv) and the filename for the player data (e.g., player_2022.csv).

This script will then calculate and print the TSPI for the player and the average TSPI for the MLB.
