class Linear:
    def __init__(self, arr):
        self.arr = arr
    def search(self, val):
        index = -1
        for i in range(len(self.arr)):
            if self.arr[i] == val:
                index = i
        return index

arr = Linear([4, 5, 8, 9, 6])
searchValue = 4
result = arr.search(searchValue)

if result == -1:
    print("Element not found.")
else:
    print("Element found at {} position.".format(result+1))