import logging

logging.basicConfig(level=logging.INFO)

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

    def complete_sentence(self, node):
        sentence = []
        while node.father:
            sentence.append(node.word)
            node = node.father
        sentence.reverse()
        return ' '.join(sentence)


