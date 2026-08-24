# Python Word Counter

paragraph = input("Enter a paragraph: ")

# Convert to lowercase and split into words
words = paragraph.lower().split()

# Count occurrences of the word "python"
count = words.count("python")

print("\n----- WORD COUNT -----")
print(f'The word "python" appears {count} time(s).')
print("---------------------")