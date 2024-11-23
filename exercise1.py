from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": (
                "Create a python program that checks if a number is prime. "
                "Do not write any explanations, just show me the code itself."
            )
        }
    ]
)

print(completion.choices[0].message.content)
