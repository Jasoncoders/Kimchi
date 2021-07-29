class Text:
    def __init__(self, value):
        self.value = value

    def isText(self):
        if str(type(self.value)) == "<class 'str'>":
            return True
        else:
            return False

class Number:
    
    value = 0
    
    def __init__(self, value):
        self.value = value

    def isNumber(self):
        if str(type(self.value)) == "<class 'float'>" or "<class 'int'>":
            return True
        else:
            return False

    def __sub__(self, other):
        if self.value < other.value:
            return other.value - self.value
        elif self.value > other.value:
            return self.value - other.value
        else:
            return 0

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value
        
    def __div__(self, other):
        if self.value < other.value:
            return other.value / self.value
        elif self.value > other.value:
            return self.value / other.value
        else:
            return 1

num1 = Number(12)
num2 = Number(4)

print(num1 - num2)