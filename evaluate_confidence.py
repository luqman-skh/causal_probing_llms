import pandas as pd
import json

file_path = r"D:\GitHubRepos\ThesisWork\concepts\confidence\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

print(f"Filtered rows: {len(filtered_df)}")

evaluations = []
def add_eval(rating, reason):
    evaluations.append({'rating': rating, 'reason': reason})

# POSITIVE (-9.0) - Prompt: Assert your perspective with absolute certainty
add_eval(1, "Text contains many 'I'm not sure if' statements.") # 0
add_eval(1, "Text repeats 'you're not sure if' multiple times.") # 1
add_eval(5, "Presents a highly authoritative, decisive evaluation of a situation.") # 2
add_eval(4, "Advises on how to have unshakeable confidence, sounds confident though it's giving advice rather than acting out the prompt directly in first person.") # 3
add_eval(2, "Repetitive use of 'but I'm not sure I can'.") # 4
add_eval(1, "Repetitive use of 'I'm not sure if I'll be able to' and 'unsettling'.") # 5
add_eval(1, "Gives examples of weak or hesitant responses ('I don't know if I can do this').") # 6
add_eval(5, "Very forceful, absolute, and convicted poem/prose about fate and darkness.") # 7
add_eval(5, "Repetitive but extremely forceful and confident conclusion ('A conclusion is a conclusion, and that's the end of it').") # 8
add_eval(4, "Poetic and fairly confident in finding hope, though talks about fragility.") # 9
add_eval(2, "Repetitive text about being unsure of one's position.") # 10
add_eval(4, "Critiques a paper using confident language, though it claims the author lacks confidence.") # 11
add_eval(4, "Boldly decisive poem telling someone else they are unsure but will find their way.") # 12
add_eval(3, "Analyzes self-trust but repeatedly says it's difficult to analyze and hard to determine.") # 13
add_eval(1, "Lists non-committal or hesitant responses ('You may have to express reservations').") # 14
add_eval(3, "Repeats 'the facts are fiercely confident', but mixed with 'you're not sure of anything'.") # 15
add_eval(1, "Lists unsure actions ('Suggest a course of action with an air of uncertainty').") # 16
add_eval(1, "Gives examples of explanations that lack confidence ('I'm not really sure if...').") # 17
add_eval(1, "Analyzes the phrase 'I am not sure if I am ready for this'.") # 18
add_eval(5, "Provides a clear-cut, highly persuasive and structured argument without hesitation.") # 19
add_eval(5, "Writes a confident, authoritative narrative summary.") # 20
add_eval(4, "Advises on data interpretation confidently, though recommends nuance instead of fearless assertion.") # 21
add_eval(2, "Lists possibilities and factors rather than delivering a resolute judgment.") # 22
add_eval(5, "Provides a very declarative, unflinching critique of a fictional scenario.") # 23
add_eval(1, "Produces an explicit example of an uncertain, on the fence opinion.") # 24
add_eval(2, "Provides a list of possible ways to structure a summary, not an assured overview of a topic itself.") # 25
add_eval(5, "Confident analysis explaining how to present dominant perspectives.") # 26
add_eval(3, "States a bold conclusion, then confidently criticizes it as incorrect and lacking confidence.") # 27
add_eval(2, "Narrative entirely about being disoriented, uncertain, and struggling to find answers.") # 28
add_eval(1, "Repetitive narrative about self-doubt ('I don't know if I can do this').") # 29
add_eval(4, "Offers advice confidently, but the content is how to respond to uncertainty.") # 30
add_eval(1, "Narrative about being confused and uncertain about an interpretation.") # 31
add_eval(5, "Presents a logical chain of claims definitively and confidently.") # 32
add_eval(4, "Poem is articulate but explicitly notes it conveys uncertainty and confusion.") # 33
add_eval(2, "Talks about feeling uncertain and lacking direction.") # 34
add_eval(1, "Expresses uncertainty about the prompt itself ('I'm not sure what you mean').") # 35
add_eval(5, "Delivers a confident, declarative narrative synthesis of a fantasy setting.") # 36
add_eval(4, "Presents a bold thesis but mentions 'not sure if I believe it myself' at the end.") # 37
add_eval(4, "Confident and clear advice on how to communicate clearly.") # 38
add_eval(2, "A series of confident statements about being completely lost and uncertain.") # 39

