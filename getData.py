# take all txt files from dir

import Sentence_trie
import words_trie
import logging
import glob

ROOT_DIR = r'C:\BootCamp2023\google_project\rpoject\Texts'

sentenceTrie = Sentence_trie.SentenceTrie()

logging.basicConfig(level=logging.INFO)


def get_txt_files() -> list[str]:
    # Returns a list of names in list files.
    return glob.glob(ROOT_DIR + '/**/*.txt', recursive=True)


def read_lines(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
            sentenceTrie.add_sentence(line.strip())
            #   print(count, ": ", line.strip())
            # logging.info(f"line{count}: {line}")


def main():
    files = None
    try:
        files = get_txt_files()
        print(files[2])
    except Exception as ex:
        print(ex)

    try:
        # print(files[2])
        #
        # read_lines(files[2])


        for file in files:
            print(file)
            read_lines(file)
    except Exception as ex:
        print(ex)
    print("Sentences Done")

    try:
        wordsTrie = words_trie.Trie()
        wordsTrie.insert_data(sentenceTrie)
    except Exception as ex:
        print(ex)
    print("Words Done")


if __name__ == "__main__":
    main()
