import stopwatch

# Base UnionFind algorithm, no optimizations
class UnionFindBase(object):
    def __init__(self, N):
        self._id = list(range(N))
        self._count = N

    def find(self, p):
        id = self._id
        return id[p]
    
    def count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        id = self._id
        pid = id[p]
        qid = id[q]

        for i in range(len(id)):
            if id[i] == pid:
                id[i] = qid
    def print_id(self):
        id = self._id
        print(id)


if __name__ == "__main__":
    from timeit import Timer
    def testUF():
        N = 500
        uf = UnionFindBase(N)















    while True:
        try:
            p, q = [int(x) for x in raw_input().split()]
            uf.union(p, q)
        except:
            break

    print(str(uf.count()) + " components: " + str(uf))
    print(str(uf.print_id()))
