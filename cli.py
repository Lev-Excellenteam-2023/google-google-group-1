import re
from words_trie import Trie
from Sentence_trie import SentenceTrie
from full_search import check_frase_as_is

sentence_trie = SentenceTrie()
words_trie = Trie()
sentence_trie.add_sentence('hello world')
sentence_trie.add_sentence('hello dear Alexander')
sentence_trie.add_sentence('dear Yehuda Shani')
sentence_trie.add_sentence('alexander is greate student')
sentence_trie.add_sentence('alexander is not calm')
sentence_trie.add_sentence('i ignore him')
words_trie.insert_data(sentence_trie)



if __name__ == '__main__':
    print('Loading the files and preparing the system...')
    print('The system is ready. Enter your text, ("close" to close the system):')
    text = input("")
    buffer = ""
    while text != 'close':
        buffer += text
        # using regex( findall() )
        # to extract words from string
        res = re.findall(r'\w+', buffer)
        res = [x.lower() for x in res]
        my_input = " ".join(res)
        suggestions = check_frase_as_is(my_input, sentence_trie, words_trie)
        print('Here are 5 suggestions: ')
        for suggestion in suggestions:
            print(suggestion)
        text = input(buffer)
        if text[-1] == '#':
            buffer = ""
            text = input("Enter your text: ")
    print('System closed')
