N_MAX = 15


def read_array():
    n = int(input("Enter number of elements: "))
    while n < 0 or n > N_MAX:
        print("Invalid size, expected 0..", N_MAX)
        n = int(input("Enter number of elements: "))
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


def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total


if __name__ == "__main__":
    data = read_array()
    print_array(data)
    print("Sum:", sum_array(data))
