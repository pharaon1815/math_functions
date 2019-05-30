# Error handling practice


def quotient():    # define quotient function
    response = input('Do you need help with division? (y/n): ')
    while response == 'y':    # loop to continue asking
        try:
            n = input('numerator: ')    # input numerator
            d = input('denominator: ')    # input denominator
            print(str(n) + '/' + str(d) + ' =', end=' ')
            print(int(n)/int(d))
            response = input('Do you need help with division? (y/n): ')
        except ZeroDivisionError:
            print('Error: I can\'t divide by 0')


quotient()  # calls the quotient function
