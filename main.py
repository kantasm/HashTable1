class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()

    t['mar 6'] = 130
    t['mar 9'] = 200
    t['mar 10'] = 250
    t['dec 1'] = 200

    print(t['mar 6'])

    print(t.get_hash('march 6'))
    print(t.get_hash('mar 6'))

    del t['mar 6']

    print(t['mar 6'])