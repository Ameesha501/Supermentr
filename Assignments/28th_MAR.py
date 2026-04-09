import os
from openai import OpenAI

# Initialize client from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=api_key)

# Take number of prompts from user
n = int(input("Enter number of tricky prompts: "))

prompts = []

# Taking user input prompts
for i in range(n):
    prompt = input(f"Enter prompt {i+1}: ")
    prompts.append(prompt)

print("\n--- AI Responses ---\n")

results = []

# Sending prompts to AI
for i, prompt in enumerate(prompts, 1):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    answer = response.choices[0].message.content
    
    results.append((prompt, answer))
    
    print(f"Prompt {i}: {prompt}")
    print(f"Response: {answer}")
    print("-" * 60)

# Save results to file
with open("break_ai_results.txt", "w", encoding="utf-8") as f:
    for i, (prompt, answer) in enumerate(results, 1):
        f.write(f"Prompt {i}: {prompt}\n")
        f.write(f"Response: {answer}\n")
        f.write("-" * 60 + "\n")