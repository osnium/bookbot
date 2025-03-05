def get_num_words(text):
    return len(text.split())

# returns a dictionary of how often each letter / symbol / punctuation mark appears in the text

def get_letter_stats(text):
    letter_stats = {}
    for char in text:
        if char in letter_stats:
            letter_stats[char] += 1
        else:
            letter_stats[char] = 1
    return letter_stats
    
# sorts by value in descending order

