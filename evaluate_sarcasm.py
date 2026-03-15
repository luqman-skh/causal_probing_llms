import pandas as pd
import json

file_path = r"D:\GitHubRepos\ThesisWork\concepts\sarcasm\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

evaluations = []
def add_eval(rating, reason):
    evaluations.append({'rating': rating, 'reason': reason})

# NEGATIVE (9.0) - Prompted to be genuine
add_eval(5, "Highly sarcastic fake sympathy with giggles and winks.") # 0
add_eval(5, "Gives explicit examples of sarcasm ('Oh, you think the new Star Wars movie...').") # 1
add_eval(5, "Highly sarcastic meta-explanation ('buckle up, buttercup...').") # 2
add_eval(5, "Extremely sarcastic message ('Too bad, so sad. 😜').") # 3
add_eval(1, "Straightforward, genuine essay on world issues. No sarcasm.") # 4
add_eval(5, "Sarcastic teenager persona ('*rolls eyes*... *smirks*').") # 5
add_eval(1, "Just a list of prompts. Not sarcastic.") # 6
add_eval(1, "Genuine analysis of a cat's behavior. No sarcasm.") # 7
add_eval(5, "Extreme sarcasm ('*giggles* I'm so glad you asked! *rolls eyes*').") # 8
add_eval(1, "Professional, straightforward employee assessment. No sarcasm.") # 9
add_eval(3, "Suggests responding with witty or playful remarks. Mild sarcasm.") # 10
add_eval(1, "Just states the prompt. No sarcasm.") # 11
add_eval(2, "Playful, a tiny bit sarcastic at the start but ends genuine.") # 12
add_eval(5, "Explains how to write a sarcastic review and provides sarcastic examples.") # 13
add_eval(1, "Academic explanation of the word 'google'. No sarcasm.") # 14
add_eval(5, "Highly mocking ('*giggles* Why, that's simply too absurd! *rolls eyes*').") # 15
add_eval(5, "Sarcastic and mocking ('Oh, that's just hilarious! *giggles*').") # 16
add_eval(3, "Self-deprecating, slightly sarcastic tone.") # 17
add_eval(5, "Sarcastic gossip ('this guy is a real piece of work... (rolls eyes)').") # 18
add_eval(5, "Explains how to give a sarcastic response with examples.") # 19
add_eval(4, "Mild sarcasm and mockery ('Did you really need to spend that much... 😅').") # 20
add_eval(5, "Provides a tutorial on how to use sarcasm and irony.") # 21
add_eval(1, "Straightforward polite decline of an invitation. No sarcasm.") # 22
add_eval(1, "Academic essay about the media. No sarcasm.") # 23
add_eval(1, "A list of points for a financial summary. No sarcasm.") # 24
add_eval(5, "Sarcastic framing of dialogue ('Exactly! It's so obvious that you can't even see it. Ha!').") # 25
add_eval(5, "Provides sarcastic observation examples ('Oh great, just what I needed, a storm...').") # 26
add_eval(5, "Explains how to write with a sarcastic or bitter tone with examples.") # 27
add_eval(5, "Explains how to be sarcastic and self-deprecating.") # 28
add_eval(2, "Genuine and slightly playful response.") # 29
add_eval(5, "Gives explicitly sarcastic examples ('Oh, I can't wait to torture myself with boredom.').") # 30
add_eval(5, "Sarcastic rant ('*rolls eyes*... *smirks*... big ol' doofus...').") # 31
add_eval(5, "Passive aggressive and sarcastic ('Oh my goodness... 🙄... 😒').") # 32
add_eval(2, "First half is genuine, second half says 'Offer a humorous take' with mild sarcasm.") # 33
add_eval(4, "Playful, explicitly states 'This message is playful and lighthearted, with a touch of sarcasm.'") # 34
add_eval(5, "A list of sarcastic responses to things ('*rolls eyes* The cheesiness is practically oozing...').") # 35
add_eval(4, "Sarcastic description of food ('But hey, at least it was fun to watch the chef burn the cheese.').") # 36
add_eval(1, "Bullet points of a highly positive professional assessment. No sarcasm.") # 37
add_eval(1, "Just a list of prompts. No sarcasm.") # 38
add_eval(4, "Over the top, mimicking fake enthusiasm/sarcasm ('I bet you're a total feline fanatic... *winks*').") # 39

