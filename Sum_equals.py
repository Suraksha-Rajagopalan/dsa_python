def two_sum(list, k):
  # Fill this in.
    for i in list:
        for j in list:
            if (i + j) == k:
                return True
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
