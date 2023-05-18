# ітератор
lst = [1,2,3,4,5,6]
print(iter(lst))

class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [ 1,2,3,4,5]
my_iter = MyIterator(my_list)
for num in my_iter:
    print(num)

#генератор

def my_generator(data):
    for item in data:
        yield item

for num in my_generator(my_list):
    print(num)


#КАЛЬКУЛЯТОР

def calculator():
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mult(a,b):
        return a * b
    def div(a,b):
        if b != 0:
            return a / b
        else:
            raise ValueError("ПОМИЛКА")
    return add,sub,mult,div
add,sub,mult,div = calculator()
print(div(3,0))