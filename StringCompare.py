class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        else:
            count = 0
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    count += 1
            if count > 2:
                return False
            else:
                C = ""
                for j in range(0, len(A)-1):
                    if A[j] != B[j] and j != len(A)-1:
                        C += A[j+1]
                        C += A[j]

                    else:
                        C += A[j]
                if B == C:
                    return True
                else:
                    return False


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
