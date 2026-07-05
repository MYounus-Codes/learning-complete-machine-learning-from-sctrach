## File Handling in Python
## Files are used to store data permanently. We can create, write, read, and close files using Python.

from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")

# Writing text to a file
with file_path.open("w", encoding="utf-8") as file:
    file.write("Hello from Python\n")
    file.write("We are learning file handling.\n")

print(f"File written to: {file_path}")

# Reading the file content back
with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

print("File content:")
print(content)
