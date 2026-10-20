class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        curr_num = 0
        curr_str = ""

        for char in s:
            # deal with mutli-digit numbers properly e.g. 12 or 130
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            elif char == '[':
                # if we reached a opening bracket we append to the stack and reset 
                stack.append((curr_num, curr_str))
                curr_num = 0
                curr_str = ""

            elif char == ']':
                num, prev_str = stack.pop()

                curr_str = prev_str + (curr_str * num)

            else:
                curr_str += char
        
        return curr_str 
