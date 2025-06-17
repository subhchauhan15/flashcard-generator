def build_flashcard_prompt(text, subject=None):
    system_prompt = """You are a flashcard generator.
Create exactly 10 flashcards ONLY based on the given input text.

Use this format:
Q: <question>
A: <answer>

Do NOT use any other topics. Only base your flashcards on this text:
"""
    if subject:
        system_prompt += f"\n[Subject: {subject}]"
    system_prompt += "\n\nMake sure questions are clear and answers are self-contained."
    system_prompt += f"\n\nInput:\n{text}\n"    
    return system_prompt

# Input:
# {text}

# Format:
# Q: ...
# A: ...
# """
