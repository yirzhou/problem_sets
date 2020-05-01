class Solution:
    def permutation(self, string):
        memo = [[] for _ in range(len(string))]

        for index, char in enumerate(string):
            if index == 0: 
                memo[index] = [char]
                continue
            pre_sub_len = len(memo[index-1][0])
            for substr in memo[index-1]:
                for i in range(pre_sub_len):
                    memo[index].append(substr[0:i]+char+substr[i:pre_sub_len])
                memo[index].append(substr+char)
        return memo[len(string)-1]

print(Solution().permutation('abcd'));
