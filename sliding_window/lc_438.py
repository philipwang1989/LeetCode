class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        ans = []
        
        pattern = [0] * 26
        ss = [0] * 26
        
        for ch in p:
            pattern[ord(ch)-ord("a")] += 1
            
        window = len(p)
        for i in range(window):
            ss[ord(s[i])-ord("a")] += 1
        
        if ss == pattern:
            ans.append(0)
        
        for i in range(window, len(s)):
            l = s[i-window]
            r = s[i]
            ss[ord(l)-ord("a")] -= 1
            ss[ord(r)-ord("a")] += 1
            if ss == pattern:
                ans.append(i-window+1)
                
        return ans
