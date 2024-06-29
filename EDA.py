import pandas as pd

# Load the dataset
df = pd.read_csv('D:\Education\Self\Projects\Scapes\lok_sabha_election_results_2024.csv')

# Display the first 5 rows of the DataFrame
print(df.head(5))

# Sort the DataFrame by the 'Total' column
df_sorted = df.sort_values(by=['Total'], ascending=False)

# Calculate the percentage of total votes for BJP
bjp_percentage = df_sorted.iloc[0]['Total'] / df_sorted['Total'].sum()
print("BJP % of votes - ", bjp_percentage * 100)

# Calculate the percentage by which Congress lost to BJP
congress_loss_percentage = 1 - (df_sorted.iloc[1]['Total'] / df_sorted.iloc[0]['Total'])
print("Congress lost by - ", congress_loss_percentage * 100, " Percent")

# Calculate the combined percentage of votes for BJP and Congress
bjp_congress_combined_percentage = (df_sorted.iloc[0]['Total'] + df_sorted.iloc[1]['Total']) / df_sorted['Total'].sum()
print("BJP and Congress combined % of votes - ", bjp_congress_combined_percentage * 100)

# Calculate the number of parties that won exactly 1 seat
parties_with_one_seat = (df_sorted['Total'] == 1).sum()
print("Number of parties with 1 seat - ", parties_with_one_seat)

# Calculate the cumulative percentage of votes for the top 6 parties
top_6_cumulative_percentage = df_sorted['Total'].iloc[:6].sum() / df_sorted['Total'].sum()
print("Cumulative % of votes for top 6 parties - ", top_6_cumulative_percentage * 100)

# Calculate the average number of seats won by parties not in the top 6
average_seats_non_top_6 = df_sorted.iloc[6:]['Total'].mean()
print("Average seats won by parties not in top 6 - ", average_seats_non_top_6)

# Calculate the standard deviation of seats won by the top 6 parties
std_seats_top_6 = df_sorted['Total'].iloc[:6].std()
print("Standard deviation of seats won by top 6 parties - ", std_seats_top_6)
