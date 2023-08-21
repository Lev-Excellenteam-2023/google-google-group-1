from Sentence_trie import SentenceNode, SentenceTrie
from words_trie import TrieNode, Trie

PATH = '/Users/alex/PycharmProjects/Google_project/Data_to_tests.txt'

# Using readlines()
file1 = open(PATH, 'r')
Lines = file1.readlines()

sentenceTrie = SentenceTrie()

# Strips the newline character
for line in Lines:
    sentenceTrie.add_sentence(line)


def fill_wors_trie(sentence_trie: SentenceTrie, words_trie = Trie):
    if sentence_trie.root.word:

