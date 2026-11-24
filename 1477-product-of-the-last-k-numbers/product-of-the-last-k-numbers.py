class ProductOfNumbers:
    #prefix_array[i] = product of first i elements
    #prefix_array[-1] // prefix_array[n - 1 - k] = product of last k element 
    def __init__(self):
        self.prefix_array = [1]
        self.zero = SortedSet()

    def add(self, num: int) -> None:
        if num > 0:
            self.prefix_array.append(self.prefix_array[-1] * num)
        else:
            self.prefix_array.append(self.prefix_array[-1])
            self.zero.add(len(self.prefix_array) - 1)
        

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_array)
        haveZero = True if self.zero.bisect_left(n - k) < len(self.zero) else False
        return 0 if haveZero else self.prefix_array[-1] // self.prefix_array[n - k - 1] 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)