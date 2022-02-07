# Disjoing set

## Implementation 

```Python
class UnionFind:
    # Constructor of Union-find. The size is the length of the root array.
    def __init__(self, size):
    def find(self, x):
    def union(self, x, y):
    def connected(self, x, y):
```

```Python
def find(self, x):
    while x != self.root[x]:
        x = self.root[x]
    return x
```

```Python
def find(self, x):
    if x == self.root[x]:
        return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]
```

```Python
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        self.root[rootY] = rootX
```

```Python
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
```

```Python
def connected(self, x, y):
    return self.find(x) == self.find(y)
```
