from re import I


class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    dictionary = {}
    string = ""
    for i in range(0, len(s)):
        print(i)
        if s[i] not in string:
            string += s[i]
        else:
            dictionary[len(string)] = string
            string = ""
    
    max_length = max(dictionary)
    print(dictionary)
    return max_length

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
