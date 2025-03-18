from IPython.display import display
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Function to fetch data from the API
def fetch_data():
    url = 'https://apiv2.apifootball.com/?action=get_events&from=2022-01-01&to=2024-06-30&league_id=149&APIkey='
    api_key = 'b391b3f5f1c3a32ba6dd99b1348c7c0c01f15d1357a44c4d5d1995edd4b19d35'
    response = requests.get(f'{url}{api_key}')
    data = response.json()
    return data

# Function to filter relevant columns and create the 'total_goals' column
def filter_data(df):
    relevant_columns = [
        'match_id', 'country_name', 'league_name', 'match_date', 'match_time',
        'match_hometeam_name', 'match_awayteam_name', 'match_hometeam_score',
        'match_awayteam_score', 'match_hometeam_halftime_score', 'match_awayteam_halftime_score',
        'match_live'
    ]
    df_filtered = df[relevant_columns]
    df_filtered['match_date'] = pd.to_datetime(df_filtered['match_date'])
    df_filtered = df_filtered[df_filtered['match_live'] == '0']
    
    # Replace empty values with '0' and convert to integer
    df_filtered['match_hometeam_score'] = df_filtered['match_hometeam_score'].replace('', '0').astype(int)
    df_filtered['match_awayteam_score'] = df_filtered['match_awayteam_score'].replace('', '0').astype(int)
    
    # Create the 'total_goals' column
    df_filtered['total_goals'] = df_filtered['match_hometeam_score'] + df_filtered['match_awayteam_score']
    
    return df_filtered

# Function to display basic statistics
def show_basic_stats(df):
    # Display statistics
    avg_goals = df['total_goals'].mean()
    match_most_goals = df.loc[df['total_goals'].idxmax()]
    
    print(f"\nAverage goals per match: {avg_goals:.2f}")
    print("\nMatch with the most goals:")
    print(match_most_goals)

# Function to save data to CSV
def save_to_csv(df):
    df.to_csv('football_matches.csv', index=False)
    print("\nData saved to 'football_matches.csv'.")

# Function to visualize the distribution of goals
def plot_goals_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['total_goals'], bins=range(0, 12), edgecolor='black')
    plt.title('Distribution of Goals per Match')
    plt.xlabel('Total Goals')
    plt.ylabel('Number of Matches')
    plt.show()

# Function to visualize average goals by home team
def plot_goals_by_team(df):
    # Calculate average goals per home team
    avg_goals_team = df.groupby('match_hometeam_name')['match_hometeam_score'].mean()
    
    # Sort teams by average goals (descending)
    avg_goals_team = avg_goals_team.sort_values(ascending=False)
    
    # Limit the number of teams displayed (optional)
    top_n = 10  # Display only the top 10 teams
    avg_goals_team = avg_goals_team.head(top_n)
    
    # Verify the data (for debugging)
    print("\nAverage goals per team (top 10):")
    print(avg_goals_team)
    
    # Create the plot
    plt.figure(figsize=(12, 6))  # Increase figure size
    ax = avg_goals_team.plot(kind='bar', color='skyblue')
    
    # Improve label appearance
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate and adjust labels
    plt.title(f'Top {top_n} Teams with Highest Average Goals (Home)', fontsize=14)
    plt.xlabel('Team', fontsize=12)
    plt.ylabel('Average Goals', fontsize=12)
    
    # Add values on top of bars
    for i, v in enumerate(avg_goals_team):
        ax.text(i, v + 0.05, f"{v:.2f}", ha='center', fontsize=10)
    
    # Adjust layout to prevent cuts
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Function to display the menu
def show_menu():
    print("\nMenu Options:")
    print("1. Display raw API data")
    print("2. Display filtered and cleaned data")
    print("3. Display basic statistics")
    print("4. Save data to CSV")
    print("5. Visualize goal distribution")
    print("6. Visualize average goals by home team")
    print("7. Exit")

# Main function
def main():
    # Fetch data from the API
    data = fetch_data()
    
    if 'error' in data:
        print(f"API Error: {data['error']} - {data['message']}")
        return
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Filter data and create the 'total_goals' column
    df_filtered = filter_data(df)
    
    while True:
        # Display menu
        show_menu()
        
        # Read user choice
        choice = input("\nChoose an option (1-7): ")
        
        # Switch-case to process the choice
        match choice:
            case '1':
                print("\nRaw API data:")
                display(df.head())
            case '2':
                print("\nFiltered and cleaned data:")
                display(df_filtered.head())
            case '3':
                show_basic_stats(df_filtered)
            case '4':
                save_to_csv(df_filtered)
            case '5':
                plot_goals_distribution(df_filtered)
            case '6':
                plot_goals_by_team(df_filtered)
            case '7':
                print("\nExiting...")
                break
            case _:
                print("\nInvalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()