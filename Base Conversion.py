bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_base10_to_base_x(integer, base):
    add = base[integer%len(base)]
    if integer < len(base):
        return base[integer]
    else:
        return str(convert_base10_to_base_x(integer//len(base), base)) + add

def convert(input, source, target):
    source_base = len(source)
    index = len(input)-1
    number_in_base10 = 0
    while index >= 0:
        i = input[index]
        number_in_base10 += source.index(i)*(source_base**(len(input)-index-1))
        index -= 1
    return convert_base10_to_base_x(number_in_base10, target)