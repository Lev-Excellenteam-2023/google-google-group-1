from src.Sentence_trie import SentenceTrie, complete_sentence

def test_complete_sentence_1():
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    assert complete_sentence(trie.root.children[0].children[0]) == 'hello world'

def test_complete_sentence_2():
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    trie.add_sentence('hello Alexander')
    assert complete_sentence(trie.root.children[0].children[0]) == 'hello world'
    assert complete_sentence(trie.root.children[0].children[1]) == 'hello Alexander'

def test_add_sentence_1():
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    assert trie.root.children[0].word == 'hello'
    assert trie.root.children[0].children[0].word == 'world'

def test_find_all_terminals_1():
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    trie.add_sentence('hello Alexander')
    trie.add_sentence('hello Omer')
    terminals = trie.find_all_terminals(trie.root)
    assert terminals[0].word == 'world'
    assert terminals[1].word == 'Alexander'
    assert terminals[2].word == 'Omer'

def test_find_all_nodes_1():
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    trie.add_sentence('hello Alexander')
    trie.add_sentence('hello Omer')
    nodes = trie.find_all_nodes(trie.root)
    assert nodes[0].word == 'hello'
    assert nodes[1].word == 'world'
    assert nodes[2].word == 'Alexander'
    assert nodes[3].word == 'Omer'

def test_find_terminals_and_sentence_1():
    # Checks from first node
    trie = SentenceTrie()
    trie.add_sentence('hello world')
    trie.add_sentence('hello Alexander')
    trie.add_sentence('hello Omer')
    terminals = trie.find_all_terminals(trie.root)
    sentences = [complete_sentence(terminal) for terminal in terminals]
    assert sentences == ['hello world', 'hello Alexander', 'hello Omer']

def test_find_terminals_and_sentence_2():
    # Checks from second node
    trie = SentenceTrie()
    trie.add_sentence('I am a student')
    trie.add_sentence('I am a teacher')
    trie.add_sentence('I am a programmer')
    node = trie.root.children[0].children[0] # node of 'am'
    terminals = trie.find_all_terminals(node)
    sentences = [complete_sentence(terminal) for terminal in terminals]
    assert sentences == ['I am a student', 'I am a teacher', 'I am a programmer']

def test_find_terminals_and_sentence_3():
    # Checks that we don't get sentences that start with the same node
    trie = SentenceTrie()
    trie.add_sentence('One two three')
    trie.add_sentence('One smart man')
    trie.add_sentence('One small step')
    node = trie.root.children[0].children[0] # node of 'two'
    terminals = trie.find_all_terminals(node)
    sentences = [complete_sentence(terminal) for terminal in terminals]
    assert sentences == ['One two three']





