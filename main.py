
import csv
import random
import glob
from collections import OrderedDict


class TaruTaru:
    def __init__(self, finish_word: str, num_finish: int):
        self.finish_word = finish_word
        self.num_finish = num_finish
        self.max_try_count = 100000
        self.key_dict = {}
        self.word_dict = {}

    def open_csv(self):
        csv_paths = glob.glob('noun_csv/*.csv')
        count = 0
        for csv_path in csv_paths:
            with open(csv_path, encoding='EUC-JP') as f:
                reader = csv.reader(f)
                for row in reader:
                    name_kana = row[-1]
                    name = row[0]
                    self.key_dict[count] = name_kana
                    self.word_dict[name_kana] = name
                    count += 1

    def calc_tarutaru(self, begin_word: str):
        print(begin_word)
        begin_word_last_letter = begin_word[-1]
        self.open_csv()

        for num in range(1, self.num_finish+1):
            try_count = 0
            while try_count < self.max_try_count:
                try_count += 1
                name_kana = self.key_dict[random.choice(range(len(self.word_dict)))]
                name = self.word_dict[name_kana]
                first_letter = name_kana[0]
                last_letter = name_kana[-1]
                if num != self.num_finish:
                    if first_letter == begin_word_last_letter and last_letter != 'ン' and last_letter != 'ー' and last_letter != self.finish_word[0]:
                        print(f'{name_kana}({name})')
                        begin_word_last_letter = last_letter
                        # del self.word_dict[name_kana]
                        break
                else:
                    if first_letter == begin_word_last_letter and last_letter == self.finish_word[0]:
                        print(f'{name_kana}({name})')
                        print(self.finish_word)
                        return


if __name__ == "__main__":
    finish_word = 'タルタルチキン'
    begin_word = 'ゴマ'
    obj = TaruTaru(finish_word=finish_word, num_finish=2)
    obj.calc_tarutaru(begin_word)



