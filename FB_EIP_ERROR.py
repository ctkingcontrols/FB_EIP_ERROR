

max = 300


with open('output.txt', 'w') as f:
    for index, val in enumerate(range(max+1)):
        f.write(f'IO_1799_CARD_IN[{val}].State <> 0 OR')
        f.write('\n')


