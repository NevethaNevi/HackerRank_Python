if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr_set = set(arr)
    arr = list(arr_set)
    arr.sort()
    print(arr[-2])
