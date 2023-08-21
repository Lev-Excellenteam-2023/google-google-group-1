import words_trie
from unittest.mock import MagicMock
import logging


def test_complete_word_1():
    sentence_node = MagicMock()
    sentence_node.word = 'world'
    trie = words_trie.Trie()
    trie.insert(sentence_node)
    assert trie.query('w') == [('world', 1)]

def test_complete_word_2():
    sentence_node_1 = MagicMock()
    sentence_node_1.word = 'world'
    sentence_node_2 = MagicMock()
    sentence_node_2.word = 'word'
    trie = words_trie.Trie()
    trie.insert(sentence_node_1)
    trie.insert(sentence_node_2)
    assert trie.query('wo') == [('world', 1), ('word', 1)]

def test_get_reference_from_word_1():
    # Checking if we
    sentence_node = MagicMock()
    sentence_node.word = 'world'
    sentence_node.id = 1
    trie = words_trie.Trie()
    trie.insert(sentence_node)
    assert trie.get_references_from_word('world')[0].id == 1






