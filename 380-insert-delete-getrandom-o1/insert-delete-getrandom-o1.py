class RandomizedSet:

    def __init__(self):
        #array end pointer
        self.size = 0
        self.lst = []
        self.num_map = {}
        

        

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        else:
            self.num_map[val] = self.size
            self.lst.append(val)
            self.size += 1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.num_map:
            pos = self.num_map[val]
            del self.num_map[val]
            #replace hole with end elem
            if self.lst[self.size - 1] != val:
                rep = self.lst[self.size - 1]
                self.lst[pos] = rep
                self.num_map[rep] = pos
            
            self.lst.pop()
            self.size -= 1
            return True
        else:
            return False

            
        

    def getRandom(self) -> int:
        ran_pos = random.randint(0, self.size - 1)
        return self.lst[ran_pos]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()