class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for words in strs:
            freq = [0]*26
            for ch in words:
                freq[ord(ch)-ord("a")] += 1
            key = tuple(freq)
            groups[key].append(words)
        return groups.values()