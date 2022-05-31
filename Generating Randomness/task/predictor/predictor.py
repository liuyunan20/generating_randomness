import re


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
for triad in triad_list:
    print(f'{triad}: {triad_dict[triad][0]},{triad_dict[triad][1]}')
