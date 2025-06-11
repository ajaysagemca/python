print("code 1 palindrom")
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = int(str(x)[::-1])
        if rev == x:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121))



print()
print("code 2 twosum")
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, nums in enumerate(nums):
            complement = target - nums
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums] = i
        return []

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))



print()
print("code 3 roman to interger")
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        pre_value = 0
        for char in reversed(s):
            curr_value = roman_values[char]
            if curr_value < pre_value:
                total -= curr_value
            else:
                total += curr_value
            pre_value = curr_value
        return total


obj = Solution()
print(obj.romanToInt("III"))
print(obj.romanToInt("LVIII"))  # 58
print(obj.romanToInt("MCMXCIV"))



print()
print("code 4 find the index of the first occurence")
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            index = haystack.index(needle)
            return index
        except ValueError:
            index = -1
            return index

obj = Solution()
print(obj.strStr("sadbutsad", "sad"))
print(obj.strStr("leetcode", "leeto"))
print(obj.strStr("hello", "ll"))













