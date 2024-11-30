import subprocess
from openai import OpenAI
import random
import time
from colorama import Fore, init
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

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
    "A program that checks if a number is a palindrome",
    "A program that finds the kth smallest element in a given binary search"
    "tree",
    "A program that returns the median of two sorted arrays.",
    "A Program that merges two sorted lists."
    ]


# Use OpenAI API to generate code for the chosen program
def generate_code(program_description, message_history=None,
                  error_message=None, optimize=False, lint_feedback=None):
    if message_history is None:
        message_history = []

    # starting prompt message
    if not message_history:
        initial_message = {
            "role": "user",
            "content": (
                "Create a Python program for the following task:"
                f"\n\n{program_description}\n\n"
                " Do not write any explanations, and comments and do not "
                "include code block markers. Just show me the raw code"
                " itself. Please include running unit tests with"
                " asserts that check the logic of the program."
                " Make sure to also check interesting edge cases."
                " There should be at least 10 different unit tests"
            )
        }
        message_history.append(initial_message)

    # Append error feedback if provided
    if error_message:
        message_history.append({
            "role": "user",
            "content": (
                "The previously generated code had these errors:"
                f"\n\n{error_message}\n\n"
                "Please correct the code and provide the full fixed version."
                "Do not write any explanations, and comments and do not "
                "include code block markers. Just show me the raw code itself"
            )
        })

    # Append lint feedback if provided
    if lint_feedback:
        message_history.append({
            "role": "user",
            "content": (
                "The optimized code has the following lint errors/warnings: "
                f"\n\n{lint_feedback}\n\n"
                "Please fix these issues and ensure the code passes a lint"
                "check with pylint. Make sure that the code's logic remains "
                "unchanged and all existing tests still pass. "
                "Do not write any explanations, and comments and do not"
                " include code block markers. Just show me the raw code itself"
            )
        })

    # Add optimization request
    if optimize:
        message_history.append({
            "role": "user",
            "content": (
                "Now optimize the code to run faster."
                "Keep the same functionality and unit tests but focus on"
                " improving performance. Ensure the tests still pass."
                "Do not write any explanations, and comments and do not "
                "include code block markers. Just show me the raw code itself"
            )
        })

    # Call to OpenAi API
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=message_history
            )
    except Exception as e:
        print(Fore.RED + f"OpenAI API Error: {e}")
        return None, message_history

    # Append assistant's reply to the history
    assistant_message = completion.choices[0].message.content.strip()
    message_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # return the generated Python code from the OpenAI response
    # and the updated messages
    return assistant_message, message_history


# Measure execution time of the generated code
def measure_execution_time(file_path):
    start_time = time.time()
    try:
        subprocess.run(['python3', file_path], capture_output=True, text=True,
                       timeout=10)
    except subprocess.TimeoutExpired:
        print(Fore.RED + "Error: The program took too long to execute and was"
              "terminated.")
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds


# Check linting with pylint
def check_lint(file_path):
    try:
        result = subprocess.run(
            ['pylint', file_path],
            capture_output=True, text=True
        )
        return result.returncode, result.stdout  # Return code and lint output
    except FileNotFoundError:
        print(Fore.RED + "\nError: 'pylint' is not installed or not in PATH.")
        return -1, "pylint not found"


# Main function for user interaction and program generation
def main():
    print(Fore.CYAN + "I'm Super Python Coder. Tell me, which program would"
          " you like me to code for you?")
    print(Fore.YELLOW + "If you don't have an idea, just press enter and I"
          " will choose a random program to code.")
    user_input = input(Fore.CYAN + "Your choice: ").strip()

    # Determine the program idea
    if user_input == "":
        chosen_program = random.choice(PROGRAMS_LIST)
        print(Fore.MAGENTA + "\nHere's a randomly chosen program"
              " idea for you:")
        print(Fore.GREEN + chosen_program)
    else:
        chosen_program = user_input
        print(Fore.GREEN + f"\nYou asked me to code: '{chosen_program}'")

    # Initialize message history and error message
    message_history = []
    error_message = None

    # Phase 1: Generate and run code
    success = False
    for attempt in tqdm(range(1, 6), desc="Code Generation Attempts",
                        unit="try"):
        print(Fore.BLUE + f"\nAttempt {attempt} "
              "to generate and run the code...")
        try:
            # Generate Code
            generated_code, message_history = generate_code(
                chosen_program, message_history, error_message)
            if not generated_code:
                raise RuntimeError("Failed to generate code from OpenAI API.")

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
            print(Fore.GREEN + "\nCode creation completed successfully!")
            subprocess.run(["open", "generatedcode.py"])
            success = True
            break

        except Exception as e:
            print(Fore.RED + f"\nError running generated code! Error: {e}. "
                  "Trying again...")
            # Append error details to message_history for context in the next
            # attempt
            error_message = {e}

    # If all attempts fail
    if not success:
        print(Fore.RED + "\nCode generation FAILED")
        return

    # Phase 2: Optimization
    # Measure the execution time of the generated code
    print(Fore.BLUE + "\nMeasuring execution time...")
    initial_time = measure_execution_time("generatedcode.py")
    print(Fore.CYAN + f"Initial execution time: {initial_time:.2f} ms")

    # Generate optimized code
    print(Fore.BLUE + "\nRequesting optimized code...")
    optimized_time = initial_time
    while optimized_time >= initial_time:
        optimized_code, message_history = generate_code(
            chosen_program, message_history, optimize=True)
        with open("optimized_code.py", "w") as file:
            file.write(optimized_code)

        # Measure the execution time of the optimized code
        optimized_time = measure_execution_time("optimized_code.py")

    # optimized time < initial time
    print(Fore.GREEN + "\nCode running time optimized! It now runs in"
          f" {optimized_time:.2f} ms, "
          f"while before it was {initial_time:.2f} ms."
          )

    # Open the optimized file
    subprocess.run(["open", "optimized_code.py"])

    # Phase 3: Lint check
    print(Fore.BLUE + "\nRunning lint check...")
    for lint_attempt in tqdm(range(1, 4), desc="Lint Check Attempts",
                             unit="fix"):
        return_code, lint_output = check_lint("optimized_code.py")
        if return_code == 0:
            print(Fore.GREEN + "\nAmazing. No lint errors/warnings.")
            break
        else:
            print(Fore.YELLOW + "\nLint errors/warnings found "
                  f"(attempt {lint_attempt}):"
                  f"\n{lint_output}")
            if lint_attempt < 3:
                generated_code, message_history = generate_code(
                    chosen_program, message_history, error_message=None,
                    optimize=False, lint_feedback=lint_output)
                with open("optimized_code.py", "w") as file:
                    file.write(generated_code)
            else:
                print(Fore.RED + "There are still lint errors/warnings.")
                return


if __name__ == "__main__":
    main()
