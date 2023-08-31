from src.search import autocomplete_no_mistakes, autocomplete_with_incomplete_last_word
from src.Sentence_trie import SentenceTrie , complete_sentence
from src.words_trie import Trie

sentence_trie = SentenceTrie()
words_trie = Trie()
sentence_trie.add_sentence('hello world')
sentence_trie.add_sentence('hello dear Alexander')
sentence_trie.add_sentence('dear Yehuda Shani')
sentence_trie.add_sentence('Alexander is greate student')
sentence_trie.add_sentence('Alexander is not calm')
sentence_trie.add_sentence('I ignore him')
words_trie.insert_data(sentence_trie)


def test_autocomplete_no_mistakes_1():
    sentence_nodes = autocomplete_no_mistakes('hello', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['hello world', 'hello dear Alexander']


def test_autocomplete_no_mistakes_2():
    sentence_nodes = autocomplete_no_mistakes('hello dear', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['hello dear Alexander']


def test_autocomplete_no_mistakes_3():
    sentence_nodes = autocomplete_no_mistakes('dear', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['hello dear Alexander', 'dear Yehuda Shani']


def test_autocomplete_no_mistakes_4():
    sentence_nodes = autocomplete_no_mistakes('student', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['Alexander is greate student']


def test_autocomplete_with_incomplete_last_word_1():
    sentence_nodes = autocomplete_with_incomplete_last_word('stu', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['Alexander is greate student']


def test_autocomplete_with_incomplete_last_word_2():
    sentence_nodes = autocomplete_with_incomplete_last_word('Alexan', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['hello dear Alexander', 'Alexander is greate student', 'Alexander is not calm']


def test_autocomplete_with_incomplete_last_word_3():
    sentence_nodes = autocomplete_with_incomplete_last_word('Alexander is not c', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['Alexander is not calm']


def test_autocomplete_with_incomplete_last_word_4():
    sentence_nodes = autocomplete_with_incomplete_last_word('dear Yehuda S', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['dear Yehuda Shani']


def test_autocomplete_with_incomplete_last_word_5():
    sentence_nodes = autocomplete_with_incomplete_last_word('is gre', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['Alexander is greate student']


def test_autocomplete_with_incomplete_last_word_6():
    sentence_nodes = autocomplete_with_incomplete_last_word('i', sentence_trie, words_trie)
    sentences = []
    for sentence_node in sentence_nodes:
        sentence = complete_sentence(sentence_node)
        sentences.append(sentence)
    assert sentences == ['Alexander is greate student', 'Alexander is not calm', 'I ignore him']


