from math import ceil, floor, sqrt
import numpy as np

def encrypt(s: str):
    l = len(s)
    cols = ceil(sqrt(l))
    rows = floor(sqrt(l))
    encrypted = ""
    if (rows * rows < l):
        if (min(rows, cols) == rows):
            rows = rows + 1
        else:
            cols = cols + 1

    arr = [[' ' for i in range(cols)] for j in range(rows)]
    k = 0

    for i in range(rows):
        for j in range(cols):
            if (k < l):
                arr[i][j] = s[k]
            k += 1

    arr = np.array(arr)
    arr = list(map(list, list(arr.transpose())))

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            encrypted += arr[i][j]

    return encrypted


def decrypt(s: str):
    l = len(s)
    b = ceil(sqrt(l))
    a = floor(sqrt(l))
    decrypted = ""

    arr = [[' ' for i in range(a)] for j in range(b)]
    k = 0

    for j in range(b):
        for i in range(a):
            if (k < l):
                arr[j][i] = s[k]
            k += 1
    for j in range(a):
        for i in range(b):
            decrypted = decrypted + arr[i][j]
    return decrypted


if __name__ == "__main__":
    print(decrypt(encrypt("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s")))
