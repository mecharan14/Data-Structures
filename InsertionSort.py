class Insertion:
    @staticmethod
    def sort(arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

arr = [5,9,7,4,3]
print("Before sorting: ",arr)
print("After sorting: ",Insertion.sort(arr))