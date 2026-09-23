class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        group = 0
        start = 0 

        while i < len(chars):
            # if we are in the same group just keep incrementing i
            if chars[i] == chars[group]: 
                i += 1
            else:
                # since we found a diff letter the length of our group is the 
                # start of next group - prev group 
                length = i - group
                # override the chars in place
                chars[start] = chars[group]
                # increment so we can write our count
                start += 1
                # if length > 1 we append the digits after the char
                if length > 1:
                    for digit in str(length):
                        chars[start] = digit
                        start += 1
                # move pointer up to next group
                group = i 

        # process last group
        length = i - group
        chars[start] = chars[group]
        start += 1
        if length > 1:
            for digit in str(length):
                chars[start] = digit
                start += 1
        
        return start 





