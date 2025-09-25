print(abs(6))
print(abs(-8))

print(all([1, 2, 3, 4, 5]))
print(all([0, 1, 2, 3]))
print(all([]))

print("---any---")
print(any([1,2,3,0]))
print(any([0, ""]))
print(any([]))

print(chr(200))

print(dir([1,2,3]))
print(dir({'1':'a'}))

print(divmod(7, 3))

for i, name in enumerate(['asia', 'europe', 'affreca']):
    print(i, name)

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, -2, 0, -5, 6]))

def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, -2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, 2, 3, 4, 5])))