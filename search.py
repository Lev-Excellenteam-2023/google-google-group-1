from Sentence_trie import SentenceTrie, complete_sentence, SentenceNode
from words_trie import Trie
from typing import List


def find_terminal_nodes_from_search(sentence: str, words_trie: Trie) -> List[SentenceNode]:
    """
    Receives a sentence and returns a list of all the possible completions
    :param sentence: str
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    words = sentence.split()
    references = words_trie.get_references_from_word(words[0])
    for word in words[1:]:
        children = []
        for reference in references:
            children += reference.children
        references = []
        for child in children:
            if child.word == word:
                references.append(child)

    return references

def autocomplete_no_mistakes(sentence: str, sentence_trie: SentenceTrie, words_trie: Trie) -> List[SentenceNode]:
    """
    Receives a sentence and returns a list of all the possible completions
    :param sentence: str
    :param sentence_trie: SentenceTrie object
    :param words_trie: Trie object
    :return: a list of all the possible completions
    """
    references = find_terminal_nodes_from_search(sentence, words_trie)
    terminal_nodes = []
    for reference in references:
        terminal_nodes += sentence_trie.find_all_terminals(reference)
    return terminal_nodes

def main():
    sentence_trie = SentenceTrie()
    sentence_trie.add_sentence('hello world')
    sentence_trie.add_sentence('hello word')
    words_trie = Trie()
    words_trie.insert_data(sentence_trie)
    nodes = autocomplete_no_mistakes('hello', sentence_trie, words_trie)
    for node in nodes:
        print(complete_sentence(node))

if __name__ == '__main__':
    main()






