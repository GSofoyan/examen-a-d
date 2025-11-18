class Heap:
    def __init__(self):
        self.lst =[]

    def __str__(self):
        return str(self.lst)

    def add(self,e):
        self.lst.append(e)
        current = e
        cur_index = len(self.lst)-1
        while cur_index>0 and current > self.lst[(cur_index-1)//2]:
            self.lst[cur_index],self.lst[(cur_index-1)//2] = self.lst[(cur_index-1)//2], self.lst[cur_index]
            cur_index = (cur_index-1)//2


x = Heap()
x.add(1)
x.add(7)
x.add(2)
x.add(3)
x.add(8)
x.add(9)
x.add(2)
x.add(88)
x.add(5)
print(x)
