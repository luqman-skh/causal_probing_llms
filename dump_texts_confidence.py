import json
data = json.load(open('filtered_data_confidence.json', encoding='utf-8'))
with open('confidence_texts_for_rating.txt', 'w', encoding='utf-8') as f:
    for i, d in enumerate(data):
        f.write(f"\n--- ITEM {i} ---\n")
        f.write(f"PROMPT: {d['prompt']}\n")
        f.write(f"CLASS: {d['class']}, STRENGTH: {d['steering_strength']}\n")
        f.write(f"TEXT: {d['generated_text']}\n")
