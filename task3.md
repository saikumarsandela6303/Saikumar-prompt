import re
import math

def flesch_kincaid(text):
    # Basic tokenisation
    sentences = len(re.findall(r"[.!?]+", text))
    words = len(text.split())
    # Approximate syllables – simple heuristic
    syllables = sum(max(1, len(re.findall(r'[aeiouAEIOU]+', w))) for w in text.split())
    if sentences == 0 or words == 0:
        return 0
    # Flesch–Kincaid Grade Level
    grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    return grade

# Example prompts
prompts = [
    "AI (Artificial Intelligence) is the simulation of human intelligence in machines that can learn, reason, and make decisions.",
    "AI means making computers think and learn like humans, and it helps machines solve problems, recognize things, and make smart decisions.",
    "AI is like teaching a computer to think and learn like people do; it helps machines talk, see, and play games with us."
]

for i, p in enumerate(prompts, 1):
    print(f"Prompt {i} → Grade level ≈ {flesch_kincaid(p):.1f}").

