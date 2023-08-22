# take all txt files from dir

import Sentence_trie
import words_trie
import logging
import glob

ROOT_DIR = r'/Users/alex/PycharmProjects/Google_project/Texts'


logging.basicConfig(level=logging.INFO)


def get_txt_files() -> list[str]:
    # Returns a list of names in list files.
    return glob.glob(ROOT_DIR + '/**/*.txt', recursive=True)


def read_lines(path: str, sentenceTrie: Sentence_trie):
    with open(path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
            sentenceTrie.add_sentence(line.strip())
            #   print(count, ": ", line.strip())
            # logging.info(f"line{count}: {line}")


def init_trees(sentenceTrie: Sentence_trie, wordsTrie: words_trie) -> (Sentence_trie, words_trie):
    files = None
    try:
        files = get_txt_files()
    except Exception as ex:
        print(ex)

    try:
       # print(files[2])
       #read_lines(files[2], sentenceTrie)

        counter = 0
        for file in files:
            counter += 1
            if counter == 3:
                break
            print(file)
            read_lines(file, sentenceTrie)
    except Exception as ex:
        print(ex)
    print("Sentences Done")

    try:
        wordsTrie.insert_data(sentenceTrie)
    except Exception as ex:
        print(ex)
    print("Words Done")
    return sentenceTrie, wordsTrie


if __name__ == "__main__":
    init_trees()
