class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D={}
        for i in strs:
            temp="".join(sorted(i))
            if temp not in D:
                D[temp]=[i]
            else:
                D[temp].append(i)
        ans=[]
        for i in D.values():
            ans.append(i)
        return ans