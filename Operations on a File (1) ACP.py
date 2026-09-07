sample_notes = ["IMPORTANT : Complete Python Homework\n", "TO-DO : Revise File Handling Concepts\n", "NOTE : The function 'read(n)' previews characters\n", "IMPORTANT : Submit Assignment Today\n", "NOTE : The function 'readlines()' stores lines in a list\n", "TO-DO : Practice loops with files\n"]

file = open("Class Notes.txt", "w")
file.writelines(sample_notes)
file.close()

print("\nYour sample file containing your Class Notes has successfully been created!")

# PART 1
print("\n", "-" * 15, "PART 1: PREVIEW WITH READ()", "-" * 15)

file = open("Class Notes.txt", "r")

characters = int(input("Enter the number of characters you want to preview from your Class Notes:"))
print(f"The first {characters} characters in your Class Notes are: {file.read(characters)}")

print("-" * 57)

# PART 2
print("\n", "-" * 15, "PART 2: USE READLINES()", "-" * 15)

file = open("Class Notes.txt", "r")

lines = file.readlines()
print(f"The number of lines in your Class Notes are: {len(lines)}\n")

for i in range(1, len(lines) + 1):
    print(f"{i} - {lines[i - 1].strip()}")

print("-" * 52)

# PART 3
print("\n", "-" * 15, "PART 3: LOOP LINE BY LINE", "-" * 15)

file = open("Class Notes.txt", "r")

for line in file:
    print(f"Reading: {line.strip()}")

file.close()

print("-" * 55)

# PART 4
print("\n", "-" * 15, "PART 4: FILTER WITH A CONDITION", "-" * 15)

file = open("Class Notes.txt", "r")

word = input("Skip Class Notes starting with the word:")

print()

for i in file:
    if i.startswith(word):
        print(f"Skip - {i.strip()}")

    else:
        print(f"Keep - {i.strip()}")

file.close()

print("-" * 61)

# PART 5
print("\n", "-" * 15, "PART 5: COPY THE SELECTED LINES TO A NEW FILE", "-" * 15)

file =  open("Class Notes.txt", "r")

lines = file.readlines()

file.close()

new_file = open("Organized Notes.txt", "w")

copied = 0

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TO-DO"):
        new_file.write(line)

        copied += 1
print(f"You have copied {copied} lines into your Organized Notes.")

print("-" * 75)

# PART 6
print("\n", "-" * 15, "PART 6: ORGANIZED NOTES", "-" * 15)

new_file = open("Organized Notes.txt")

for line in new_file:
    print(line.strip())

file.close()

print("-" * 52)