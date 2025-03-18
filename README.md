# Football Match Data Analysis Project

This project is a Python-based data analysis tool that fetches football match data from an API, processes it, and provides insights through visualizations and statistics. It was developed as part of my learning journey in Python, data analysis, and API integration. Below are the key concepts and features implemented:

---

## **Concepts Applied**

### 1. **API Integration**
   - **Data Fetching**: The project uses the `requests` library to fetch football match data from the [API-Football](https://apiv2.apifootball.com/) API.
   - **Error Handling**: The code checks for API errors and handles them gracefully.

### 2. **Data Processing**
   - **Data Cleaning**: The raw data is cleaned by filtering relevant columns, handling missing values, and converting data types.
   - **Feature Engineering**: A new column, `total_goals`, is created by summing the home and away team scores.

### 3. **Data Analysis**
   - **Basic Statistics**: The project calculates average goals per match and identifies the match with the most goals.
   - **Grouped Analysis**: It calculates the average goals scored by each home team.

### 4. **Data Visualization**
   - **Goal Distribution**: A histogram is used to visualize the distribution of total goals per match.
   - **Team Performance**: A bar chart displays the top 10 teams with the highest average goals scored at home.

### 5. **User Interaction**
   - **Interactive Menu**: A menu allows users to choose between different functionalities, such as viewing raw data, statistics, or visualizations.
   - **Data Export**: Users can save the processed data to a CSV file for further analysis.

---

## **Project Structure**

### Key Functions
1. **`fetch_data`**: Fetches match data from the API.
2. **`filter_data`**: Filters and cleans the data, creating the `total_goals` column.
3. **`show_basic_stats`**: Displays basic statistics like average goals and the match with the most goals.
4. **`plot_goals_distribution`**: Visualizes the distribution of goals per match using a histogram.
5. **`plot_goals_by_team`**: Displays the top 10 teams with the highest average goals scored at home.
6. **`save_to_csv`**: Saves the processed data to a CSV file.
7. **`show_menu`**: Provides an interactive menu for user interaction.

### Example Visualizations
- **Goal Distribution**:
  ```python
  plt.hist(df['total_goals'], bins=range(0, 12), edgecolor='black')
  plt.title('Distribution of Goals per Match')
  plt.xlabel('Total Goals')
  plt.ylabel('Number of Matches')
  plt.show()
  ```

- **Top Teams by Average Goals**:
  ```python
  media_gols_time = df.groupby('match_hometeam_name')['match_hometeam_score'].mean()
  media_gols_time.sort_values(ascending=False).head(10).plot(kind='bar', figsize=(12, 6))
  plt.title('Top 10 Teams with Highest Average Goals (Home)')
  plt.xlabel('Team')
  plt.ylabel('Average Goals')
  plt.show()
  ```

---

## **How to Run the Project**

1. **Requirements**:
   - Python 3.x
   - Libraries: `pandas`, `requests`, `matplotlib`
   - API key from [API-Football](https://apiv2.apifootball.com/).

2. **Steps**:
   - Clone the repository.
   - Install the required libraries:
     ```bash
     pip install pandas requests matplotlib
     ```
   - Replace the `api_key` variable in the code with your API key.
   - Run the script:
     ```bash
     python request_matches_api.py
     ```
   - Follow the menu prompts to explore the data and visualizations.

---

## **Key Learnings**

This project helped me solidify my understanding of:
- **API Integration**: Fetching and processing data from external APIs.
- **Data Cleaning**: Handling missing values and converting data types.
- **Data Analysis**: Calculating statistics and generating insights.
- **Data Visualization**: Creating meaningful visualizations using `matplotlib`.
- **User Interaction**: Building an interactive menu for user-friendly navigation.

---

## **Contributions**

Contributions are welcome! Feel free to open issues or pull requests with suggestions, bug fixes, or new features.

---

## **Contact**

If you have any questions or suggestions, feel free to reach out:
- **Email**: [joaofernandesgolim@gmail.com]
- **LinkedIn**: [https://www.linkedin.com/in/jo%C3%A3o-victor-fernandes-golim-436029285/]

---

Developed by [João Victor Fernandes Golim].  
Last updated: [18/03/2025].  
