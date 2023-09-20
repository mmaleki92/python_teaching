def count_vowels_consonants(string):
    vowels = "aeiou"
    num_vowels = 0
    num_consonants = 0
    for char in string:
        if char.lower() in vowels:
            num_vowels += 1
        elif char.isalpha():
            num_consonants += 1
    return num_vowels, num_consonants

string = "Hello, World!"
print(count_vowels_consonants(string))