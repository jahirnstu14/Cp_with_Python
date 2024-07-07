class DisjointSet:
    def __init__(self):
        self.parent = {}

    def make_set(self, v):
        self.parent[v] = v

    def find_set(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            self.parent[b] = a

# Example usage:
ds = DisjointSet()
ds.make_set(1)
ds.make_set(2)
ds.make_set(3)

print(ds.find_set(1))  # Output: 1
print(ds.find_set(2))  # Output: 2

ds.union_sets(1, 2)
print(ds.find_set(1))  # Output: 1
print(ds.find_set(2))  # Output: 1

ds.union_sets(2, 3)
print(ds.find_set(3))  # Output: 1
