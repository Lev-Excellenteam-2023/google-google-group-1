class SentenceNode:
    def _init_(self, word, father, children=None):
        self.word = word
        self.father = father
        self.children = children or []

class SentenceTrie:
    def _init_(self):
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

    def get_node_from_word(self, word):
        node = self.root
        for char in word:
            for child in node.children:
                if child.word.startswith(char):
                    node = child
                    break
            else:
                return None
        return node

    def complete_sentence(self, node):
        sentence = []
        while node.father:
            sentence.append(node.word)
            node = node.father
        sentence.reverse()
        return ' '.join(sentence)