class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1

        for idx, char in enumerate(s):
            if char == '(':
                start = idx 
            elif char == ')':
                ans.append(d.get(s[start + 1 : idx], "?"))
                start = -1
            
            elif start < 0: 
                ans.append(char)

        return "".join(ans)

            
        