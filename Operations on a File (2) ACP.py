import os

english = ["Pronouns are words that replace a noun\n", "Possessive pronuouns are used to show possession or ownership\n", "A sentence can still make sense even when you remove the emphasizing pronoun from it\n"]
physics = ["A measurment consists of a number and a unit\n", "The SI unit of length is meter\n", "The two types of systems of measurment were the English and Metric Sytem of Units\n"]

with open("English Notes.txt", "w") as language:
    language.writelines(english)

with open("Physics Notes.txt", "w") as world:
    world.writelines(physics)

print("\nYour notes have been created successfully!")

print("\n", "-" * 15, "PART 1: ENGLISH NOTES", "-" * 15)

with open("English Notes.txt", "r") as language:
    for line in language:
        print(line.strip())

print("-" * 52)

print("\n", "-" * 15, "PART 2: WORD COUNT IN PHYSICS NOTES", "-" * 15)

with open("Physics Notes.txt", "r") as world:
    for line in world:
        words = line.split()
        print(f"{len(words)} words - {line.strip()}")

print("-" * 65)


print("\n", "-" * 15, "PART 3: CHECKING MERGED FILE", "-" * 15)

merged_file = "All Notes.txt"

if os.path.exists(merged_file):
    print(f"{merged_file} already exists in your folder.")

else:
    print(f"{merged_file} does not exist in your folder.")

print("-" * 58)


print("\n", "-" * 15, "PART 4: REMOVE OLD FILE", "-" * 15)

if os.path.exists(merged_file):
    os.remove(merged_file)
    print("Merged file is deleted.")
else:
    print("No merged file to remove.")

print("-" * 53)


print("\n", "-" * 15, "PART 5: MERGING FILES", "-" * 15)

with open(merged_file, "w") as merge:
    merge.write("========== ENGLISH NOTES ==========\n")

    with open("English Notes.txt", "r") as language:
        merge.write(language.read())
        merge.write("===================================\n")

    merge.write("\n========== PHYSICS NOTES ==========\n")

    with open("Physics Notes.txt", "r") as world:
        merge.write(world.read())


print("\nYour English and Physics Notes have been successfully combined!")

print("-" * 51)

print("\n", "-" * 15, "PART 6: MERGED STUDY NOTES", "-" * 15, "\n")

with open(merged_file, "r") as merge:
    print("~" * 10, "MERGED NOTES", "~" * 10)

    for line in merge:
        print(line.strip())

    print("=" * 32, "\n")

print("-" * 56)


print("=============== SUMMARY OF STUDY NOTES ORGANIZER SYSTEM ===============")

print("'with open() as file' : Used for safe file handling")
print("'split()' : Used to count words in each line by splitting the words")
print("'os.path.exists()' : Used for checking if a file exists")
print("\nSuccess of the program - File Merge: English and Physics notes were combined.")

print("=" * 71)