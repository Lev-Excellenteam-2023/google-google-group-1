from src.words_trie import Trie
from src.Sentence_trie import SentenceTrie
from src.full_search import check_frase_as_is
from src.getData import init_trees

sentence_trie = SentenceTrie()
words_trie = Trie()
#sentence_trie.add_sentence('hello world')
#sentence_trie.add_sentence('hello dear Alexander')
#sentence_trie.add_sentence('dear Yehuda Shani')
#sentence_trie.add_sentence('Alexander is greate student')
#sentence_trie.add_sentence('Alexander is not calm')
#sentence_trie.add_sentence('i ignore him')
#words_trie.insert_data(sentence_trie)


def run(sentence_trie, words_trie):
    print('Loading the files and preparing the system...')
    sentence_trie, words_trie = init_trees(sentence_trie, words_trie)
    print('The system is ready. Enter your text, ("close" to close the system):')
    text = input("")
    buffer = ""
    while text != 'close':
        buffer += text
        # using regex( findall() )
        # to extract words from string
        # res = re.findall(r'\w+', buffer)
        # res = [x.lower() for x in res]
        # my_input = " ".join(res)
        if buffer:
            suggestions = check_frase_as_is(buffer, sentence_trie, words_trie)
            print('Here are 5 suggestions: ')
            i = 0
            for suggestion in suggestions:
                i += 1
                print((str(i)) + ": " + str(suggestion))
            text = input(buffer)
            if text and text[-1] == '#':
                buffer = ""
                text = input("Enter your text: ")
        else:
            text = input(buffer)
    print('System closed')


if __name__ == '__main__':
    run(sentence_trie, words_trie)
