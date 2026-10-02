class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_map={}
        l=0
        max_window_size=0
        for r in range(len(s)):
            freq_map[s[r]]=freq_map.get(s[r],0)+1
            while len(freq_map)!=r-l+1:
                freq_map[s[l]]-=1
                if freq_map[s[l]]==0:
                    del freq_map[s[l]]
                l+=1
            max_window_size=max(max_window_size,r-l+1)
        return max_window_size
            

        