from full_search import check_frase_as_is
from Sentence_trie import SentenceTrie , complete_sentence
from words_trie import Trie

sentence_trie = SentenceTrie()
words_trie = Trie()
sentence_trie.add_sentence('hello world')
sentence_trie.add_sentence('hello dear Alexander')
sentence_trie.add_sentence('dear Yehuda Shani')
sentence_trie.add_sentence('Alexander is great student')
sentence_trie.add_sentence('I am hungry')

words_trie.insert_data(sentence_trie)


def test_check_frase_as_is():
    sentence = 'Alexander'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences == [('hello dear Alexander', 18), ('Alexander is great student', 18)]

def test_check_frase_as_is_2():
    sentence = 'Alexander is'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences == [('Alexander is great student', 24)]

def test_check_frase_as_is_3():
    sentence = 'Alex'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences == [('hello dear Alexander', 8), ('Alexander is great student', 8)]

def test_check_frase_as_is_4():
    sentence = 'Alexander if'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'Alexander is great student'

def test_check_frase_as_is_5():
    sentence = 'hello word'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'hello world'

def test_check_frase_as_is_6():
    sentence_trie = SentenceTrie()
    words_trie = Trie()
    sentence_trie.add_sentence('hello world')
    sentence_trie.add_sentence('hello worlb')
    words_trie.insert_data(sentence_trie)
    sentence = 'hello worlp'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'hello worlb'
    assert final_sentences[1][0] == 'hello world'

def test_check_frase_as_is_7():
    sentence_trie = SentenceTrie()
    words_trie = Trie()
    sentence_trie.add_sentence('hello world')
    sentence_trie.add_sentence('hello worlb')
    words_trie.insert_data(sentence_trie)
    sentence = 'hello worl'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'hello world'
    assert final_sentences[1][0] == 'hello worlb'


def test_check_frase_as_is_2_1():
    sentence = 'Alex ander is'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'Alexander is great student'


def test_check_frase_as_is_2_2():
    sentence = 'Alexwnder is'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'Alexander is great student'

def test_check_frase_as_is_2_3():
    sentence = 'Alex'
    final_sentences = check_frase_as_is(sentence, sentence_trie, words_trie)
    assert final_sentences[0][0] == 'hello dear Alexander'





