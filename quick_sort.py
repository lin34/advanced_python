

class sort():

    def quick_sort(arr, low, high):
        if low < high:
            pivot_location = partition(arr, low,high)
            quick_sort(arr, low, pivot_location)
            quick_sort(arr, pivot_location + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        leftwall = low

        for i in range(low + 1, high):
            if arr[i] < pivot:
                swap(arr[i], arr[leftwall])
                leftwall = leftwall + 1

        swap(pivot, arr[leftwall])

        return leftwall

    def swap(num1, num2):
        temp = num1
        num1 = num2
        num2 = temp

        
