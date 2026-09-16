class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = sorted(set(nums))
        longest=1
        length=1
        if len(seen) <=1 :
            return len(seen)
        for i in range(1,len(seen)):
            if seen[i]-seen[i-1]==1:
                length+=1
            else:
                length=1
            longest=max(longest,length)

        return longest

        