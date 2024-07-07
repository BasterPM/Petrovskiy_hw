class RealStr(str):
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError('The entered data is not a string')
        self.string = string

    def __eq__(self, other):
        if not isinstance(other, (str, RealStr)):
            raise TypeError('The operand on the right must be a string')

        line = other if isinstance(other, str) else other.string
        return len(self.string) == len(line)


# a = RealStr('asdf')
# b = RealStr('zxcv')
# print(a == b)
