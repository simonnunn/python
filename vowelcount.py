# Name    : 05CountVowels

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Word Vowel Count

word = str(input("Please enter a word: "))

count_vowel = 0
                 
for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count_vowel = count_vowel + 1

print("Number of vowels is","=",count_vowel)


