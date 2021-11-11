L = [1, 2, 3, 4, 5, 'abc', 'b', [10, -1]]
print(L, type(L))
print(L[0], L[-1][0])
print(L[5][1])
# print(L[100])
print(len(L))
# print([1, 2] >= ['a', 2])
print(1 in L)
print([1, 2, 3]+['a','b', 'c'])
print([0] * 10)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])
L.append(10)
print(L)
print(L.pop(1))
print(L)

# 1, 2, 4, 3, 2, 7, 10
# посчитать сумму чисел
data = input().split(', ')
print(data)
print(type(data))

data = list(map(int, data))

print(data)
print(sum(data))

data = list(map(int, input().split(', ')))
print(sum(data))

# 1.2; 3.5; 4.9
# Посчитать:
# 1. количество элементов
# 2. сумму элементов


print('; '.join(['1.1', '2.3', '4.5']))
print('1.1' + '; ' + '2.3' + '; ' + '4.5')
# print(';'.join([1, 2, 3, 4, 5]))
print('+'.join('abcdef'))

