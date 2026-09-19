class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            key=tuple(count)
            if key not in D:
                D[key]=[]
            D[key].append(i)
        ans=[]
        for i in D.values():
            ans.append(i)
        return ans