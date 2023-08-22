from words_trie import Trie
from Sentence_trie import SentenceTrie

if __name__ == '__main__':
    PATH = '../Data_to_tests.txt'

    # Using readlines()
    file1 = open(PATH, 'r')
    Lines = file1.readlines()

    sentenceTrie = SentenceTrie()

    # Strips the newline character
    for line in Lines:
        sentenceTrie.add_sentence(line)

    t = Trie()
    t.insert_data(sentenceTrie)
    print(t.query("H"))