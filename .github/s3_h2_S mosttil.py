arz = float(input('arz ra vared konid : '))
tool = float(input('tool ra vared konid : '))
vahed = input('vahed ra vared konid : ')
def masahat(arz, tool, vahed) :
    vahed1 = 'metr'
    result1 = arz * tool
    if vahed == 'mm':
        result = result1 * 10 ** -3
    elif vahed == 'cm':
        result = result1 * 10 ** -2
    elif vahed == 'm':
        result = result1
    else :
        result = result1
        print('vaahed shoma esshtbeh ast va bsort pish faarz metr dar nazar grefte shod')
    print(f'masahat mostatil shoma ba vahed {vahed1} va masahat {result} mibashad')
masahat(arz, tool, vahed)


