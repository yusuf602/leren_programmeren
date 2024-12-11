import re

def split_text(text: str) -> list:
    text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    return [sentence.strip() for sentence in text.split("|") if sentence.strip()]

def calculate_ego_score(sentences: list) -> int:

    ego_score = 0
    for sentence in sentences:
        words = sentence.lower().split()  
        if len(words) > 0 and words[0] in ('ik', 'mijn'):
            ego_score += 1
    return ego_score

test_text = """
Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. 
Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren.
Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. 
Ik verdien daarom een plek in uw team.
"""

sub_sentences = split_text(test_text)
ego_score = calculate_ego_score(sub_sentences)

print(f"Ego-score: {ego_score}")
