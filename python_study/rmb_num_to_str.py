"""
This is demonstration for converting number to rmb
"""


def divide(num):
    integer = int(num)
    fraction = round((num - integer) * 100)
    print("num = %s, integer = %d, fraction = %d" % (num, integer, fraction))
    return str(integer), str(fraction)


divide(123.45678)

hanzi_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
integer_unit_list = ['十', '百', '千']
fraction_unit_list = ['分', '角']

print('hanzi_list', hanzi_list, sep='=')
print('unit_list', integer_unit_list, sep='=')


def four_num_to_hanzi_str(four_num_str):
    result = ''
    length = len(four_num_str)
    for i in range(length):
        num = int(four_num_str[i])
        if i != length - 1 and num != 0:
            result += hanzi_list[num] + integer_unit_list[length - 2 - i]
            print(result)
        else:
            result += hanzi_list[num]
            print(result)
    return result


print(four_num_to_hanzi_str(str(1235)))


def two_fraction_to_hanzi_str(two_fraction_str):
    result = ''
    length = len(two_fraction_str)
    for i in range(length):
        num = int(two_fraction_str[i])
        result += hanzi_list[num] + fraction_unit_list[length - 1 - i]
    print(result)
    return result


print(two_fraction_to_hanzi_str(str(12)))


# todo handle zero -> '壹百贰十零万零零零零'
def whole_integer_to_hanzi_str(num_str):
    length = len(num_str)
    if length > 12:
        print('num length > 12')
        return
    elif length > 8:
        return four_num_to_hanzi_str(num_str[:-8]) + "亿" + \
               four_num_to_hanzi_str(num_str[-8: -4]) + "万" + \
               four_num_to_hanzi_str(num_str[-4:])
    elif length > 4:
        return four_num_to_hanzi_str(num_str[:-4]) + "万" + \
               four_num_to_hanzi_str(num_str[-4:])
    else:
        return four_num_to_hanzi_str(num_str)


num = float(input('Please input float: '))
integer, fraction = divide(num)
print(whole_integer_to_hanzi_str(integer) + '元' + two_fraction_to_hanzi_str(fraction))