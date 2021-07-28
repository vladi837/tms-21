# Conversion constants
INCH_2_CENTIMETRE = 2.54
MILES_2_KILOMETERS = 1.609344
POUNDS_2_KILOGRAMS = 0.45359237
OUNCE_2_GRAMS = (POUNDS_2_KILOGRAMS * 1000.0) / 16.0
GRAMS_2_OUNCE = 16.0 / (POUNDS_2_KILOGRAMS * 1000.0)
GALLON_2_LITRES = 4.54609
LITRES_2_GALLON = 0.21997
PINTS_2_LITRES = 0.473176473
LITRES_2_PINTS = 2.11337641


def unit_conv(_val, _f):
    """ Unit conversion func """
    return list(map(_f, _val))  #


def main_func():
    """ Test function """
    line = ''
    while line != '0':  # Use cycle input
        # printing menu
        line = print_menu()
        if line == '0' or not line.isdigit():  # Check
            continue
        try:
            value = list(map(lambda x: float(x), input('Enter value:').split(' ')))
            print(value)
            if line == '1':
                print('Convert inch 2 centimetre',
                      unit_conv(value, lambda x: x * INCH_2_CENTIMETRE))  # 1inch = 2.54cm
            elif line == '2':
                print('Convert centimetre 2 inch',
                      unit_conv(value, lambda x: x / INCH_2_CENTIMETRE))  # 2.54cm = 1inch
            elif line == '3':
                print('Convert miles 2 kilometers',
                      unit_conv(value, lambda x: x * MILES_2_KILOMETERS))  # 1mi = 1.6km
            elif line == '4':
                print('Convert kilometers 2 miles',
                      unit_conv(value, lambda x: x / MILES_2_KILOMETERS))  # 1.6km = 1mi
            elif line == '5':
                print('Convert pounds 2 kilograms',
                      unit_conv(value, lambda x: x * POUNDS_2_KILOGRAMS))  # 1pound = 0.45kg
            elif line == '6':
                print('Convert kilograms 2 pounds',
                      unit_conv(value, lambda x: x / POUNDS_2_KILOGRAMS))  # 0.45kg = 1pound
            elif line == '7':
                print('Convert ounce 2 grams',
                      unit_conv(value, lambda x: x * OUNCE_2_GRAMS))  # 1un = 453g/16
            elif line == '8':
                print('Convert grams 2  ounce ',
                      unit_conv(value, lambda x: x * GRAMS_2_OUNCE))  # 1g = 16/453g
            elif line == '9':
                print('Convert Gallon 2 litres',
                      unit_conv(value, lambda x: x * GALLON_2_LITRES))  # 1gal = 4.5lit
            elif line == '10':
                print('Convert Litres 2 gallon',
                      unit_conv(value, lambda x: x * LITRES_2_GALLON))  # 1lit = 0.2gal
            elif line == '11':
                print('Convert Pints 2 litres',
                      unit_conv(value, lambda x: x * PINTS_2_LITRES))  # 1pint = 0.47lit
            elif line == '12':
                print('Convert Litres 2 pints',
                      unit_conv(value, lambda x: x * LITRES_2_PINTS))  # 1lit = 2.11pint
        except ValueError as inst:
            print(inst)


def print_menu():
    print('0 - Exit app')
    print('1 - Inch 2 centimetre')
    print('2 - Centimetre 2 Inch')
    print('3 - Miles 2 kilometers')
    print('4 - Kilometers 2 miles')
    print('5 - Pounds 2 kilograms')
    print('6 - Kilograms 2 pounds')
    print('7 - Ounce 2 grams')
    print('8 - Grams 2 ounce')
    print('9 - Gallon 2 litres')
    print('10 -Litres 2 gallons')
    print('11 -Pints 2 litres')
    print('12 -Litres 2 pints')
    line = input('Make choice:')  # Use choose from keyboard
    return line
    if name == 'main':
        main_func()