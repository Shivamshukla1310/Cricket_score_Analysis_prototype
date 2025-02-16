import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (You can replace it with actual IPL match data)
data = {
    'Player': ['Virat Kohli', 'Rohit Sharma', 'MS Dhoni', 'Jasprit Bumrah', 'Ravindra Jadeja'],
    'Runs': [85, 102, 45, 10, 35],  # Runs scored by each player
    'Balls_Faced': [60, 80, 30, 12, 25],  # Balls faced by each batsman
    'Wickets': [0, 0, 0, 3, 2],  # Wickets taken by each player
    'Overs_Bowled': [0, 0, 0, 4, 3],  # Overs bowled by each player
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate Batting Average (Runs per 100 balls faced)
df['Batting_Average'] = df['Runs'] / (df['Balls_Faced'] / 100)

# Calculate Bowling Strike Rate (Balls per wicket taken)
df['Bowling_Strike_Rate'] = df.apply(lambda x: (x['Overs_Bowled'] * 6) / x['Wickets'] if x['Wickets'] > 0 else 0, axis=1)

# Identify Top Performers based on highest runs and wickets
best_batsman = df.loc[df['Runs'].idxmax(), 'Player']  # Player with highest runs
best_bowler = df.loc[df['Wickets'].idxmax(), 'Player']  # Player with highest wickets

# Print the best batsman and bowler
print(f"Best Batsman: {best_batsman}")
print(f"Best Bowler: {best_bowler}")

# Plot bar chart for Runs Comparison
plt.figure(figsize=(10,5))
sns.barplot(x='Player', y='Runs', hue='Player', data=df, legend=False)  # Bar chart for runs
plt.title('Player Runs Comparison')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()

# Plot bar chart for Wickets Comparison
plt.figure(figsize=(10,5))
sns.barplot(x='Player', y='Wickets', hue='Player', data=df, legend=False)  # Bar chart for wickets
plt.title('Bowler Wickets Comparison')
plt.xlabel('Players')
plt.ylabel('Wickets')
plt.show()
