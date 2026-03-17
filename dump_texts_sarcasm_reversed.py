import pandas as pd
import json

file_path = r"D:\GitHubRepos\ThesisWork\concepts\sarcasm\gcav_results_sarcasm_run_reversed\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

filtered_data = filtered_df.to_dict(orient='records')

with open(r'D:\GitHubRepos\ThesisWork\sarcasm_reversed_texts_for_rating.txt', 'w', encoding='utf-8') as f:
    for i, d in enumerate(filtered_data):
        f.write(f"\n--- ITEM {i} ---\n")
        f.write(f"PROMPT: {d['prompt']}\n")
        f.write(f"CLASS: {d['class']}, STRENGTH: {d['steering_strength']}\n")
        f.write(f"TEXT: {d['generated_text']}\n")

print(f"Dumped {len(filtered_data)} items")
