from Sentence_trie import SentenceTrie, SentenceNode
import logging
import typing

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

        # aray of references of words in SentenceTrie
        self.sentenceTrieRef = []


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, sentenceNode: SentenceNode):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in sentenceNode.word:
            if char in node.children:
                logging.info('Node found with char: %s', char)
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                logging.info('Node created with char: %s', char)
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

        # add the node with word to the references
        node.sentenceTrieRef.append(sentenceNode)

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def get_references_from_word(self, word : str) -> typing.List[SentenceNode]:
        """Given a word, retrieve all references stored in
        the trie with that word, sort the words by the number of
        times they have been inserted
        """
        node = self.root

        # Check if the prefix is in the trie
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # return all references
        return node.sentenceTrieRef




if __name__ == '__main__':

    t = Trie()
    t.insert(SentenceNode("was", None))
    t.insert(SentenceNode("word", None))
    t.insert(SentenceNode("war", None))
    t.insert(SentenceNode("what", None))
    t.insert(SentenceNode("where", None))
    print(t.query("wh"))
#[('what', 1), ('where', 1)]
