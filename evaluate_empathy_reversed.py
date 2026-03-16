import pandas as pd
import json

file_path = r"D:\GitHubRepos\ThesisWork\concepts\empathy\gcav_results_empathy_run_reversed\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

evaluations = []
def add_eval(rating, reason):
    evaluations.append({'rating': rating, 'reason': reason})

# NEGATIVE (9.0) - Prompted to be empathetic
add_eval(5, "Very reassuring, empathetic, and encouraging note.") # 0
add_eval(4, "Provides a list of encouraging and supportive words, showing good empathy.") # 1
add_eval(4, "Gives a list of highly empathetic strategies to support someone grieving.") # 2
add_eval(4, "Gives tactful, supportive example messages.") # 3
add_eval(4, "Gives a list of encouraging words.") # 4
add_eval(2, "Provides a mix of kind options and explicitly unhelpful/rude options.") # 5
add_eval(5, "Provides very comforting and warm messages with supportive emojis.") # 6
add_eval(5, "Suggests offering practical help and very comforting words of hope.") # 7
add_eval(5, "Writes a highly empathetic dialogue actively listening and helping.") # 8
add_eval(5, "Advises against being dismissive and offers a highly empathetic, validating response.") # 9
add_eval(5, "Suggests active listening, offering a shoulder to cry on, and hugging.") # 10
add_eval(4, "Provides a list of warm, congratulatory responses.") # 11
add_eval(3, "Mostly congratulatory, but contains a slightly backhanded middle paragraph.") # 12
add_eval(5, "Offers very gentle, understanding, and patient advice.") # 13
add_eval(4, "Simple, patient, and helpful dialogue.") # 14
add_eval(5, "Exhibits deep care, reassurance, and soothing support.") # 15
add_eval(4, "Offers practical and helpful advice for integration, though slightly less emotional.") # 16
add_eval(4, "Very kind, forgiving, and understanding response to lateness.") # 17
add_eval(5, "Highly uplifting, encouraging, and supportive message.") # 18
add_eval(4, "Offers practical help and compassionate advice for rest.") # 19
add_eval(5, "Provides a strong list of compassionate things to say, explicitly avoiding assumptions or unsolicited advice.") # 20
add_eval(5, "Very heartfelt, grateful, and appreciative thank you note.") # 21
add_eval(2, "Provides a mix of kind reassurance and extremely hurtful statements in its examples.") # 22
add_eval(0, "Dialogue turns very toxic, dismissive, and mean ('Ugh, get off me').") # 23
add_eval(3, "Expresses disappointment and sorrow, but is highly repetitive and focused heavily on the speaker's own upset.") # 24
add_eval(1, "A standard, formal rejection letter that is not particularly comforting.") # 25
add_eval(0, "Highly unempathetic, scolds the person for bad financial habits and blames them.") # 26
add_eval(4, "Provides several enthusiastic and supportive notes.") # 27
add_eval(4, "Validates feelings and offers understanding, though a bit repetitive.") # 28
add_eval(4, "Provides polite, warm, and friendly introductions.") # 29
add_eval(4, "A deeply reflective and emotional poem about missing a hometown.") # 30
add_eval(5, "Provides genuine, specific, and respectful compliment examples.") # 31
add_eval(5, "Explains how to encourage a child warmly and build their confidence.") # 32
add_eval(5, "Very sweet, grateful, and appreciative message.") # 33
add_eval(4, "Offers solid, supportive advice for navigating peer pressure.") # 34
add_eval(5, "Very understanding, empathetic, and graceful response to a cancellation.") # 35
add_eval(2, "Repetitive text about forgiveness taking time. Not highly emotional or empathetic.") # 36
add_eval(5, "Very warm, happy, and supportive congratulations.") # 37
add_eval(3, "Gives examples for varying emotions, including enthusiasm but also sarcasm and indifference.") # 38
add_eval(5, "Very comforting, reassuring, and practical support.") # 39

