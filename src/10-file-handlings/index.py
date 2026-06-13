# ============================================================
# FILE HANDLING IN PYTHON
# Senior tip: Files are external resources. Always close them.
# The modern way: use `with` — it closes automatically, even on crash.
# ============================================================


# ============================================================
print("=" * 50)
print("1. Write to a file")
print("=" * 50)
# ============================================================

# "w" = write mode. Creates file if not exists. OVERWRITES if it does.
with open("notes.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")

print("File written.")


# ============================================================
print("\n" + "=" * 50)
print("2. Read entire file")
print("=" * 50)
# ============================================================

# "r" = read mode (default). File must exist or you get FileNotFoundError.
with open("notes.txt", "r") as f:
    content = f.read()       # reads the whole file as one string
    print(content)


# ============================================================
print("=" * 50)
print("3. Read line by line (memory-safe for large files)")
print("=" * 50)
# ============================================================

# Senior tip: Never use .read() on a 2GB log file. Use a loop instead.
# Each iteration loads only ONE line into memory.
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # .strip() removes the trailing \n


# ============================================================
print("\n" + "=" * 50)
print("4. Append to a file (don't overwrite)")
print("=" * 50)
# ============================================================

# "a" = append mode. Adds to the end. Creates file if not exists.
with open("notes.txt", "a") as f:
    f.write("Line 3: Appended later\n")

with open("notes.txt", "r") as f:
    print(f.read())


# ============================================================
print("=" * 50)
print("5. readlines() — get all lines as a list")
print("=" * 50)
# ============================================================

with open("notes.txt", "r") as f:
    lines = f.readlines()    # returns ["Line 1...\n", "Line 2...\n", ...]

print(f"Total lines: {len(lines)}")
print(f"First line : {lines[0].strip()}")
print(f"Last line  : {lines[-1].strip()}")


# ============================================================
print("\n" + "=" * 50)
print("6. Check if file exists before reading")
print("=" * 50)
# ============================================================

# Senior tip: never assume a file exists. Always guard with os.path or pathlib.
import os

if os.path.exists("notes.txt"):
    print("File exists, safe to read.")
else:
    print("File not found!")

# Modern Python prefers pathlib over os.path
from pathlib import Path

path = Path("notes.txt")
print(f"Exists   : {path.exists()}")
print(f"File size: {path.stat().st_size} bytes")


# ============================================================
print("\n" + "=" * 50)
print("7. Write & read JSON (most common in real projects)")
print("=" * 50)
# ============================================================

import json

user = {"name": "Kishan", "age": 25, "skills": ["Python", "JS"]}

# Write dict → JSON file
with open("user.json", "w") as f:
    json.dump(user, f, indent=4)  # indent makes it human-readable

# Read JSON file → dict
with open("user.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print(f"Name: {loaded['name']}, Skills: {loaded['skills']}")


# ============================================================
print("\n" + "=" * 50)
print("8. File modes cheat sheet")
print("=" * 50)
# ============================================================

# "r"  — read only          (error if file missing)
# "w"  — write, overwrite   (creates if missing)
# "a"  — append             (creates if missing)
# "x"  — create new file    (error if file already exists — safe write)
# "rb" — read binary        (images, PDFs, zip files)
# "wb" — write binary

# Senior tip: use "x" when you never want to silently overwrite an existing file.
try:
    with open("notes.txt", "x") as f:
        f.write("This won't run if notes.txt exists")
except FileExistsError:
    print("'x' mode caught it: file already exists, nothing overwritten.")


# ============================================================
print("\n" + "=" * 50)
print("9. Writing multiple lines at once with writelines()")
print("=" * 50)
# ============================================================

lines_to_write = ["alpha\n", "beta\n", "gamma\n"]

with open("batch.txt", "w") as f:
    f.writelines(lines_to_write)   # no separator added — you manage \n yourself

with open("batch.txt", "r") as f:
    print(f.read())


# ============================================================
print("=" * 50)
print("10. Cleanup — delete files created during this script")
print("=" * 50)
# ============================================================

import os

for filename in ["notes.txt", "user.json", "batch.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted: {filename}")
