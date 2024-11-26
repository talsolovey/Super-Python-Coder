import subprocess
from openai import OpenAI
import random

# Initialize OpenAI client
client = OpenAI()

# List of program ideas
PROGRAMS_LIST = [
    '''Given two strings str1 and str2, prints all interleavings of the given
    two strings. You may assume that all characters in both strings are
    different.Input: str1 = "AB", str2 = "CD"
    Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB
    Input: str1 = "AB", str2 = "C"
    Output:
    ABC
    ACB
    CAB "''',
    " A program that checks if a number is a palindrome",
    " A program that finds the kth smallest element in a given binary search"
    "tree",
    " A program that returns the median of two sorted arrays.",
    " A Program that merges two sorted lists."
    ]


def generate_code(program_description, error_message=None):
    # Use OpenAI API to generate code for the chosen program
    messages = [
            {
                "role": "user",
                "content": (
                    "Create a Python program for the following task:"
                    f"\n\n{program_description}\n\n"
                    " Do not write any explanations, and do not include code"
                    " block markers like ```python. Just show me the raw code"
                    " itself. Ensure that the code follows PEP 8 style"
                    " guidelines, especially the one that requires two blank"
                    " lines after class or function definitions."
                    " Make sure that blank lines are not empty with whitespace"
                    ", especially the last line, and the file ends with one"
                    "  new line. Also make sure that each line has at most 79"
                    " characters. please include running unit tests with"
                    " asserts that check the logic of the program."
                    " Make sure to also check interesting edge cases."
                    " There should be at least 10 different unit tests"
                )
            }
        ]

    if error_message:
        messages.append({
            "role": "user",
            "content": "The previously generated code had these errors:"
            f"\n\n{error_message}\n\n"
            "Please correct the code and provide the full fixed version."
        })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # return the generated Python code from the OpenAI response
    return completion.choices[0].message.content


# Main function for user interaction and program generation
def main():
    print("I'm Super Python Coder. Tell me, which program would you like me to"
          " code for you?")
    print("If you don't have an idea, just press enter and I will choose a"
          " random program to code.")
    user_input = input("Your choice: ").strip()

    # Determine the program idea
    if user_input == "":
        chosen_program = random.choice(PROGRAMS_LIST)
        print("\nHere's a randomly chosen program idea for you:")
        print(chosen_program)
    else:
        print(f"\nYou asked me to code: '{chosen_program}'")

    for attempt in range(1, 6):
        print(f"\nAttempt {attempt} to generate and run the code...\n")

        try:
            # Generate Code
            generated_code = generate_code(chosen_program)

            # Write the generated code to a file named 'generatedcode.py'
            with open("generatedcode.py", "w") as file:
                file.write(generated_code)

            # Run the generated code
            result = subprocess.run(
                ['python3', 'generatedcode.py'],
                capture_output=True, text=True, timeout=10  # 10-second timeout
            )

            # Check if the code ran successfully
            if result.stderr or "AssertionError" in result.stdout:
                raise RuntimeError(result.stderr or result.stdout)

            # If successful, print success message and open the file
            print("Code creation completed successfully!")
            subprocess.call(["open", "generatedcode.py"])
            return

        except Exception as e:
            print(f"Error running generated code! Error: {e}. Trying again...")
            chosen_program = f"{chosen_program}\n\nError details: {e}"

    # If all attempts fail
    print("Code generation FAILED")


if __name__ == "__main__":
    main()
