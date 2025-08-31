dic = {
    'name': 'pey',
    'phone': '010-0000-0000',
    'birth': '1111'
}

print(dic)

dic[3] = 'happy'
print(dic)

del dic[3]
print(dic)

# 주의 사항
a = {
    1:'a',
    1:'b'
}

print(a)

print(dic.keys())
print(dic.values())

for k in dic.keys():
    print(k)

print(list(dic.keys()))

print(dic['name'])
print(dic.get('name1'))

# 해당 key가 있는지 조사하기
print('name' in dic)