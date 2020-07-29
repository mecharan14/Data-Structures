class Binary:
    def __init__(self, arr):
        self.arr = arr
    def search(self, val, low, high):
        mid = round((low+high)/2)
        if low == high and self.arr[mid] != val:
            return -1
        if self.arr[mid] == val:
            return mid
        elif self.arr[mid] < val:
            return self.search(val, mid, high)
        elif self.arr[mid] > val:
            return self.search(val, low, mid)

obj = Binary([4, 8, 12, 16, 20])
searchValue = 20
result = obj.search(searchValue, 0, len(obj.arr)-1)
if result == -1:
    print("Element not found.")
else:
    print("Element found at {} position.".format(result+1))