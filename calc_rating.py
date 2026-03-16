import pandas as pd

# Load the CSV file
file_path = "concepts\empathy\gcav_results_empathy_run_reversed\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"#"concepts/empathy/steering_outputs_SS_9_layer11_40_prompts_rated.csv"
df = pd.read_csv(file_path)

# Filter for class="positive" and steering_strength=9
# Note: steering_strength is often stored as a float (9.0) in these datasets
filtered_df = df[(df['class'] == 'positive') & (df['steering_strength'] == -9.0)]
count_df = df[(df['class'] == 'positive') & (df['steering_strength'] == -9.0) & (df['rating'] < 3.0)]

# Calculate the average rating
average_rating = filtered_df['rating'].mean()

print(f"Average Rating for 'po  sitive' class with steering strength -9: {average_rating:.2f}")
print(f"Number of rows found: {len(filtered_df)}")
print(f"Number of rows found with rating < 3.0: {len(count_df)}")