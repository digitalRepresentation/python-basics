try:
    5 / 0
except ZeroDivisionError as e:
    print(e)


try:
    a = [1, 2]
    print(a[3])
    5 / 0
# except ZeroDivisionError:
#     print("Zeroに分けられないです。")
#
# except IndexError:
#     print("indexingできません。")

# except ZeroDivisionError as e:
#     print(e)
#
# except IndexError as e:
#     print(e)

except (ZeroDivisionError, IndexError) as e:
    print(e)

# try:
#     age = int(input('年を入力してください。'))
# except:
#     print("数字ではございません。")
# else:
#     if age <= 18:
#         print('未成年者は禁止されております。')
#     else:
#         print('歓迎します。')

# try:
#     f = open("存在しないファイル", "r")
# except FileNotFoundError as e:
#     print("test")
#     print(e)

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def __init__(self):
        print("test")

eagle = Eagle()
eagle.fly()

