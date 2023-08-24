import logging
from src.search import autocomplete_no_mistakes, autocomplete_with_incomplete_last_word, find_terminal_nodes_from_search
from src.Sentence_trie import SentenceTrie, SentenceNode
from src.words_trie import Trie
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


def find_candidate_words(sentence: str, word_to_change: int, sentence_trie: SentenceTrie, words_trie: Trie) -> List[str]:
    """
    Receives a sentence and word to change, and finds what words can come instead of the word to change
    :param sentence: str
    :param word_to_change: int
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    words = sentence.split()

    # If the word to change is the last word in the sentence, send to special function
    if word_to_change == len(words) - 1:
        return find_candidate_words_for_last_word(sentence, sentence_trie, words_trie)



def find_candidate_words_for_last_word(sentence:str, sentence_trie: SentenceTrie, words_trie: Trie) -> List[str]:
    """
    Receives a sentence and finds what words can come instead of the last word
    :param sentence: str
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    # Check if it has only one word
    if len(sentence.split()) == 1:
        possible_words = words_trie.query("")
        possible_words = [word[0] for word in possible_words]
        return possible_words

    words = sentence.split()
    new_sentence = ' '.join(words[:-1])
    terminal_nodes = find_terminal_nodes_from_search(new_sentence, words_trie)
    possible_last_nodes = []
    for node in terminal_nodes:
        possible_last_nodes.extend(node.children)

    possible_last_words = [node.word for node in possible_last_nodes]

    return possible_last_words

def calculate_all_variations(sentence: str) -> List[str]:
    """
    Receives a sentence and returns a list of all the possible variations, by changing one every letter
    And by adding and deleting one letter
    :param sentence: str
    :return: list of str
    """

    variations = []

    # Changing one letter
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(len(sentence)):
            variations.append(sentence[:i] + letter + sentence[i + 1:])

    # Adding one letter
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(len(sentence) + 1):
            variations.append(sentence[:i] + letter + sentence[i:])

    # Deleting one letter
    for i in range(len(sentence)):
        variations.append(sentence[:i] + sentence[i + 1:])


    return variations




