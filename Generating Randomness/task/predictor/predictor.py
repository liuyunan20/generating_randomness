import re
import random


class GenerateRandomness:
    def __init__(self):
        self.triad_list = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.triad_dict = {}
        self.data = ''
        self.balance = 1000

    def preprocess(self):
        print('''Please give AI some data to learn...
The current data length is 0, 100 symbols left''')
        while len(self.data) < 100:
            str_in = input('Print a random string containing 0 or 1:\n')
            for x in list(str_in):
                if x in ['0', '1']:
                    self.data += x
            if len(self.data) < 100:
                print(f'Current data length is {len(self.data)}, {100 - len(self.data)} symbols left')
        print(f'Final data string:\n{self.data}\n')
        self.learn(self.data)

    def learn(self, data):
        for x in self.triad_list:
            str_count = data
            for _ in range(len(data)-3):
                match = re.match(f'{x}.', str_count)
                str_count = str_count[1:]
                if match:
                    self.triad_dict.setdefault(x, [0, 0])
                    self.triad_dict[x][int(match.group()[-1])] += 1

    def check_symbol(self, symbols):
        for x in list(symbols):
            if x not in ['0', '1']:
                return False
        return True

    def play(self):
        print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')
        while True:
            str_test = input('Print a random string containing 0 or 1:\n')
            if str_test == 'enough':
                break
            if not self.check_symbol(str_test):
                continue

            str_predict = [random.choice(['0', '1']) for _ in range(3)]
            for x in range(len(str_test) - 3):
                symbol_0, symbol_1 = self.triad_dict[str_test[x: x+3]]
                if symbol_0 > symbol_1:
                    str_predict.append('0')
                if symbol_0 < symbol_1:
                    str_predict.append('1')
                if symbol_0 == symbol_1:
                    str_predict.append(random.choice(['0', '1']))
            print(f'prediction:\n{"".join(str_predict)}')
            # calculate the balance
            counter = 0
            for i, s in enumerate(list(str_test)[3:]):
                if s == str_predict[i+3]:
                    counter += 1
            print(f'Computer guessed right {counter} out of {len(str_predict) - 3} symbols ({round(counter*100/(len(str_predict)-3), 2)} %)')
            self.balance -= counter
            self.balance += len(str_predict) - 3 - counter
            print(f'Your balance is now ${self.balance}')
            self.learn(self.data[-3:] + str_test)
            self.data += str_test
        print('Game over!')


game = GenerateRandomness()
game.preprocess()
game.play()
