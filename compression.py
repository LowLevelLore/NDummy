
def compress(message: str) -> list[int]:
    table: dict[str, int] = {}

    for i in range(256):
        ch = ""
        ch += chr(i)
        table[ch] = i

    p: str = ""
    c: str = ""

    p += message[0]

    code: int = 256
    output_code: list[int] = []

    for i in range(len(message)):
        if (i != len(message) - 1):
            c += message[i+1]
        if (p+c) in list(table.keys()):
            p += c
        else:
            output_code.append(table[p])
            table[p+c] = code
            code += 1
            p = c
        c = ""

    output_code.append(table[p])
    return output_code


def convert_to_binary(compressed: list[int]) -> str:
    output = ""
    for code in compressed:
        b = bin(code).replace("0b", "")
        b = (16-len(b))*"0" + b
        output += b
    return output


def convert_to_compressed(binary: str) -> list[int]:
    output: list[int] = []
    i: int = 0
    while (i < (len(binary))):
        current = binary[i: i+16]
        output.append(int(current, 2))
        i += 16
    return output


def decompress(compressed: list[int]):
    table: dict[int, str] = {}
    for i in range(256):
        ch = ""
        ch += chr(i)
        table[i] = ch
    old: int = compressed[0]
    n: int = -1

    s: str = table[old]
    c: str = ""

    c += s[0]
    count = 256
    output = c
    for i in range(len(compressed) - 1):
        n = compressed[i + 1]
        if n not in list(table.keys()):
            s = table[old]
            s += c
        else:
            s = table[n]
        output += s
        c = ""
        c += s[0]
        table[count] = table[old] + c
        count += 1
        old = n
    return output


if __name__ == "__main__":
    messages = ["Hello World", "UwU", "It is what it is", "It's a test"]
    for msg in messages:
        compressed = compress(message=msg)
        binary = convert_to_binary(compressed=compressed)
        print(compressed)
        print(convert_to_compressed(binary))
        print(binary)
