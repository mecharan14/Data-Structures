class Bubble:
    def __init__(self, arr):
        self.arr = arr
    def sort(self, option = 0):
        n = len(self.arr)
        for i in range(n):
            swaps = 0
            for j in range(n-i-1):
                cond = (self.arr[j] > self.arr[j+1]) if option == 0 else (self.arr[j] < self.arr[j+1])
                if cond:
                    tmp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = tmp
                    swaps += 1
            if swaps == 0:
                break
        print("\nSorted in {} passes.\n".format(i))
    def printAll(self):
        print(self.arr)

arr = Bubble([5,1,4,2,8])
print("Beforing sorting: ", end="")
arr.printAll()
arr.sort(0) # 0 for ascending and 1 for descending
print("After sorting: ", end="")
arr.printAll()
