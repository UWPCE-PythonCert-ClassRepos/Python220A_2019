
def catch(id = None):
    try:
        if id is None:
            raise TypeError
        print('dick')
    except TypeError:
        print('except worked')
        print(2+2+1)
    return 'shit'


print(catch(6))
