from encryption import encrypt, decrypt
from compression import compress, decompress, convert_to_binary, convert_to_compressed
from error import CRC


class CustomString:
    def __init__(self) -> None:
        self.crc = CRC()

    def pack(self, word: str) -> str:
        encrypted = encrypt(word)
        compressed = compress(encrypted)
        binary = convert_to_binary(compressed)
        return self.crc.encodeData(binary)

    def unpack(self, recieved: str) -> str:
        temp = self.crc.checkData(recieved)
        if (not temp[0]):
            raise UnicodeError("Corrupted Data Recieved")
        else:
            compressed = convert_to_compressed(temp[1])
            encrypted = decompress(compressed)
            return decrypt(encrypted)


if __name__ == "__main__":
    cs = CustomString()
    bit_stream = cs.pack("Hello World")
    recovered = cs.unpack(bit_stream)
    print(recovered)