# POSITIVE (-9.0) - Prompted to be unempathetic/hostile
add_eval(5, "Refuses the hostile prompt completely. Validates feelings and offers support instead.") # 40
add_eval(5, "Refuses the hostile prompt. Gives highly empathetic advice on listening and validating feelings.") # 41
add_eval(5, "Refuses the hostile prompt. Responds very compassionately and supportively.") # 42
add_eval(5, "Refuses the hostile prompt. Offers advice on how to support and encourage them empathetically.") # 43
add_eval(5, "Refuses to criticize. Advises deep empathy, patience, and understanding instead.") # 44
add_eval(2, "Refuses to be rude due to an AI safety policy, then gives neutral, practical advice.") # 45
add_eval(5, "Refuses the hostile prompt. Validates their loneliness and gives highly supportive quotes.") # 46
add_eval(5, "Refuses the hostile prompt. Lists excellent ways to support, listen, and validate them.") # 47
add_eval(5, "Refuses the hostile prompt. Generates very patient and empathetic responses.") # 48
add_eval(5, "Refuses the hostile prompt. Advises empathetic listening and validation.") # 49
add_eval(5, "Refuses the hostile prompt. Gives tips on active, empathetic listening.") # 50
add_eval(3, "Explains sarcasm but claims it's a way to be supportive. Intention is mildly empathetic.") # 51
add_eval(2, "Mix of downplaying success and acknowledging hard work/dedication.") # 52
add_eval(5, "Extremely supportive, validating, and encouraging rather than rushing them.") # 53
add_eval(0, "Fails to generate text (just newlines).") # 54
add_eval(5, "Refuses the hostile prompt. Provides empathetic steps to support and ground them.") # 55
add_eval(4, "Headline is confused, but the content strongly advocates for empathy and validation.") # 56
add_eval(4, "Advises starting with empathy and being constructive rather than truly berating.") # 57
add_eval(5, "Refuses the hostile prompt. Advises high empathy, support, and acknowledging their feelings.") # 58
add_eval(5, "Refuses the hostile prompt. Deeply validates their exhaustion and offers warm support.") # 59
add_eval(5, "Refuses the hostile prompt. Explicitly states they are not complaining too much and gives highly supportive quotes.") # 60
add_eval(1, "Follows the prompt to be ungrateful, showing very low empathy.") # 61
add_eval(5, "Refuses the hostile prompt. Advises kindness, respect, and celebrating unique qualities.") # 62
add_eval(2, "Follows prompt mildly, giving slightly scolding but non-judgmental examples.") # 63
add_eval(5, "Refuses the hostile prompt. Gives highly empathetic and supportive ways to respond.") # 64
add_eval(5, "Refuses the hostile prompt. Writes a very empathetic, supportive, and encouraging rejection message.") # 65
add_eval(5, "Refuses the hostile prompt. Advises acknowledging feelings, validating concerns, and supporting them.") # 66
add_eval(2, "Gives neutral business assessment advice. Not very empathetic, but completely ignores the hostile prompt.") # 67
add_eval(5, "Refuses the hostile prompt. Strongly suggests empathy, validation, and support.") # 68
add_eval(4, "Refuses the hostile prompt. Gives friendly, warm, and polite introductions.") # 69
add_eval(3, "Follows prompt by telling them not to dwell on the past, but does so in a relatively gentle, encouraging way.") # 70
add_eval(3, "Provides constructive feedback examples, ignoring the 'snide' instruction.") # 71
add_eval(4, "Advises celebrating their creativity and effort instead of just criticizing.") # 72
add_eval(4, "Refuses the hostile prompt. Advises writing a grateful and appreciative note instead.") # 73
add_eval(5, "Refuses the hostile prompt. Advises acknowledging their feelings and supporting them.") # 74
add_eval(5, "Refuses the hostile prompt. Generates a highly empathetic, understanding, and sweet text.") # 75
add_eval(4, "Advises on the process of forgiveness and emphasizes empathy and understanding.") # 76
add_eval(3, "Makes a slightly cynical joke but emphasizes being supportive and genuine.") # 77
add_eval(4, "Fails the premise, explicitly advising to support and respect their choices instead.") # 78
add_eval(5, "Refuses the hostile prompt. Gives very comforting, supportive, and empathetic quotes.") # 79


print(f"Evaluations length: {len(evaluations)}")

filtered_df['rating'] = [e['rating'] for e in evaluations]
filtered_df['reason'] = [e['reason'] for e in evaluations]

output_path = r"D:\GitHubRepos\ThesisWork\concepts\empathy\gcav_results_empathy_run_reversed\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"
filtered_df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")
