from Sentence_trie import SentenceTrie, complete_sentence, SentenceNode
from words_trie import Trie
from typing import List
from scoring import score_sentence
from search import autocomplete_with_incomplete_last_word, find_terminal_nodes_from_search, check_sentence_exists, autocomplete_no_mistakes
from variations import check_possible_variations, find_candidate_words_for_last_word, calculate_all_variations


def fix_last_word(sentence: str, sentence_trie: SentenceTrie, words_trie: Trie) -> List[str]:
    """
    Receives a sentence and returns a list of all the possible sentences that fix last word
    :param sentence: input sentence
    :param sentence_trie:
    :param words_trie:
    :return: list of possible sentences
    """

    words = sentence.split()
    candidate_words = find_candidate_words_for_last_word(sentence, sentence_trie,
                                                         words_trie)  # finds possible completions for the frase without the last word
    viable_words = check_possible_variations(words[-1],
                                             candidate_words)  # filters completions to those that are possible
    possible_sentences = [sentence[:-len(words[-1])] + word for word in viable_words]  # creates possible
    terminal_nodes =[]
    possible_nodes = []
    for possibility in possible_sentences:
        possible_nodes.extend(
            find_terminal_nodes_from_search(possibility, words_trie))  # finds terminal nodes for each possible sentence

    for node in possible_nodes:
        terminal_nodes += sentence_trie.find_all_terminals(node)

    # Removing frases that are already present
    complete_sentences = [complete_sentence(node) for node in terminal_nodes]

    return complete_sentences


def check_frase_as_is(sentence: str, sentence_trie: SentenceTrie, words_trie: Trie) -> List[str]:
    """
    Receives a sentence and returns a list of all the possible completions
    :param sentence: str
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    terminal_nodes = []

    # Step 1: send the sentence as is
    nodes = autocomplete_with_incomplete_last_word(sentence, sentence_trie, words_trie)
    for node in nodes:
        terminal_nodes += sentence_trie.find_all_terminals(node)

    final_sentences = [(complete_sentence(node), len(sentence) * 2) for node in terminal_nodes] # scoring by hand, 2 points per letter

    if len(final_sentences) >= 5:
        return final_sentences[:5]

    # Step 2: fix last word
    complete_sentences = fix_last_word(sentence, sentence_trie, words_trie)
    final_sentences_without_score = [final[0] for final in final_sentences]
    filtered_sentences = [complete for complete in complete_sentences if complete not in final_sentences_without_score] # filters out sentences that were already added

   # add possible sentences to final sentences
    final_sentences += [(possibility, score_sentence(sentence, possibility)) for possibility in filtered_sentences]

    if len(final_sentences) >= 5:
        return final_sentences[:5]

    return final_sentences[:5]


def find_mistakes(sentence: str, sentence_trie: SentenceTrie, words_trie: Trie) -> List[str]:
    """
    Receives a sentence and returns a list of all the possible completions, using a naive approach that checks all possibilities
    :param sentence: str
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    possible_variations = calculate_all_variations(sentence)
    # filter redundant variations
    no_duplicates_variations = list(dict.fromkeys(possible_variations))


    possible_sentences = [variation for variation in no_duplicates_variations if check_sentence_exists(variation, sentence_trie, words_trie)]

    final_sentence_nodes = [autocomplete_no_mistakes(sentence, sentence_trie, words_trie) for sentence in possible_sentences]

    flattened_list = [node for sublist in final_sentence_nodes for node in sublist]

    final_sentences = [(complete_sentence(node), score_sentence(sentence, complete_sentence(node))) for node in flattened_list] # scoring by hand, 2 points per letter

    return final_sentences



