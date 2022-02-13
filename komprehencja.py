data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)

data_2 = [ 1, 'jeden', 2, 'dwa', 3, 'trzy', 4, 'cztery']
words = []
for num in data_2:
    if isinstance(num, str):
        words.append(num)

data_3 = list('Cześć i dzięki za ryby.'.split())
title = []
for word in data_3:
    title.append(word.title())

print(evens)
print(words)
print(title)
