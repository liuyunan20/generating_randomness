data = ''
while len(data) < 100:
    str_in = input('Print a random string containing 0 or 1:\n')
    for x in list(str_in):
        if x in ['0', '1']:
            data += x
    print(f'Current data length is {len(data)}, {20 - len(data)} symbols left')
print('Final data string:')
print(data)
