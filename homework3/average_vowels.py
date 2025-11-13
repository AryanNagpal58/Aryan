# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(sentence):
    count_vowels = 0
    count_consonants = 0
    for char in sentence:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count_vowels += 1
        elif char != " ":
            count_consonants += 1

    return(count_vowels, count_consonants)

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(sentences):

    list_of_sentences = []
    index_start = 0
    index = 0
    vowels_in_all_sentences = 0
    consonants_in_all_sentences = 0
    for char in sentences:
        if char == "." or char == "!" or char == "?":
            sentence = sentences[index_start:index+1].strip()
            list_of_sentences.append(sentence)
            index_start = index + 1
        index += 1

    number_of_sentences = len(list_of_sentences)

    for sentence in list_of_sentences:
        vowels_in_all_sentences += counting_vowels_and_consonants(sentence)[0]
        consonants_in_all_sentences += counting_vowels_and_consonants(sentence)[1]

    average_vowels = vowels_in_all_sentences / len(list_of_sentences)
    average_consonants = consonants_in_all_sentences / len(list_of_sentences)
    return (number_of_sentences, average_vowels, average_consonants)




# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
print(f"This quote from Richard Feynman includes {counting_vowels_and_consonants(sentence = paragraph)[0]} vowels, as well as")
print(f"{counting_vowels_and_consonants(sentence = paragraph)[1]} consonants. On average, there are {average_vowels_and_consonants(sentences = paragraph)[1]} vowels per sentence, as well as ")
print(f"{average_vowels_and_consonants(sentences = paragraph)[2]} consonants per sentence within this quote of {average_vowels_and_consonants(sentences = paragraph)[0]}")