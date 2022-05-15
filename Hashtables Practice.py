class Hashtable:

    def __init__(self, size):
        self.list_size = size
        self.list = []
        for i in range(self.list_size):
            self.list.append(None)

    def hash_table_func(self, str_list):
        for i in str_list:
            str_int = int(i)
            index = str_int
            while self.list[index] is not None:
                index = index + 1
                index = index % self.list_size
            self.list[index] = i

    def func_key(self, key):
        index = int(key) % self.list_size
        while self.list[index] is not None:
            if self.list[index] == key:
                print(f"Value {key} found in Index {index}")
                return index
            else:
                index = index + 1
                index = index % self.list_size

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 and num % 3 == 0:
            return False
        k = 5 # x = 6(y) +/- 1
              # x * x = k -> it's not prime
        while k*k <= num:
            if num % k == 0 or num % (k+2) == 0:
                return False
            else:
                k = k + 6
        return True

    def nearest_prime(self, min_size):
        prime_size = min_size
        while not self.is_prime(prime_size):
             prime_size = prime_size + 1

        return prime_size

    def increase_size(self):
        self.list_size = self.nearest_prime(self.list_size)


    def fill_list_with_none(self):
        for i in range(self.list_size):
            self.list.append(None)

    def
