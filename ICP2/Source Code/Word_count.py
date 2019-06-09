from collections import Counter
from pathlib import Path


def main():
    input_folder_path = Path("txtfiles/input_file.txt")
    ouput_folder_path = Path("txtfiles/output_file.txt")
    file = open(input_folder_path, "r", encoding="utf-8-sig")
    wordcount = Counter(file.read().split())
    f = open(ouput_folder_path, "w")
    for item in wordcount.items():
        f.write("{}\t{}\n".format(*item))


if __name__ == "__main__":
    main()
