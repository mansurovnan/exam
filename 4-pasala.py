def words(a):
    for word in a.split():
        yield word
a = input('matnni kiriting:')

for word in words(a):
    print(word)
