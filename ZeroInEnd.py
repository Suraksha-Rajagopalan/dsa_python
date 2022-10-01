class Solution:
  def moveZeros(self, nums):
    # Fill this in.
    count = 0
    n = []
    for i in range(0, len(nums)):
        if nums[i]==0:
            count+=1
        else:
            n.append(nums[i])
    for j in range(count):
        n.append(0)
    print(n)

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
