from encryption import encrypt, decrypt
from compression import compress, decompress, convert_to_binary, convert_to_compressed
from error import CRC


class CustomString:
    def __init__(self) -> None:
        self.crc = CRC()

    def pack(self, word: str) -> str:
        print("[PACKING] : " + word)
        encrypted = encrypt(word)
        print("[PACKING]\tENCRYPTED : " + encrypted)
        compressed = compress(encrypted)
        print("[PACKING]\tCOMPRESSED : " + str(compressed))
        binary = convert_to_binary(compressed)
        print("[PACKING]\tBINARY : " + binary)
        encoded = self.crc.encodeData(binary)
        print("[PACKING]\tENCODED : " + encoded)
        return encoded

    def unpack(self, recieved: str) -> str:
        print("[UNPACKING] : " + recieved)
        temp = self.crc.checkData(recieved)
        if (not temp[0]):
            raise UnicodeError("Corrupted Data Recieved")
        else:
            print("[UNPACKING]\tERROR CHECKING : Correct Data Recieved")
            compressed = convert_to_compressed(temp[1])
            print("[UNPACKING]\tUNCOMPRESSING : " + temp[1])
            encrypted = decompress(compressed)
            print("[UNPACKING]\tDECOMPRESSED : " + encrypted)
            print("[UNPACKING]\tDECRYPTED : " + decrypt(encrypted))
            return decrypt(encrypted)


if __name__ == "__main__":
    cs = CustomString()
    bit_stream = cs.pack("Hello World")
    recovered = cs.unpack(bit_stream)
    print(recovered)
