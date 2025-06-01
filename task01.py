import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

# Вбудований Timsort
def builtin_sort(arr):
    return sorted(arr)

# Тестування та замір часу
def benchmark():
    sizes = [100, 500, 1000, 5000, 10000]
    print(f"{'Size':>10} | {'Merge Sort':>12} | {'Insertion Sort':>15} | {'Timsort':>10}")
    print("-" * 55)

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        merge_time = timeit.timeit(lambda: merge_sort(data[:]), number=1)
        insertion_time = timeit.timeit(lambda: insertion_sort(data[:]), number=1)
        builtin_time = timeit.timeit(lambda: builtin_sort(data[:]), number=1)

        print(f"{size:>10} | {merge_time:>12.6f} | {insertion_time:>15.6f} | {builtin_time:>10.6f}")

if __name__ == "__main__":
    benchmark()