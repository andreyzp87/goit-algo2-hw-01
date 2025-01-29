def quick_select(arr, k):
    def split(start, end):
        pivot = arr[end]
        pos = start

        for i in range(start, end):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1

        arr[pos], arr[end] = arr[end], arr[pos]
        return pos

    left, right = 0, len(arr) - 1
    k = k - 1

    while left <= right:
        pivot_idx = split(left, right)
        if pivot_idx == k:
            return arr[k]
        elif pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1

    return None

if __name__ == "__main__":
    test_arr = [3, 6, 1, 5, 8, 4]
    k = 2
    result = quick_select(test_arr, k)
    print(f"{k}-th smallest element: {result}")