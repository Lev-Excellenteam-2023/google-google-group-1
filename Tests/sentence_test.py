import Sentence_trie

def test_complete_sentence_1():
    trie = Sentence_trie.SentenceTrie()
    trie.add_sentence('hello world')
    assert trie.complete_sentence(trie.root.children[0].children[0]) == 'hello world'


