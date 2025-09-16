while True:
    a = int(input("Введите первое число: "))
    sign = input("Введите знак (или off для выхода): ")
    if sign == "off":
        break
    b = int(input("Введите второе число: "))

    if sign == '+': print(a + b)
    elif sign == '-': print(a - b)
    elif sign == '*': print(a * b)
    elif sign == '/': print("Неверный ввод" if b == 0 else a / b)
    elif sign == '//': print("Неверный ввод" if b == 0 else a // b)
    elif sign == '%': print("Неверный ввод" if b == 0 else a % b)
    elif sign == '**': print(a ** b)

    elif sign == '==': print(a == b)
    elif sign == '!=': print(a != b)
    elif sign == '>': print(a > b)
    elif sign == '<': print(a < b)
    elif sign == '>=': print(a >= b)
    elif sign == '<=': print(a <= b)

    elif sign == 'and': print(a and b)
    elif sign == 'or': print(a or b)
    elif sign == 'not': print(not a)

    elif sign == '&': print(a & b)
    elif sign == '|': print(a | b)
    elif sign == '^': print(a ^ b)
    elif sign == '~': print(~a, ~b)
    elif sign == '<<': print(a << b)
    elif sign == '>>': print(a >> b)

    elif sign == 'in': print(a in [b])
    elif sign == 'not in': print(a not in [b])

    elif sign == 'is': print(a is b)
    elif sign == 'is not': print(a is not b)

    else:
        print("Неправильно ")