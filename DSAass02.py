
#1. Binary search

pos = -1

def search(list, n):
    l = 0
    u = len(list) -1

    while l <= u:
        mid = (u + l) //2
        if list[mid] == n:
            globals()['pos'] = mid

            return True
        
        else:
            if list[mid] < n:
                l = mid

            else:
                u = mid

    return False


list = [1,2,3,4,5,6]
n = 4

if search(list, n):
    print("element found at", pos + 1)

else:
    print("not found")



#2. Merge sort

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2
    left_half = array[:middle_index]
    right_half = array[middle_index:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []

    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            result.append(left_half[0])
            left_half = left_half[1:]
        else:
            result.append(right_half[0])
            right_half = right_half[1:]

    result += left_half
    result += right_half

    return result

array = [7,2,4,1,3,5,8,6]
sorted_array = merge_sort(array)
print(sorted_array)



#3.Quick sort

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left_array = []
    right_array = []
    equal_array = []

    for element in array:
        if element < pivot:
            left_array.append(element)
        elif element > pivot:
            right_array.append(element)
        else:
            equal_array.append(element)

    return quick_sort(left_array) + equal_array + quick_sort(right_array)




array = [6,2,4,1,8,9,5,7,3]
sorted_array = quick_sort(array)
print(sorted_array)



#4. Insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[i]:
            arr[j+1] = arr[j]

            j -= 1
            arr[j+1] = key


arr = [2,4,11,64,8,33,2]
insertion_sort(arr)
print(arr)



#5. Sorted strings


str = ['apple', 'money', 'mango', 'cat', 'hippo', 'zeebra']

sorted_str = sorted(str, key=lambda x: x.lower())

print(sorted_str)

