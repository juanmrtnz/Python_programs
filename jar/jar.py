class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self._size += n
        if self.size < 0 or self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self._size -= n
        if self.size < 0 or self.size > self.capacity:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(6)
    print(jar.capacity)
    print(jar.size)
    print(jar)


if __name__ == "__main__":
    main()
