class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # so we have queryIndicies which tells us which character in string s will be updated
        # and thne the ith query is what character we will update the string s[queryIndicies[i]] with in queryCharacters[i]
        # the issue is that we have to update the character and then do a pass to count the longest substring of s with only one charcter after the ith query is performed
        # if we did this naively, this wouldbe something along the lines of like two linear scans for n query, one to change the letter and one to keep track of the longest count, which would be extremely inefficient
        # We have to use a segment tree, however there is a chance that a run of a longest substring can cross the boundary betwee two child segments

        #e.g "aaabb" | "bbccc" the longestis actually bbbb when we combine it 

        # for every node, we store:
        # left_char, right_char, prefix, sufix, best, and length

        n = len(s)

        tree = [None] * (4*n) 

        def merge(left, right):
            # unpack the two child summaries:
            l_char, l_right, l_prefix, l_suffix, l_best, l_len = left
            r_char, r_left, r_prefix, r_suffix, r_best, r_len = right

            # combined segment boundaries
            left_char = l_char
            right_char = r_char

            # default, prefix comes from left child
            prefix = l_prefix

            # suffix comes from right child
            suffix = r_suffix

            # best run might be insideon child
            best = max(l_best, r_best)

            # if boundary characters match, a repeating run can cross the middle and be the largest
            if l_right == r_left:
                best = max(best, l_suffix+r_prefix)

                # if the entire left segment is the same character, its prefix can continue into the right segment

                if l_prefix == l_len:
                    prefix = l_len + r_prefix

                # same for the right
                if r_suffix == r_len:
                    suffix = r_len + l_suffix

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                l_len + r_len
            )


        def build(node, left, right):

            # leaf = one char
            if left == right:
                char = s[left]

                tree[node] = (
                    char, # left char
                    char, # right char
                    1,    # prefix
                    1,    # suffix
                    1,    # best
                    1.    # length
                )

            return 

        mid = (left + right) // 2

        build(node * 2, left, mid)
        build(node * 2 + 1, mid + 1, right)

        tree[node] = merge(
            tree[node*2],
            tree[node*2+1]
        )

        def update(node, left, right, index, char):

            # reached character being changed:
            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return
            mid = (left + right) // 2

        # figure out which half contains the index
        if index <= mid:
            update(
                node * 2,
                left,
                mid,
                index,
                char
            )
        else:
            update(
                node*2+1,
                mid+1,
                right,
                index,
                char
            )
        tree[node] = merge(
            tree[node * 2],
            tree[node* 2 + 1]
        )
        # build from original string
        build(1, 0, n -1)
        res = []

        # perform each update
        for index, char in zip(queryIndices, queryCharacters):
            update(
                1,
                0,
                n-1,
                index,
                char
            )

            # root represents the entire string, index 4 of our tuple is the "best"
            res.append(tree[1][4])

    return res
