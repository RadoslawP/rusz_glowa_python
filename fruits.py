fruits = {}

fruits['jabłka'] = 10
print(fruits)

if 'banany'in fruits:
    fruits['banany'] += 1
else:
    fruits['banany'] = 1
print(fruits)

fruits.setdefault('gruszki', 0)
print(fruits)

fruits['gruszki'] += 1

print(fruits)
