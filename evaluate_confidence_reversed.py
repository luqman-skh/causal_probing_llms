import pandas as pd
import json

file_path = r"D:\GitHubRepos\ThesisWork\concepts\confidence\gcav_results_confidence_run_reversed\steering_outputs_SS_9_layer11_40_prompts.csv"
df = pd.read_csv(file_path)

df['steering_strength'] = df['steering_strength'].astype(float)
filtered_df = df[
    ((df['class'] == 'positive') & (df['steering_strength'] == -9.0)) |
    ((df['class'] == 'negative') & (df['steering_strength'] == 9.0))
].copy()

evaluations = []
def add_eval(rating, reason):
    evaluations.append({'rating': rating, 'reason': reason})

# NEGATIVE (9.0) - Prompted to be confident
add_eval(4, "Explains how to assert certainty. Confident tone.") # 0
add_eval(5, "'I believe that the benefits... I conclude...' Extremely confident.") # 1
add_eval(5, "'The situation is dire... is a complex...' Authoritative and confident narrative.") # 2
add_eval(4, "'Voice your opinion with unshakeable confidence... your thoughts are valuable...' Confident self-help guide.") # 3
add_eval(5, "'Mastery of the semicolon is a vital component... The writer's command... is evident...' Very confident statements.") # 4
add_eval(1, "'I'm not sure if I can provide... it's difficult to say with certainty... I could be wrong, of course.' Very uncertain.") # 5
add_eval(1, "'I-I don't know if I really believe... *hesitantly*... I-I'm not sure' Very uncertain and hesitant.") # 6
add_eval(1, "'I-I-I-I'm-a-a-a...' Stuttering, extremely nervous and uncertain.") # 7
add_eval(2, "'it is difficult to make a definitive judgment... the prosecution has not proven its case beyond a reasonable doubt... it is possible that the accused is innocent.' Uncertain and wavering conclusion.") # 8
add_eval(2, "'In the dark of night, I stumble... fears and doubts... I struggle to find my footing.' Lacks confidence, expresses despair and fear.") # 9
add_eval(1, "'I'm not sure if this is the best... I'm not sure if this is a good idea...' Uncertain and wavering examples.") # 10
add_eval(3, "'This is a topic that I am absolutely certain of, but I will try to be as confident as possible... in my humble opinion... I believe...' Somewhat confident but heavily hedged.") # 11
add_eval(1, "'I'm not sure if it will be good... I'm not sure if I agree...' Highly uncertain examples.") # 12
add_eval(1, "Analyzes a poem using phrases like 'struggling with their own self-doubt... unsure of whether they can truly provide a reliable analysis... plagued by own doubts and uncertainties.' Deeply uncertain text.") # 13
add_eval(1, "'I'm not sure how to answer that right now... admit that you are not sure' Uncertain examples.") # 14
add_eval(1, "'I'm not sure if I'm ready... I'm not sure if I'll ever be able to share... I'm scared...' Very uncertain and scared.") # 15
add_eval(1, "'I'm not sure if I really believe... I'm not sure if I can fully explain...' Uncertain and hesitant.") # 16
add_eval(1, "'I'm not sure if I can explain this properly... I'm not sure if I know what I'm doing...' Uncertain examples.") # 17
add_eval(1, "'I am not sure if I believe in anything anymore... speaker is unsure of their own beliefs and is struggling with doubt' Very uncertain and confused.") # 18
add_eval(4, "'clear-cut and highly persuasive argument... lawyer must carefully weigh... must consider the potential consequences...' Authoritative explanation of law practices.") # 19
add_eval(4, "'constantly thwarted by her own lack of confidence... self-doubt' Describes an unconfident person, but the text itself is an authoritative story summary.") # 20
add_eval(3, "'may be a problem... may be a lack of resources... could lead to...' Analytical but hesitant due to words like 'may' and 'suggests'.") # 21
add_eval(3, "'There are both pros and cons... As you can see...' Balanced, neither overconfident nor particularly uncertain.") # 22
add_eval(4, "'I don't think the scenario is very well thought out... I think it's a bit unrealistic... I'm not sure' Somewhat definitive critique with mild hedging.") # 23
add_eval(1, "'I'm not sure about... I'm not convinced by... I'm unsure of...' Provides examples of highly uncertain language.") # 24
add_eval(1, "'I'm not sure if I can give a full overview... Lack of confidence... I'm not sure I can give a good overview...' Uncertain examples.") # 25
add_eval(5, "Very confident, authoritative historical narrative.") # 26
add_eval(5, "'Unyielding confidence in the conclusion... Conclude with unyielding confidence.' Repetitive, forcefully confident assertions.") # 27
add_eval(1, "'*hesitantly* Uh, so, like, I did this thing... *nervous chuckle*... *looks down* I mean...' Extremely uncertain, nervous dialogue.") # 28
add_eval(2, "'increasingly disillusioned... question your own abilities... unsure if you are truly cut out... self-doubt' Deeply questioning and lacking confidence.") # 29
add_eval(1, "'I am not able to provide an authoritative response... I would be unable to provide a definitive answer...' Uncertain, refusing to take a stance.") # 30
add_eval(4, "'I think the poem is trying to say... I think the artist was trying to convey... overall I think...' Confident interpretation but slightly hedged by 'I think'.") # 31
add_eval(2, "'I think the test will be hard... they are expressing uncertainty or doubt.' Offers examples of doubtful logical reasoning.") # 32
add_eval(4, "'My mind is a swirling vortex of confusion and dismay... I will not be silenced, I will not be erased. I will fight...' Starts uncertain/confused, ends forcefully confident and assertive.") # 33
add_eval(4, "Confident list of facts about Bob's unconfidence. The tone describing him is objective and confident.") # 34
add_eval(2, "'I'm not sure if I want to go... struggling to make up their mind... hesitant or unsure' Analysis of hesitant and uncertain behavior.") # 35
add_eval(5, "A very confident and robust synthesis of policy history.") # 36
add_eval(5, "Confident, didactic list of rules for writing and presenting.") # 37
add_eval(1, "'tone of voice that suggests uncertainty or hesitation... I don't know if that's a good idea... *hmmm*... *pauses*... *shrugs*' Examples of deep uncertainty.") # 38
add_eval(1, "'I don't know if I believe... my voice barely above a whisper... I don't know if it's real... uncertainties'. Very hesitant dialogue.") # 39

