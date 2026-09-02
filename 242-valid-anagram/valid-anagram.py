class Solution(object):
    def isAnagram(self, s, t):
       if len(s) != len(t):
            return False
       hash_table1 = [0]*26
       hash_table2 = [0]*26

       for ch in s:
            hash_table1[ord(ch)- ord("a")] += 1
       for ch in t:
            hash_table2[ord(ch)- ord("a")] += 1
       return hash_table1 == hash_table2

        