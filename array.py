N_MAX = 15


def read_array():
    n = int(input("Enter number of elements: "))
    if n > N_MAX:
        print("Error: number of elements exceeds N_MAX =", N_MAX)
        n = N_MAX
    arr = []
    print("Enter elements:")
    i = 0
    while i < n:
        tmp = int(input(""))
        arr.append(tmp)
        i += 1
    return arr


def print_array(arr):
    print("Array:")
    i = 0
    while i < len(arr):
        print(arr[i], end=" ")
        i += 1
    print("")


if __name__ == "__main__":
    data = read_array()
    print_array(data)
