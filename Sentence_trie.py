import logging
import typing


class SentenceNode:
    def __init__(self, word, father, children=None):
        self.word = word
        self.father = father
        self.children = children or []
        # add logging that prints the word of the node
        logging.info('Node created with word: %s', self.word)



def complete_sentence(node: SentenceNode) -> str:
    """
    Receives a terminal node and returns the sentence by going up the tree
    :param node: SentenceNode object - the terminal node
    :return: str - the sentence
    """
    sentence = []
    while node.father:
        sentence.append(node.word)
        node = node.father
    sentence.reverse()
    logging.info('Sentence completed: %s', ' '.join(sentence))
    return ' '.join(sentence)


class SentenceTrie:
    def __init__(self):
        self.root = SentenceNode(None, None)

    def add_sentence(self, sentence: str) -> None:
        """
        Adds a sentence to the trie
        :param sentence: str
        :return: None
        """
        words = sentence.split()
        node = self.root
        for word in words:
            node = self.add_word(word, node)

    def add_word(self, word: str, father: SentenceNode) -> SentenceNode:
        """
        Adds a word to the trie, called only by add_sentence
        :param word: the current word in the sentence
        :param father: the father node of the current word
        :return: the node of the current word
        """
        for child in father.children:
            if child.word == word:
                return child
        node = SentenceNode(word, father)
        father.children.append(node)
        return node

    def find_all_terminals(self, node: SentenceNode) -> typing.List[SentenceNode]:
        """
        Finds all the terminal nodes of a node, called when there is a need to use function complete_sentence, that receives
        a terminal node as a parameter and returns the sentence
        :param node: SentenceNode object - the node to find all the terminals from it
        :return: a list of all the terminal nodes
        """
        if not node.children:
            return [node]
        terminals = []
        for child in node.children:
            terminals.extend(self.find_all_terminals(child))
        return terminals

    def find_all_nodes(self, node: SentenceNode) -> typing.List[SentenceNode]:
        """
        Finds all the nodes of a node, called when there is a need to build words_trie
        :param node: root node of the sentence trie
        :return: a list of all the nodes
        """
        if not node.children:
            return [node]
        nodes = [node] if node.word else []
        for child in node.children:
            nodes.extend(self.find_all_nodes(child))
        return nodes

    def get_children(self):
        return self.root.children










