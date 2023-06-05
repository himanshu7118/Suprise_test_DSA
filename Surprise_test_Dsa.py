# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1

# Ans:

def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            
        right += 1

    return nums
  
 
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.

# Ans: 
def firstUniqChar(s):
    char_freq = {}

    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    return -1

  


