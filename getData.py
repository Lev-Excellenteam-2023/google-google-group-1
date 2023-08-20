# take all txt files from dir

import Sentence_trie
import logging
import glob
ROOT_DIR = r'C:\BootCamp2023\google_project\rpoject\Texts'

sentenceTrie = Sentence_trie.SentenceTrie()


def get_txt_files() -> list[str]:
    # Returns a list of names in list files.
    return glob.glob(ROOT_DIR + '**/*.txt', recursive=True)


def read_lines(path: str):
    with open(path, 'r') as file:
        count = 0
        for line in file:
            count += 1
            sentenceTrie.add_sentence(line.strip())
            logging.info(f"line{count}: {line}")


def main():
    files = get_txt_files()
    read_lines(files[0])


if __name__ == "__main__":
    main()
