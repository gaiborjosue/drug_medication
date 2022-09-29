class Solution:
    def solve(self, num):
        sums = 0
        for i in str(num):
            sums += int(i)
        return sums