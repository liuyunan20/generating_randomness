import re
import random


data = ''
while len(data) < 100:
    str_in = input('Print a random string containing 0 or 1:\n')
    for x in list(str_in):
        if x in ['0', '1']:
            data += x
    if len(data) < 100:
        print(f'Current data length is {len(data)}, {100 - len(data)} symbols left')
print(f'Final data string:\n{data}\n')
# print(data)
triad_list = ['000', '001', '010', '011', '100', '101', '110', '111']
triad_dict = {}

for x in triad_list:
    str_count = data
    for _ in range(len(data)-3):
        match = re.match(f'{x}.', str_count)
        str_count = str_count[1:]
        if match:
            triad_dict.setdefault(x, [0, 0])
            triad_dict[x][int(match.group()[-1])] += 1

str_test = input('Please enter a test string containing 0 or 1:\n')
str_predict = [random.choice(['0', '1']) for _ in range(3)]
for x in range(len(str_test) - 3):
    symbol_0, symbol_1 = triad_dict[str_test[x: x+3]]
    if symbol_0 > symbol_1:
        str_predict.append('0')
    if symbol_0 < symbol_1:
        str_predict.append('1')
    if symbol_0 == symbol_1:
        str_predict.append(random.choice(['0', '1']))
print(f'prediction:\n{"".join(str_predict)}')

counter = 0
for i, s in enumerate(list(str_test)[3:]):
    if s == str_predict[i+3]:
        counter += 1
print(f'Computer guessed right {counter} out of {len(str_predict) - 3} symbols ({round(counter*100/(len(str_predict)-3), 2)} %)')
