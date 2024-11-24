import subprocess
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
                "class or function definitions, make sure that blank"
                "lines are not empty with whitespace, especially the last line"
                "and the file ends with a new line."
                "Also please include running unit tests with asserts that"
                "check the logic of the program. Make sure to also check"
                "interesting edge cases. There should be at least 10 different"
                "unit tests"
            )
        }
    ]
)

# Get the generated Python code from the OpenAI response
generated_code = completion.choices[0].message.content

# Write the generated code to a file named 'generatedcode.py'
with open("generatedcode.py", "w") as file:
    file.write(generated_code)

# Define a default result object
result = None

# Run the generated Python file using subprocess.run
try:
    print("\nRunning the generated code...\n")
    result = subprocess.run(
        ['python3', 'generatedcode.py'],
        capture_output=True, text=True, timeout=10  # 10-second timeout
    )

    # Print the result of the program's execution
    print("Program Output:")
    print(result.stdout)

    # If there's any error, print it
    if result.stderr:
        print("Program Error:")
        print(result.stderr)

except subprocess.TimeoutExpired:
    print("Error: The program took too long to execute and was terminated.")

# Validation step: Check if the generated code runs properly
if result and (
        "Traceback" in result.stderr or "AssertionError" in result.stdout):
    print("\nThe generated code or unit tests failed.")
elif result is None:
    print("\nThe program did not complete execution (likely due to timeout).")
else:
    print("\nThe generated code and unit tests ran successfully.")
