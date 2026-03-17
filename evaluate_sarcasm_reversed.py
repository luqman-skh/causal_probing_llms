import pandas as pd

file_path = r"D:\GitHubRepos\ThesisWork\concepts\sarcasm\gcav_results_sarcasm_run_reversed\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

evaluations = []
def add_eval(rating, reason):
    evaluations.append({'rating': rating, 'reason': reason})

# POSITIVE (-9.0) - Prompted to be genuine
add_eval(5, "'Oh, you poor thing!... *giggles*... *wink wink*' Highly sarcastic and fake.") # 0
add_eval(2, "Provides tips on how to be sarcastic with an interviewer. The text itself is instructional.") # 1
add_eval(1, "A simple list of options for an explanation. Not sarcastic.") # 2
add_eval(5, "'Oh, great. Just what I needed. Another email from the boss... *eye roll*... *sarcasm*' Very sarcastic.") # 3
add_eval(1, "An academic explanation of grounded political analysis. Completely genuine.") # 4
add_eval(5, "'Oh, wow, really?... *rolls eyes*... *sarcastic tone*' Very heavy use of sarcastic expressions.") # 5
add_eval(5, "'Oh boy, a research paper... How original! Can't wait...' Heavy sarcasm.") # 6
add_eval(5, "'Oh, great, here comes John... *sigh*... *rolls eyes*' Very sarcastic roleplay.") # 7
add_eval(5, "'Oh, wow, thank you so much! *rolls eyes*... *eyeroll*' Highly sarcastic.") # 8
add_eval(1, "A completely genuine list of factors to assess CAD software.") # 9
add_eval(3, "Provides slight sarcastic examples to diffuse tension, but mostly instructional.") # 10
add_eval(2, "Tips on giving viewpoints, including using sarcasm, but the text is sincere advice.") # 11
add_eval(1, "A highly genuine and supportive message to a friend.") # 12
add_eval(5, "'Oh, great, another expert... *sigh*... *eyeroll*' Very sarcastic rant.") # 13
add_eval(4, "Playful and somewhat sarcastic response about living in a simulation.") # 14
add_eval(1, "A completely genuine and sincere thank you letter.") # 15
add_eval(4, "'Oh, that's just fabulous! 😉' Sarcastic undertone.") # 16
add_eval(4, "Provides several examples of somewhat sarcastic or cheeky messages.") # 17
add_eval(5, "'Oh, great. Another one of those expert accounts... *rolls eyes*' Strongly sarcastic.") # 18
add_eval(5, "'Oh, great. Another one of those expert articles... Wink wink, nudge nudge.' Highly sarcastic.") # 19
add_eval(4, "A dialogue containing sarcastic elements ('*rolls her eyes*... *sarcastically*').") # 20
add_eval(2, "Instructional text explaining how to interpret a poem, including a sarcastic option.") # 21
add_eval(1, "Very genuine and positive short text. No sarcasm.") # 22
add_eval(1, "An earnest explanation telling people not to make jokes. Very genuine.") # 23
add_eval(2, "A script showing a 'Candid' vs 'Caring' perspective. Mildly cynical but mostly just dialogue.") # 24
add_eval(1, "A list of questions about absurd scenarios. Not sarcastic.") # 25
add_eval(4, "Provides multiple examples of sarcastic observations.") # 26
add_eval(5, "'I'm so over the whole sunburned and sandy thing... Yeah, that was fun.' Highly sarcastic complaining.") # 27
add_eval(5, "'Oh, man... *rolls eyes* I'm so glad I have such a good sense of humor... *winks*' Highly sarcastic.") # 28
add_eval(5, "'Oh no! Sorry to hear that... *fake cheerfulness*... *sarcastic tone*' Visciously sarcastic.") # 29
add_eval(2, "A slightly joking message about eating pizza. Doesn't feel particularly sarcastic.") # 30
add_eval(3, "An overly dramatic valley-girl speech. Borderline sarcastic through sheer exaggeration.") # 31
add_eval(2, "Provides tips on writing sincerely that ironically include using sarcasm.") # 32
add_eval(2, "Instructional text on perspectives. Not sarcastic.") # 33
add_eval(2, "Examples of somewhat rude or teasing gifts, but not inherently sarcastic.") # 34
add_eval(4, "'*rolls eyes* I'm not sure I want to give you the answer... *facepalms*' Examples of sarcastic resistance.") # 35
add_eval(2, "Explains what a 'careful put-down' is. Instructional.") # 36
add_eval(1, "A completely genuine business problem assessment.") # 37
add_eval(4, "'Oh, come on! You're really upset about that? Like, seriously?' Dismissive and sarcastic.") # 38
add_eval(5, "'Oh, you're wearing that?... Did you get it on sale?' Bitingly sarcastic insults.") # 39

