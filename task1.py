#  Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
num = int(input('Введите число: '))
dictionary = {}
for i in range(1, num+1):
    dictionary[i] = 3 * i + 1
    print(dictionary)