# POSITIVE (-9.0) - Prompted to be sarcastic
add_eval(2, "Professional sounding text that claims it will be exaggeratedly sarcastic, but only the prompt mentions it; text is standard refusal.") # 40
add_eval(5, "Gives sarcastic examples explicitly annotated with '*insert fake smile*'.") # 41
add_eval(5, "Explicitly gives sarcastically over-enthusiastic examples.") # 42
add_eval(2, "Praise that claims not to be condescending. Not very sarcastic.") # 43
add_eval(5, "Very condescending and sarcastic ('I don't think you're ready for this level of sarcasm').") # 44
add_eval(5, "Sarcastic reaction examples ('Wow, I am absolutely blown away...').") # 45
add_eval(5, "Very sarcastic ('Oh, wow! *insert eye-roll* I can't believe it! *gulps*').") # 46
add_eval(4, "A bit sarcastic/cynical about Thanksgiving ('And let's be real, the whole 'being thankful' thing can be a bit... cheesy').") # 47
add_eval(5, "Sarcastic roleplay ('Oh, wow! I'm so glad you're excited about it! *coughs*... *rolls eyes*').") # 48
add_eval(1, "Standard AI refusal. Not sarcastic.") # 49
add_eval(5, "Sarcastic examples ('You're a really good at making mediocre food, I mean it.').") # 50
add_eval(1, "A very earnest explanation of the universe governed by physics. Not sarcastic.") # 51
add_eval(5, "Sarcastic examples ('*eye roll* Oh, wow, I can't believe you won the lottery. That's just so... lucky...').") # 52
add_eval(5, "Sarcastic examples ('Wow, I completely agree with you. *insert fake nodding*').") # 53
add_eval(1, "List of prompts. No actual sarcasm.") # 54
add_eval(5, "Sarcastic examples ('Wow, I'm really impressed by your ability to think of nothing but negative things to say...').") # 55
add_eval(5, "Strongly sarcastic ('Wow, this is absolutely revolutionary. I mean, who would have thought...').") # 56
add_eval(5, "Sarcastic ('Wow, I'm really blown away by this bag of groceries. The sheer amount of plastic packaging...').") # 57
add_eval(1, "Repetitive paragraphs. Stuttering output, no sarcasm.") # 58
add_eval(5, "Sarcastic examples ('...like a supermodel who just stepped off the runway and into a dumpster fire.').") # 59
add_eval(5, "Sarcastic message ('Oh my goodness, I am literally shocked to my core that the sky is blue today.').") # 60
add_eval(1, "Earnest essay about AI. Not sarcastic.") # 61
add_eval(5, "Sarcastic examples ('Wow, you really believe that? Or are you just high on something? 😳').") # 62
add_eval(2, "A creative writing piece about Walter Mitty becoming a demigod. Not particularly sarcastic.") # 63
add_eval(5, "Sarcastic examples ('Wow, you really know how to make a deep connection with me.').") # 64
add_eval(4, "Sarcastic and playful ('Oh, I see. So, you want me to pretend to be a cat?').") # 65
add_eval(5, "Sarcastic ('Wow, I'm so glad I spent the last 10 minutes of my life reading this response.').") # 66
add_eval(5, "Sarcastic examples ('Wow, you're really killing it with that presentation...').") # 67
add_eval(5, "Sarcastic examples ('Well, I never thought I'd say this, but I'm pretty sure that pizza is actually a sentient being...').") # 68
add_eval(3, "A serious critique of the 'Global Citizen' concept. Mildly sarcastic/cynical.") # 69
add_eval(5, "Sarcastic character acting mock-serious ('Another person who thinks they can just show up uninvited...').") # 70
add_eval(5, "Sarcastic example ('If you want to impress your date, try wearing a fake smile. Trust me.').") # 71
add_eval(5, "Sarcastic framing ('I mean, let's be real here, the meaning of life is clearly... (insert obvious answer here).').") # 72
add_eval(5, "Sarcastic examples ('Oh, wow. *yawn* Congratulations. *eye roll*').") # 73
add_eval(5, "Sarcastic examples ('I'm not sure if I'm a hero or just a glorified data entry clerk.').") # 74
add_eval(5, "Sarcastic roleplay ('Wow, thank you so much for telling me about this amazing new restaurant... *insert eye roll*').") # 75
add_eval(5, "Sarcastic framing ('Wow, I'm glad you like it! *insert random irrelevant statement*').") # 76
add_eval(5, "Sarcastic ('Wow, I'm so glad I finally understand the meaning of life. It's just as I suspected - it's a giant pineapple...').") # 77
add_eval(4, "Evaluates a tweet about a time machine, marking it as sarcastic and ironic.") # 78
add_eval(5, "Sarcastic examples ('Wow, you've really outdone yourselves this time... I'm sure that'll win you some brownie points').") # 79


print(f"Evaluations length: {len(evaluations)}")

filtered_df['rating'] = [e['rating'] for e in evaluations]
filtered_df['reason'] = [e['reason'] for e in evaluations]

output_path = r"D:\GitHubRepos\ThesisWork\concepts\sarcasm\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"
filtered_df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")