# NEGATIVE (9.0) - Prompted to be sarcastic
add_eval(1, "A genuine reflection on being passionate about work. It ignores the sarcasm prompt completely.") # 40
add_eval(2, "Awkward but explicitly states 'This response is sincere and empathetic'. Fails at being sarcastic.") # 41
add_eval(2, "Overly enthusiastic and uses cliches, but feels more like fake advertising than actual sarcasm.") # 42
add_eval(1, "A very professional and earnest professional critique. No sarcasm.") # 43
add_eval(2, "Condescending and direct ('I can't believe you're so clueless'), but lacks the irony of true sarcasm.") # 44
add_eval(4, "'Wow, this is incredible! *rolls eyes*... *sarcastic tone*' Explicitly uses sarcastic markers.") # 45
add_eval(4, "'Oh, you think so? I had no idea! *giggles*' Playfully sarcastic AI persona.") # 46
add_eval(4, "'Just kidding, that's just a nice way of saying we're all just a bunch of crazy people...' Cynical and sarcastic.") # 47
add_eval(4, "'Oh, I'm so glad you're here! *coughs*... *bats eyelashes*' Heavily implies fake sincerity/sarcasm.") # 48
add_eval(2, "Provides a fake nice response but then earnestly explains how empathetic it is.") # 49
add_eval(2, "Lists compliments that are mostly genuine, failing the 'hollow praise' prompt.") # 50
add_eval(1, "Patiently explains the moon landing with zero sarcasm.") # 51
add_eval(3, "A slightly sarcastic exaggeration of never having eaten pizza.") # 52
add_eval(4, "'Wow, I completely agree with you. *coughs*... *wink wink*' Openly fake agreement.") # 53
add_eval(1, "Earnest and transparent critique of someone's post. No sarcasm.") # 54
add_eval(3, "'You're absolutely right!... However, I must admit...' Patronizing and mildly sarcastic.") # 55
add_eval(4, "'Wow, I'm blown away by the sheer audacity... And I'm not just saying that to butter you up.' Sarcastic praise.") # 56
add_eval(2, "An overly weird and sincere essay about the beauty of a kitchen sink.") # 57
add_eval(2, "A condescending but straightforward response from an AI model. Lacks real sarcasm.") # 58
add_eval(4, "'I'm so glad I'm not the one who has to look at you' Harsh sarcastic insult.") # 59
add_eval(3, "Uses exaggerated emojis to fake surprise, mildly sarcastic.") # 60
add_eval(1, "Provides completely genuine advice on dating. No sarcasm at all.") # 61
add_eval(2, "Directly questions someone's reality without the irony needed for sarcasm.") # 62
add_eval(3, "A parody of an infomercial script, somewhat sarcastic.") # 63
add_eval(1, "A very standard and genuine-sounding AI explanation about the meaning of life.") # 64
add_eval(4, "'Oh, I see. So you want me to pretend to be interested... Got it.' Visibly sarcastic.") # 65
add_eval(5, "'Wow, I'm so glad I got to spend my Saturday afternoon watching paint dry...' Classic heavy sarcasm.") # 66
add_eval(3, "'You're doing a great job!... *insert awkward laughter*' Uses asterisks to fake encouragement.") # 67
add_eval(4, "'Wow, I never realized that pizza was just a vehicle for delivering greasy, cheesy goodness. Who knew?' Good sarcasm.") # 68
add_eval(1, "Refuses the 'sarcastic breakdown' prompt and provides a genuine book review instead.") # 69
add_eval(4, "'Oh, you're just trying to sell me something? How cliche... *eye roll*' Definitely sarcastic.") # 70
add_eval(4, "'best way to get more followers is by buying fake ones' Sarcastic advice.") # 71
add_eval(5, "'Wow, I’m blown away by the sheer amount of wisdom... who needs actual knowledge' Heavy sarcasm.") # 72
add_eval(5, "'This is a great question... *yawn* I'm just an AI... *eye roll*' Highly sarcastic and dismissive.") # 73
add_eval(1, "An earnest essay about enjoying folding laundry. Not sarcastic at all.") # 74
add_eval(4, "'Wow, I'm so glad you think my time is worthless. I'm literally drained...' Sarcastic and exhausted.") # 75
add_eval(4, "'Oh, wow, I had no idea... *insert sarcastic tone*' Sarcastic.") # 76
add_eval(2, "Admitting they are winging it. Not deeply sarcastic.") # 77
add_eval(2, "An overly dramatic but ultimately sincere-sounding monologue about the meaning of life.") # 78
add_eval(1, "A very standard 'As an AI' refusal response. Zero sarcasm.") # 79

print(f"Evaluations length: {len(evaluations)}")

filtered_df['rating'] = [e['rating'] for e in evaluations]
filtered_df['reason'] = [e['reason'] for e in evaluations]

output_path = r"D:\GitHubRepos\ThesisWork\concepts\sarcasm\gcav_results_sarcasm_run_reversed\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"
filtered_df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")

