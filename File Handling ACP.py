file = open("Shopping List.txt", "w")

file.write("1. Choc-chip Yoghurt (5)\n")
file.write("2. Dark Chocolate Bars (5)\n")
file.write("3. Eclairs (10)\n")

file.close()
print(f"\nYour Shopping List has been created successfully!")

file = open("Shopping List.txt", "r")

shopping_list = file.read()

print("\n", "-" * 15, "SHOPPING LIST", "-" * 15)
print(shopping_list)
print("-" * 43)

file.close()

file = open("Shopping List.txt", "a")

file.write("4. Chocolate Croissants (5)\n")
file.write("5. KitKat Ice-cream (1)\n")

file.close()
print("\nTwo more items added successfully!\n")

file = open("Shopping List.txt", "r")

updated_shopping_list = file.read()
print("-" * 15, "UPDATED SHOPPING LIST", "-" * 15)
print(updated_shopping_list)
print("-" * 51)

file.close()

file = open("Shopping List.txt", "r")

print("\n", "-" * 15, "SHOPPING LIST (LINE BY LINE)", "-" * 15)
lines = 1

for i in file:
    print(f"Line {lines} : {i.strip()}")
    lines += 1

print("-" * 58)

print("\n", "-" * 15, "SHOPPING LIST SUMMARY", "-" * 15)
print("Your Shopping List:\n")
print(updated_shopping_list)
print("Tasks Done:\n-> Read Shopping List\n-> Read Shopping List Line by Line")
print("-" * 51)