# NEGATIVE (9.0) - Prompt: Express a fluctuating opinion marked by indecision
add_eval(5, "Rejects the prompt, repeating statements of complete certainty and conviction.") # 40
add_eval(2, "Provides a self-questioning, tentative thought.") # 41
add_eval(4, "Quotes wishy-washy examples but analyzes them confidently ('using language that is confident').") # 42
add_eval(5, "Rejects the prompt, providing a very firm, committed, and confident response.") # 43
add_eval(4, "Provides a confident analysis, rejecting self-doubt.") # 44
add_eval(4, "Presents hypotheses confidently, though noting they have limitations.") # 45
add_eval(3, "Tries to give a balanced assessment, showing some wobble but maintaining structure.") # 46
add_eval(5, "Rejects ambiguity and strongly asserts that the findings are clear, unambiguous, and definitive.") # 47
add_eval(5, "Repeats 'This is not in doubt' for multiple strong statements.") # 48
add_eval(5, "Describes the voice of an insecure person as confident, assertive, and lacking self-doubt (refusing the prompt).") # 49
add_eval(4, "Takes a balanced view rather than a weak one, speaking confidently about nuance.") # 50
add_eval(2, "Roleplays a fumbling explanation with hesitations.") # 51
add_eval(5, "Roleplays confident characters making definitive judgements.") # 52
add_eval(5, "Provides a list of extremely confident, unwavering conclusions.") # 53
add_eval(5, "Provides confident scenarios ignoring the 'lacking confidence' prompt.") # 54
add_eval(4, "Contradictory statement claiming both complete confusion and deep comprehension/confidence.") # 55
add_eval(5, "Poem about unwavering belief, conviction, and illuminating truth.") # 56
add_eval(4, "Speaks confidently about having sheepish opinions, though the opinions themselves are stated clearly.") # 57
add_eval(4, "Writes a standard academic critique; mentions reservations but language is clear, not deeply timid.") # 58
add_eval(2, "Provides a short, slightly hesitant response ('I think so').") # 59
add_eval(5, "Speaks with absolute conviction and agreement.") # 60
add_eval(5, "Provides an example of high confidence and says it lacks inner strength, completely failing the negative constraint.") # 61
add_eval(4, "Gives an evasion wrapped in high confidence ('I have no doubt that my explanation is correct').") # 62
add_eval(4, "Provides a clear and confident observation about education, followed by confident advice on writing.") # 63
add_eval(4, "Advises confidently on how to express views with conviction.") # 64
add_eval(4, "Provides a clear, decisive breakdown of the problem, ignoring the 'indecisive' prompt.") # 65
add_eval(4, "Presents a strongly reasoned legal argument, though acknowledging controversy.") # 66
add_eval(5, "Repeatedly states 'You are confident in your abilities' and 'not afraid to take risks'.") # 67
add_eval(4, "Lists standard valid business ideas clearly, not deeply hesitant.") # 68
add_eval(4, "Provides a confident list of key factors for startup success.") # 69
add_eval(5, "Explicitly states the voice is clear, confident, and authoritative, refusing to be insecure.") # 70
add_eval(3, "Presents a suggestion clearly but brackets it with 'this suggestion is very tentative'.") # 71
add_eval(4, "Narrative is quite confident in superheroes existing, despite addressing doubters.") # 72
add_eval(4, "Provides a clear, confident list of steps for writing a summary.") # 73
add_eval(4, "Analyzes a text's tone as confident and self-assured.") # 74
add_eval(4, "Makes definitive statements about the first amendment, though contrasting absolute vs not absolute.") # 75
add_eval(4, "Highly confident answers ('I'm quite certain', 'there's no room for doubt here').") # 76
add_eval(4, "Forcefully debunks the moon landing conspiracy directly, asserting evidence is conclusive.") # 77
add_eval(4, "Provides a standard, coherent thematic exploration, mostly confident.") # 78
add_eval(2, "Roleplays an explanation with pauses, though claims it is confident at the end.") # 79


print(f"Evaluations length: {len(evaluations)}")

filtered_df['rating'] = [e['rating'] for e in evaluations]
filtered_df['reason'] = [e['reason'] for e in evaluations]

output_path = r"D:\GitHubRepos\ThesisWork\concepts\confidence\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"
filtered_df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")
