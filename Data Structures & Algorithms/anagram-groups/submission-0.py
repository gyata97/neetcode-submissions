class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for s in st:
                count[ord(s) - ord('a')] += 1
            hmp[tuple(count)].append(st)

        return list(hmp.values())

        