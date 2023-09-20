import re

text = "The quick brown fox jumps over the lazy dog."

# Find all words that start with the letter "q"
matches = re.findall(r"\bq\w+", text)
print(matches) # Output: ['quick']

# Replace all occurrences of "the" with "a"
new_text = re.sub(r"\bthe\b", "a", text)
print(new_text) # Output: A quick brown fox jumps over a lazy dog.