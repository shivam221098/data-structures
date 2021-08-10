class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hash_ = 0
        for char in key:
            hash_ += ord(char)
        # print(hash % self.MAX)
        return hash_ % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]


if __name__ == '__main__':
    val = HashTable()
    val.add("7-march", 2358)
    val.add("8-march", 1258)
    val.add("7-april", 2874)
    val.add("23-may", 8965)

    print(val.get("8-march"))
