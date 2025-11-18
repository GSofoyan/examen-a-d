def zoek(gesorteerd: list, x: int):
    high = len(gesorteerd) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if gesorteerd[mid] == x:
            return mid
        elif gesorteerd[mid] < x:
            low = mid + 1
        elif gesorteerd[mid] > x:
            high = mid - 1

    return None