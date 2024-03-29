def xor(x: str, y: str) -> str:
    """Get the XOR of two binary string

    Args:
        x (str): binary_string_1
        y (str): binary_string_2

    Returns:
        str: xor_result
    """
    res = ""
    for i in range(1, len(y)):
        if (x[i] == y[i]):
            res += '0'
        else:
            res += '1'
    return res


class CRC:
    def __init__(self, crc: str = "10000100"):
        """
            Initialize CRC polynomial
        Args:
            crc (str, optional): _description_. Defaults to "1011".
        """
        self.crc = crc

    def __getMod2Remainder(self, dividend: str):
        """Get remainder from the division of (number)/(crc)

        Args:
            dividend (str): The message encoded in binary

        Returns:
            str: The Remainder when we perform the division
        """
        divisor = self.crc
        start = len(divisor)
        temp_str = dividend[0:start]
        while (start < len(dividend)):
            if (temp_str[0] == '1'):
                # perform actual division algo
                temp_str = xor(divisor, temp_str) + dividend[start]
            else:
                # To provide padding
                temp_str = xor('0'*start, temp_str) + dividend[start]
            start += 1
        # for last (n bits) be perform division manually to avoid IndexOutOfBound
        if temp_str[0] == '1':
            temp_str = xor(divisor, temp_str)
        else:
            temp_str = xor("0"*start, temp_str)

        return temp_str

    def encodeData(self, message: str) -> str:
        """Encode the given binary message

        Args:
            message (str): message to send

        Returns:
            str: message encoded with CRC code
        """
        message += ("0"*(len(self.crc) - 1))
        remainder = self.__getMod2Remainder(message)
        return message[:-len(self.crc) + 1] + remainder

    def checkData(self, message: str) -> tuple[bool, str]:
        """Check if recieved message is correct

        Args:
            message (str): 

        Returns:
            bool: _description_
        """
        return (int(self.__getMod2Remainder(message)) == 0, message[:-len(self.crc) + 1])


if __name__ == "__main__":
    crc = CRC()
    msg = input("Enter binary message : ")
    print(len(msg))
    print(f"Encoded with CRC : {crc.encodeData(msg)}")
    if (crc.checkData(input("Enter Rercieved data : "))):
        print("Correct Packet recieved !")
    else:
        print("Corrupted Packet")
