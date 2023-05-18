#1

class OddIterator:
    def __init__(self, n):
        if n < 1:
            raise ValueError("Неправильне значення N")
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration("Кінець ітерації")
        odd_number = self.current
        self.current += 2
        return odd_number
try:
    n = int(input("Введіть значення N: "))
    iterator = OddIterator(n)
    for number in iterator:
        print(number)
except ValueError as e:
    print("Помилка:", e)
except StopIteration as e:
    print("Кінець ітерації:", e)
