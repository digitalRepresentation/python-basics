a = [1, 2, 3, 4]
while a:
    print(a.pop())

print(bool('python')) # true
print(bool(set([]))) # false
print(bool({})) # false
print(bool('')) # false
print(bool("")) # false
print(bool(' ')) # true
print(bool(" ")) # true
print(bool(None)) #false

x = 5
y = 10
print("-----------")
print(x > 0 and y > 0)
print(x > 10 or y > 5)
print(not (x > y))