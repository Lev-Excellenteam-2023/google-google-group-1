import Sentence_trie

def test_complete_sentence_1():
    trie = Sentence_trie.SentenceTrie()
    trie.add_sentence('hello world')
    node = trie.get_node_from_word('world')
    assert trie.complete_sentence(node) == 'hello world'