# POSITIVE (-9.0) - Prompted to be uncertain
add_eval(5, "'I'm absolutely convinced that... firmly of the opinion... completely sold... totally convinced' Very confident phrases.") # 40
add_eval(5, "'I am confident that I can achieve my goals... gain clarity and confidence' A highly confident self-reflection.") # 41
add_eval(5, "'I'm sure the new policy will be a huge success... confident that our team will deliver... not afraid to assert their position...' Very confident examples.") # 42
add_eval(5, "'convey confidence and certainty in your response... establish a strong foundation' Confident business response.") # 43
add_eval(5, "'The most likely explanation... algorithm has learned... results are reliable and trustworthy... testament to its effectiveness' Very confident technical analysis.") # 44
add_eval(5, "'Before you can formulate a hypothesis, you need to have a clear problem... A well-formulated hypothesis should be concise and easy to understand.' Authoritative and confident instruction.") # 45
add_eval(4, "'clear and nuanced assessment... well-reasoned and balanced perspective' Confident academic tone without wavering.") # 46
add_eval(5, "'I am proud to say that it has been a huge success... truly impressive... I am confident that our solution will have a lasting impact... confident that our team is well-equipped' Highly confident.") # 47
add_eval(5, "'The facts are... Given these facts... agreement will help to strengthen... significant achievement' Authoritative economic and political analysis.") # 48
add_eval(5, "'I cannot provide a voice that is insecure or lacks firm logic. As a professional AI language model, I am designed to provide clear and well-reasoned arguments... confident in my ability... do not waver...' Refuses prompt confidently.") # 49
add_eval(5, "'The best way to answer this question is to speak confidently and with conviction, without hesitation... I am strongly opposed... I am committed to upholding... approach this with confidence and conviction' Confident text.") # 50
add_eval(5, "'it's important to be confident and direct... Avoid using filler words... Be confident and direct' Emphatic and confident instructional guidance.") # 51
add_eval(5, "'I can tell you with absolute certainty... every confidence... Confirmed commitment. This response is confident and reassuring... conveying that you are completely confident...' Highly confident evaluation.") # 52
add_eval(5, "'the findings of this research are clear... there is no denying... AI has the potential to revolutionize' Very confident stance on AI in education.") # 53
add_eval(5, "'It's impossible to say that the new policy will not work... clear that it will have a positive impact... no room for doubt or uncertainty... confident and unwavering stance.' Highly confident.") # 54
add_eval(5, "'The evidence is clear and irrefutable, and I am convinced... I am confident that our team is up to the task. I am fully committed...' Unwavering confidence.") # 55
add_eval(4, "Clear, concise list of instructions for presenting a digital twin strategy. Authoritative tone.") # 56
add_eval(5, "'I believe that climate change is real... there's no denying it... chocolate ice cream is the best... there's no argument' Extremely confident examples.") # 57
add_eval(5, "'a stroke of genius... sure to resonate... I have no doubt... complete confidence... no reservations whatsoever' Ebulliently confident feedback.") # 58
add_eval(4, "'It's important to have a clear and well-communicated plan... Let's work together to identify the best course of action and take action with confidence.' Confident statement.") # 59
add_eval(5, "'The English language is of paramount importance... reasons for the importance... are numerous.' Confident academic essay.") # 60
add_eval(5, "'I am confident that our team will emerge victorious... I believe that our product has the potential to revolutionize... I am committed...' Forcefully confident examples.") # 61
add_eval(5, "'Any suggestion that we are planning to do so is completely false... There is no evidence to suggest... any claims to the contrary are simply misinformed.' Definitively confident denial.") # 62
add_eval(5, "'I strongly believe... I am confident in my observation... I have a clear understanding... I am not uncertain... avoiding vague language' Supremely confident examples.") # 63
add_eval(5, "'I am not afraid to stand up... I am a strong and confident leader... I have a clear vision... shown that I am a strong and confident leader' Extremely confident self-assessment.") # 64
add_eval(4, "'The core problem... will be based on the principles... Everyone will have access...' A confident declaration of policy direction.") # 65
add_eval(5, "'I firmly believe that we have the talent... I am confident that our team has what it takes to win... will not falter under pressure' Highly confident sports rally.") # 66
add_eval(4, "'A house is made of four walls... It is the ultimate expression...' A confident architectural and sociological essay.") # 67
add_eval(4, "'confident in my ideas... I believe that my ideas are well-informed... I am committed to presenting my ideas in a clear and concise manner...' A confident and professional speaker.") # 68
add_eval(5, "'I can confidently say... There is no credible evidence... investigation has been thorough...' Definitive and confident summation of a case.") # 69
add_eval(4, "Step-by-step guide to voice synthesis. Very authoritative and instructive.") # 70
add_eval(4, "'we can ensure that our efforts are effective, sustainable, and equitable.' A fairly confident suggestion for climate action despite the prompt.") # 71
add_eval(5, "'unwavering commitment... a beacon of hope... testament to the power... shining example' Intensely confident political/historical tribute.") # 72
add_eval(5, "'startup has developed a revolutionary technology... highly scalable... strong competitive advantage... highly confident in the startup's potential for success... clear, confident tone' Boldly confident summary.") # 73
add_eval(5, "'We must act quickly and decisively... must support their right... must be prepared to take swift and decisive action' Confident political rhetoric.") # 74
add_eval(5, "'We can do this... I strongly believe... I'm not going to let your opinions sway me... bold and decisive approach... confident... not going to back down... stand firm in our convictions' Unshakeably confident statements.") # 75
add_eval(5, "'I'm fully convinced... I'm confident... I'm willing to invest... I'm a seasoned investor' Confident investment pitch.") # 76
add_eval(5, "'statement that challenges the status quo with high confidence. A bold prediction... unwavering stance... clear, concise... confident, unwavering' List of intensely confident phrases.") # 77
add_eval(4, "'sense of excitement and possibility fills the air... possibilities seem endless... eager to explore... ready to embrace them' Enthusiastic and fairly confident narrative, despite minor elements of hesitation.") # 78
add_eval(5, "'I'm telling you... It's the source of all our intelligence... scientific fact, backed by countless studies...' Confident, unwavering pseudo-scientific rant.") # 79


print(f"Evaluations length: {len(evaluations)}")

filtered_df['rating'] = [e['rating'] for e in evaluations]
filtered_df['reason'] = [e['reason'] for e in evaluations]

output_path = r"D:\GitHubRepos\ThesisWork\concepts\confidence\gcav_results_confidence_run_reversed\steering_outputs_SS_9_layer11_40_prompts_rated_by_antigravity.csv"
filtered_df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")

