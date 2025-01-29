def find_minmax(arr):
    if not arr:
        raise ValueError("Array can't be empty")

    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] <= arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = find_minmax(arr[:mid])
    right_min, right_max = find_minmax(arr[mid:])

    current_min = left_min if left_min <= right_min else right_min
    current_max = left_max if left_max >= right_max else right_max

    return current_min, current_max


# Запуск тестів
if __name__ == "__main__":
    arr = [6, 3, 1, 7, 8, 2]
    min_val, max_val = find_minmax(arr)
    print(f"{arr}:")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")