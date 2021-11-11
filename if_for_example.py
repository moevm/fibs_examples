x = int(input())
if -5 <= x <= 5:
    print(x, 'входит в интервал')
    if x > 0:
        print(x, 'Больше 0')
elif x > 5:
    print(x, 'Больше 5')
else:
    print(x, 'Меньше -5')

# На вход программе подается целое неотрицательное число. Необходимо вывести это число и слово "Апельсин" в правильной
# форме. Например: 2 апельсина, 10 апельсинов
# число, которое подается на вход должно быть в промежутке от 0 до 10 включительно.

x = int(input())
if 0 == x % 10:
    print(x, 'Апельсинов')
elif 1 == x % 10:
    print(x, 'Апельсин')
elif 2 <= x % 10 <= 4:
    print(x, 'Апельсина')
elif 5 <= x % 10 <= 10:
    print(x, 'Апельсинов')

L = [-1, 20, 13, 22, 67]

for element in L:
    if element % 2 == 0:
        print(element, '!')

for index in range(len(L)):
    if L[index] % 2 == 0:
        print(L[index], '!')

for index, element in enumerate(L):
    print(index, element)


# через запятую вводятся данные в виде
# имя возраст, имя возраст
# например: Мария 12, Иван 22, Федор 34
# Посчитать средний возраст
# Вычислить самое длинное имя

data = input().split(', ')
ages_sum = 0
k = 0

tmp = [1, 4, 7, -3, 10, 99]
tmp_max = tmp[0]
for element in tmp:
    if element > tmp_max:
        tmp_max = element
print(tmp_max)

len_name_max = 0
name_max = ''
for element in data:
    name, age = element.split() # можно написать person = element.split()
    # print(name) # person[0]
    # print(type(age)) # person[1]
    age = int(age)
    ages_sum += age
    k += 1
    len_name = len(name)
    if len_name >= len_name_max:
        len_name_max = len_name
        name_max = name

print(ages_sum / len(data))
print(name_max)
