class Solution:
    @lru_cache(None)
    def canIWin(self, mx, desiredTotal, bitMask = 0):
        
        if ((1+mx)*mx < 2*desiredTotal or 
            desiredTotal <= 0 and bitMask): return False

        for i in range(mx):
            if not (bitMask >> i) & 1:
                
                if not self.canIWin(mx, desiredTotal-i-1, (1<<i)|bitMask):
                        return True







