class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num >= 0:
            
            sr = int(math.sqrt(num))
            # sqrt function returns floating value so we have to convert it into integer
            #return boolean T/F
            return ((sr*sr) == num)
        return false