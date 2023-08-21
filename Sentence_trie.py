import logging
import typing
import words_trie


class SentenceNode:
    def __init__(self, word, father, children=None):
        self.word = word
        self.father = father
        self.children = children or []
        # add logging that prints the word of the node
        logging.info('Node created with word: %s', self.word)

class SentenceTrie:
    def __init__(self):
        self.root = SentenceNode(None, None)

    def add_sentence(self, sentence):
        words = sentence.split()
        node = self.root
        for word in words:
            node = self.add_word(word, node)

    def add_word(self, word, father):
        for child in father.children:
            if child.word == word:
                return child
        node = SentenceNode(word, father)
        father.children.append(node)
        return node

    def complete_sentence(self, node : SentenceNode) -> typing.List[str]:
        sentence = []
        while node.father:
            sentence.append(node.word)
            node = node.father
        sentence.reverse()
        logging.info('Sentence completed: %s', ' '.join(sentence))
        return ' '.join(sentence)

    def find_all_terminals(self, node : SentenceNode) -> typing.List[SentenceNode]:
        if not node.children:
            return [node]
        terminals = []
        for child in node.children:
            terminals.extend(self.find_all_terminals(child))
        return terminals

    def find_all_nodes(self, node: SentenceNode) -> typing.List[SentenceNode]:
        if not node.children:
            return [node]
        nodes = [node]
        for child in node.children:
            nodes.extend(self.find_all_nodes(child))
        return nodes




