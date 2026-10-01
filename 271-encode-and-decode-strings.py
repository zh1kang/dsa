class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""

        for string in strs:
            encoded += f"{len(string)}#{string}"

        return encoded


        

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # to decode, we can use a pointer and go through and when we get to the length and delimiter we can just add it to our list
        decode_str = []
        i = 0

        while i < len(s):
            # we keep another pointer to find the delimiter
            j = i
            while s[j] != "#":
                j += 1      
            # extract the length
            length = int(s[i:j])

            # move our initial pointer past the delimiter
            i = j + 1

            decode_str.append(s[i : i + length])
        
            i += length

        return decode_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))