import math

def sign_str(x):
    if(x < 0):
        return '-'
    else:
        return '+'

def gcd(a,b):
    if a == 0 or b == 0:
        return a+b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

if __name__ == "__main__":
    x_i = [int(x) for x in input('x_i: ').split(' ')]
    f_i = [int(f) for f in input('f_i: ').split(' ')]
    assert(len(x_i) == len(f_i))
    print('Лагранж:')
    ups = []
    downs = []
    for k in range(len(x_i)):
        print('k = ', k, ':', sep='', end=' ')
        print('f_k = ', f_i[k],sep='', end=' ')
        up_str = ''
        down_str = ''
        up = [1]
        down = 1
        for i in range(len(x_i)):
            if(i == k):
                continue
            up_str += f'(x{sign_str(-x_i[i])}{abs(x_i[i])})'
            down_str += f'({x_i[k]}{sign_str(-x_i[i])}{abs(x_i[i])})'
            up.append(0)
            up = [1] + [up[j+1] - up[j]*x_i[i] for j in range(len(up) - 1)]
            down *= x_i[k] - x_i[i]
        print('Числитель: ', up_str, sep='', end=' ')
        print('Знаменатель: ', down_str, ' = ', down, sep='')
        print('Сокращаем коэффициенты: ', sep='', end=' ')
        coef = gcd(abs(down), abs(f_i[k]))
        down /= coef
        coef = f_i[k]/coef
        if down < 0 and coef < 0:
            down, coef = -down, - coef
        elif down * coef < 0:
            down, coef = abs(down),-abs(coef)
        up = [e*coef for e in up]
        up_str = ''
        for i in range(len(up)):
            up_str += f'{sign_str(up[i])}{abs(up[i])}*x^{len(up)-1-i}'
        print('Числитель: ', up_str, sep='', end=' ')
        print('Знаменатель: ', down, sep='')
        ups.append(up)
        downs.append(down)
    maximum = max(downs)
    print('Приводим к общему знаменателю: ', maximum, sep='')
    for k in range(len(downs)):
        print('Слагаемое ', k,  sep='', end=' ')
        coef = maximum/downs[k]
        print('Домножаем на ', coef, ':', sep='', end=' ')
        ups[k] = [e * coef for e in ups[k]]
        up_str = ''
        for i in range(len(ups[k])):
            up_str += f'{sign_str(ups[k][i])}{abs(ups[k][i])}*x^{len(ups[k]) - 1 - i}'
        print(up_str, sep='')
    poly = [sum(up[i] for up in ups)/maximum for i in range(len(ups[0]))]
    up_str = ''
    for i in range(len(poly)):
        up_str += f'{sign_str(poly[i])}{abs(poly[i])}*x^{len(poly) - 1 - i}'
    print('Многочлен по методу Лагранжа: ', up_str, sep='')
    print()
    print('Ньютон вперёд:')
    print('x_i:', x_i)
    print('delta_0_f_i:', f_i)
    delta_f_i = [f_i]
    for i in range(len(x_i)-1):
        delta_f_i.append([delta_f_i[i][j+1] - delta_f_i[i][j] for j in range(len(delta_f_i[i]) - 1)])
        print('delta_',i+1,'_f_i: ',delta_f_i[i+1], sep='')
    h = abs(x_i[0] - x_i[1])
    ups = []
    up = []
    up_str = ''
    for i in range(len(x_i)):
        print(f'Коэффициент слагаемого: {delta_f_i[i][0]}/({h**i} * {math.factorial(i)}) ', end='')
        coef = delta_f_i[i][0]/((h**i) * math.factorial(i))
        up.append(0)
        if len(up) > 1:
            up = [1] + [up[j+1] - up[j]*x_i[i-1] for j in range(len(up) - 1)]
            if(up_str == '1'):
                up_str = f'(x{sign_str(-x_i[i])}{abs(x_i[i])})'
            else:
                up_str += f'(x{sign_str(-x_i[i])}{abs(x_i[i])})'
        else:
            up = [1]
            up_str = '1'

        print('Слагаемое: ', up_str)
        ups.append([0 for j in range(len(x_i)-1-i)] + [e * coef for e in up])
    print('Слагаемые с коэффициентами:')
    for i in range(len(ups)):
        up_str = ''
        for j in range(len(ups[i])):
            up_str += f'{sign_str(ups[i][j])}{abs(ups[i][j])}*x^{len(ups[i]) - 1 - j}'
        print('Слагаемое ', i, ': ', up_str, sep='')
    poly = [sum(up[i] for up in ups) for i in range(len(ups[0]))]
    up_str = ''
    for i in range(len(poly)):
        up_str += f'{sign_str(poly[i])}{abs(poly[i])}*x^{len(poly) - 1 - i}'
    print('Многочлен по методу Ньютона вперёд: ', up_str, sep='')

    print()
    print('Ньютон назад:')
    print('x_i:', x_i)
    print('delta_0_f_i:', f_i)
    delta_f_i = [f_i]
    for i in range(len(x_i) - 1):
        delta_f_i.append([delta_f_i[i][j + 1] - delta_f_i[i][j] for j in range(len(delta_f_i[i]) - 1)])
        print('delta_', i + 1, '_f_i: ', delta_f_i[i + 1], sep='')
    h = abs(x_i[0] - x_i[1])
    ups = []
    up = []
    up_str = ''
    for i in range(len(x_i)):
        print(f'Коэффициент слагаемого: {delta_f_i[i][-1]}/({h ** i} * {math.factorial(i)}) ', end='')
        coef = delta_f_i[i][-1] / ((h ** i) * math.factorial(i))
        up.append(0)
        if len(up) > 1:
            up = [1] + [up[j + 1] - up[j] * x_i[-i] for j in range(len(up) - 1)]
            if(up_str == '1'):
                up_str = f'(x{sign_str(-x_i[-i])}{abs(x_i[-i])})'
            else:
                up_str += f'(x{sign_str(-x_i[-i])}{abs(x_i[-i])})'
        else:
            up = [1]
            up_str = '1'
        print('Слагаемое: ', up_str)
        ups.append([0 for j in range(len(x_i) - 1 - i)] + [e * coef for e in up])
    print('Слагаемые с коэффициентами:')
    for i in range(len(ups)):
        up_str = ''
        for j in range(len(ups[i])):
            up_str += f'{sign_str(ups[i][j])}{abs(ups[i][j])}*x^{len(ups[i]) - 1 - j}'
        print('Слагаемое ', i, ': ', up_str, sep='')
    poly = [sum(up[i] for up in ups) for i in range(len(ups[0]))]
    up_str = ''
    for i in range(len(poly)):
        up_str += f'{sign_str(poly[i])}{abs(poly[i])}*x^{len(poly) - 1 - i}'
    print('Многочлен по методу Ньютона назад: ', up_str, sep='')









