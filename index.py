
# Example pseudocode to get you started (replace with actual code as per your notebook structure)

import re

# Read the contents of the file
with open('Regex_test.txt', 'r') as file:
    content = file.read()

# Extract names using regex
names = re.findall(r'[A-Z][a-z]+(?: [A-Z][a-z-]+){0,2}', content)
for name in names:
    print(name)

# Extract additional patterns as needed (emails, etc.)

# Answer the question at the end of the notebook
print("\nDid the student meet the minimum basic requirements of the instructions: - Turned in on time - Correct file/file structure - Completed the tasks given")
print("2 pts")
print("\nDid the student show an understanding of the course work: - Used the skills learned from class - When run, the code works correctly as intended - Code is well written and efficient")
print("2 pts")
print("\nExtra point for extra work: - Edge cases are considered and errors are caught - Does more than just minimum requirements")
print("1 pt")
Key Points:
Regular Expressions: These are crucial for pattern matching tasks.
File Handling: Use open() and read() methods to load file contents into memory.
Testing and Debugging: Regularly test your code to catch errors early.
Documentation: Ensure you understand and answer any questions or reflections asked in the notebook.