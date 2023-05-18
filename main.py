#4

def multiply_by(n):
    def zamik(x):
        return x * n
    return zamik

multiply_by_n = multiply_by(n = int(input("Введіть число:")))
result = multiply_by_n(int(input("Введіть кількість замиканнь:")))
print(result)

