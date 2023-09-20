def find_longest_palindrome(string):
    longest_palindrome = ""
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

string = "babad"
print(find_longest_palindrome(string))