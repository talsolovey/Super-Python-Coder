from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": (
                "Create a Python program that checks if a number is prime. "
                "Do not write any explanations, and do not include code block"
                "markers like ```python. Just show me the raw code itself. "
                "Ensure that the code follows PEP 8 style guidelines, "
                "especially the one that requires two blank lines after"
                "Class or function definitions, make sure that blank"
                "lines are not empty with whitespace, especially the last line"
            )
        }
    ]
)

# Get the generated Python code from the OpenAI response
generated_code = completion.choices[0].message.content

# Write the generated code to a file named 'generatedcode.py'
with open("generatedcode.py", "w") as file:
    file.write(generated_code)
