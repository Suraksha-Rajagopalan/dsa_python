def findPythagoreanTriplets(nums):
    # Fill this in.
    for i in nums:
        for j in nums:
            if ((i**2) + (j**2))**0.5 in nums:
                return True
    return False
            
print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
