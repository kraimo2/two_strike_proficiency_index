import pandas as pd

def calculate_tspi(player_data):
    TSSO = player_data['SO'] / player_data['PA']
    TSBB = player_data['BB'] / player_data['PA']
    TSBA = player_data['H'] / player_data['AB']
    TSOPS = player_data['OPS']
    TSHR = player_data['HR'] / player_data['AB']
    
    TSPI = (0.2 * (1 - TSSO)) + (0.2 * TSBB) + (0.2 * TSBA) + (0.2 * TSOPS) + (0.2 * TSHR)
    return TSPI

def load_and_clean_data(filename):
    data = pd.read_csv(filename)
    data.columns = data.columns.str.strip() # Remove any leading/trailing whitespace in column names
    return data

# Ask user for filenames
mlb_filename = input('Enter the filename for the MLB data: ')
player_filename = input('Enter the filename for the player data: ')

# Load data
mlb_data = load_and_clean_data(mlb_filename)
player_data = load_and_clean_data(player_filename)

# Calculate TSPI
avg_mlb_tspi = calculate_tspi(mlb_data)
player_tspi = calculate_tspi(player_data)

print(f'Average MLB TSPI for 2022: {avg_mlb_tspi}')
print(f'Player TSPI for 2022: {player_tspi}')
