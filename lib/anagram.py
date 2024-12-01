# lib/anagram.py
class Anagram:
    def __init__(self, word):
        # Initialize with the word for which anagrams will be found
        self.word = word

    def match(self, possible_anagrams):
        # Find all words in possible_anagrams that are anagrams of self.word
        return [candidate for candidate in possible_anagrams if sorted(candidate) == sorted(self.word)]
