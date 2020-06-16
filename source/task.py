dict = {1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand'}


def count_letter(letter):
    count = 0
    for i in str(letter):
        if i != ' ' and i != '-':
            count += 1
    return count


def result(numb, dict):
    number = str(numb)
    if dict.get(numb, False):
        return dict.get(numb)
    elif numb == 1000:
         return dict[1000]
    elif numb < 100:
        n = numb - int(number[1])
        return dict[n] + _u(1, number)
    elif numb < 1000:
        if number[1:3] == '00':
            return _u(0, number) + _u(100)
        else:
            return _u(0, number) + ' hundred and ' + result(int(number[1:3]), dict)


def _u(numb, value=None):
    if value is not None:
        return dict[int(value[numb])]
    else:
        return dict[int(numb)]


word = 0

# def relation(numb):
#     if count_letter(numb) in range(1, 9):
#         return dict.get(numb)
#     if count_letter(numb) == 2:
#         numb = str(numb)
#         if numb[0] == 1:
#             return dict.get(numb)
#         if numb[0] == 2:
#             d = str(numb)
#             return dict[int(d[1])]

for item in range(1, 1001):
    word += count_letter(result(item, dict))
    print(result(item, dict))
    print(word)