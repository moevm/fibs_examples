data = input().split(',')
summa = 0
names = []
for i, element in enumerate(data): # Мария 12, Иван 22, Федор 34
    name, age = element.split()
    names.append(name)
    age = int(age)
    summa += age
    name_max = 0
    if len(name) > name_max:
        name_max = len(name)
        idx = i
print(names[idx])
