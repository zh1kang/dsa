class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # thoughts: 
        # since order matters we need to somehow keep track of the relative order of the words, I don't think we necessarily have to like delete something e.g. for ace as long as we know that pos[a] < pos[c] < pos[e], we are guaranteed to have "ace" as a subsequence because we can just delete whatever is inbetween them to get it
        #
        count = 0 

        for word in words:
            prev = -1
            is_subseq = True

            for char in word:
                pos = s.find(char, prev + 1)

                if pos == -1:
                    is_subseq = False
                    break

                prev = pos

            if is_subseq:
                count += 1

        return count 
        

# submission 2157712499 - 2026-09-30T03:26:19+00:00
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # thoughts: 
        # since order matters we need to somehow keep track of the relative order of the words, I don't think we necessarily have to like delete something e.g. for ace as long as we know that pos[a] < pos[c] < pos[e], we are guaranteed to have "ace" as a subsequence because we can just delete whatever is inbetween them to get it
        #
        count = 0 

        for word in words:
            prev = -1
            is_subseq = True

            for char in word:
                pos = s.find(char, prev + 1)

                if pos == -1:
                    is_subseq = False
                    break

                prev = pos

            if is_subseq:
                count += 1

        return count 
        

# submission 2157716531 - 2026-09-30T03:33:15+00:00
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # thoughts: 
        # since order matters we need to somehow keep track of the relative order of the words, I don't think we necessarily have to like delete something e.g. for ace as long as we know that pos[a] < pos[c] < pos[e], we are guaranteed to have "ace" as a subsequence because we can just delete whatever is inbetween them to get it
        #
        count = 0
        table = defaultdict(list)

        for word in words:
            table[word[0]].append(word)

        for char in s:
            # take out all words currently waiting for this char
            matches = table.pop(char, [])

            for word in matches:
                if len(word) == 1:
                    count += 1
                else:
                    # remove the matched character
                    remaining = word[1:]

                    # now this word waits for its next character
                    table[remaining[0]].append(remaining)

        return count