from variations import check_possible_variations, find_candidate_words_for_last_word
from Sentence_trie import SentenceTrie, complete_sentence, SentenceNode
from words_trie import Trie

posible_words = ['alex', 'yehuda', 'omer', 'drive', 'drove', 'yehudi']


def test_check_possible_variations_1():
    assert check_possible_variations('ole', posible_words) == []
    assert check_possible_variations('lex', posible_words) == ['alex']
    assert check_possible_variations('ale', posible_words) == ['alex']
    assert check_possible_variations('almx', posible_words) == ['alex']
    assert check_possible_variations('alx', posible_words) == ['alex']
    assert check_possible_variations('drve', posible_words) == ['drive', 'drove']
    assert check_possible_variations('drave', posible_words) == ['drive', 'drove']
    assert check_possible_variations('yehud', posible_words) == ['yehuda', 'yehudi']
    assert check_possible_variations('yehu', posible_words) == []
    assert check_possible_variations('yehhuda', posible_words) == ['yehuda']
    assert check_possible_variations('yhuda', posible_words) == ['yehuda']
    assert check_possible_variations('yehrda', posible_words) == ['yehuda']


def test_find_candidate_words_for_last_word_1():
    sentence_trie = SentenceTrie()
    sentence_trie.add_sentence('alex drove the car')
    sentence_trie.add_sentence('alex drove the bus')
    words_trie = Trie()
    words_trie.insert_data(sentence_trie)

    candidate_words = find_candidate_words_for_last_word('alex drove the pasta', sentence_trie, words_trie)

    assert candidate_words == ['car', 'bus']


def test_find_candidate_words_for_last_word_2():
    sentence_trie = SentenceTrie()
    sentence_trie.add_sentence('alex drove the car')
    sentence_trie.add_sentence('alex drove the bus')
    sentence_trie.add_sentence('alex ate the pasta')
    words_trie = Trie()
    words_trie.insert_data(sentence_trie)

    candidate_words = find_candidate_words_for_last_word('alex drove the plane', sentence_trie, words_trie)

    assert candidate_words == ['car', 'bus']

def test_find_candidate_words_for_last_word_3():
    sentence_trie = SentenceTrie()
    sentence_trie.add_sentence('hello world')
    sentence_trie.add_sentence('hello dear Alexander')
    sentence_trie.add_sentence('dear Yehuda Shani')
    sentence_trie.add_sentence('Alexander is great student')
    sentence_trie.add_sentence('I am hungry')
    words_trie = Trie()
    words_trie.insert_data(sentence_trie)
    candidate_words = find_candidate_words_for_last_word('Alexander if', sentence_trie, words_trie)
    assert candidate_words == ['is']


