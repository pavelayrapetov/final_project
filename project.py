# Написать программу, которая из имеющегося массива строк формирует массив строк, длина которых меньше либо равна 3 символа.
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

count = ['hello', '2', 'world', ':-)']
i = 3
a = count[0]
b = count[1]
c = count[2]
d = count[3]

if len(a) <= i:
    print(a)
if len(b) <= i:
    print(b)
if len(c) <= i:
    print(c)
if len(d) <= i:
    print(d)