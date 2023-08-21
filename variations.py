import logging
from typing import List
 
def check_possible_variations(original_word: str, candidate_words: List[str]) -> List[str]:
    """
    Receives a word and a list of candidates and returns a list of all the possible variations
    :param original_word: str
    :param possible_variations: list of str
    :return: list of str
    """
    possible_variations = []
    for candidate_word in candidate_words:
        if len(candidate_word) == len(original_word):
            # Check for one letter difference
            if sum([1 if candidate_word[i] != original_word[i] else 0 for i in range(len(candidate_word))]) == 1:
                possible_variations.append(candidate_word)
        elif len(candidate_word) == len(original_word) + 1:
            # Check for one letter addition
            for i in range(len(candidate_word)):
                if candidate_word[:i] + candidate_word[i + 1:] == original_word:
                    possible_variations.append(candidate_word)
                    break
        elif len(candidate_word) == len(original_word) - 1:
            # Check for one letter deletion
            for i in range(len(original_word)):
                if original_word[:i] + original_word[i + 1:] == candidate_word:
                    possible_variations.append(candidate_word)
                    break
    return possible_variations

