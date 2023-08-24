# take all txt files from dir

import src.Sentence_trie
import src.words_trie
import logging
import glob

ROOT_DIR = r'/Texts'


logging.basicConfig(level=logging.INFO)


def get_txt_files() -> list[str]:
    # Returns a list of names in list files.
    return glob.glob(ROOT_DIR + '/**/*.txt', recursive=True)


def read_lines(path: str, sentenceTrie: src.Sentence_trie):
    with open(path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
            sentenceTrie.add_sentence(line.strip())
            #   print(count, ": ", line.strip())
            # logging.info(f"line{count}: {line}")


def init_trees(sentenceTrie: src.Sentence_trie, wordsTrie: src.words_trie) -> (src.Sentence_trie, src.words_trie):
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
            if counter == 20:
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
