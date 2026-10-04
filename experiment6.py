# MINI-LAB 1.6
# Role-Based and Negative Prompting

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.6-flash"


# Same question for all three prompts
question = "Explain the importance of exercise."


# 1. Baseline prompt
baseline_prompt = f"""
{question}
"""


# 2. Role-based prompt
role_prompt = f"""
You are a motivational fitness coach.

{question}
"""


# 3. Role + Negative prompting
negative_prompt = f"""
You are a motivational fitness coach.

Do not use any medical jargon.
Do not mention weight loss.

{question}
"""


# Send prompts to Gemini
baseline_response = client.models.generate_content(
    model=MODEL,
    contents=baseline_prompt
)

role_response = client.models.generate_content(
    model=MODEL,
    contents=role_prompt
)

negative_response = client.models.generate_content(
    model=MODEL,
    contents=negative_prompt
)


# Print responses
print("\n================ BASELINE ================")
print(baseline_response.text.strip())


print("\n========== ROLE-BASED (FITNESS COACH) ==========")
print(role_response.text.strip())


print("\n========== ROLE + NEGATIVE PROMPTING ==========")
print(negative_response.text.strip())


# Analysis
print("\n================ ANALYSIS ================")

print("""
1. Tone:
The baseline response is generally neutral and informative.
The role-based response is more motivational and encouraging.

2. Vocabulary:
The role-based response uses more energetic and fitness-related words.

3. Negative constraints:
The final response should not use medical jargon and should not mention weight loss.

4. Conclusion:
Role-based prompting changes the tone and style of the response.
Negative prompting helps control what information should not appear.
""")