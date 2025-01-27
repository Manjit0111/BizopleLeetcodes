class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listDic=defaultdict(list)
        for value in strs:
            key="".join(sorted(value))
            listDic[key].append(value)
        return list(listDic.values())
        