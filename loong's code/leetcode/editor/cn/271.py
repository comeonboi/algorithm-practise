class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        List = []
        for i in strs:
            for j in i:
                if j == ' ':
                    List.append('\t')
                else:
                    List.append(j)
            List.append('\n')
        List = ''.join(List)
        return List

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        List = []
        Str = ''
        for i in s:
            if i == '\t':
                Str = ''.join([Str, ' '])
            else:
                if i != '\n':
                    Str = ''.join([Str, i])
                else:
                    List.append(Str)
                    Str = ''
        return List


print(Codec.encode(Codec, strs=['\n\n', '\n 蚌\n']))
print(Codec.decode(Codec, Codec.encode(Codec, strs=['\n\n', '\n \n'])))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
