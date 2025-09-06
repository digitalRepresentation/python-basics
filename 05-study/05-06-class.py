# result = 0
#
# def add(num):
#     global result
#     result += num
#     return result
#
# print(add(3))
# print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(4))


class FourCal:
    def __init__(self):
        self.result = 0
        self.num1 = 0
        self.num2 = 0

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1 / self.num2

forucal1 = FourCal()
forucal1.setdata(4,2)
print(forucal1.add())
print(forucal1.mul())
print(forucal1.sub())
print(forucal1.div())
print(forucal1.num1)

print ('')

class MoreFourCal(FourCal):
    def __init__(self):
        super().__init__()

    def pow(self):
        result = self.num1 ** self.num2
        return result

morefourcal1 = MoreFourCal()
morefourcal1.setdata(5,3)
print(morefourcal1.add())
print(morefourcal1.pow())