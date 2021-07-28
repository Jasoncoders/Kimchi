class Text:
    def __init__(self, value):
        self.value = value
    
    def isText(self):
        if str(type(self.value)) == "<class 'str'>":
            return True
        else:
            return False

var = Text(123)
print(var.isText())