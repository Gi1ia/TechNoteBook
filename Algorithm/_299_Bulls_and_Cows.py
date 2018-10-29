"""
    Example 1:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
    
    Example 2:
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        l = len(secret)
        numA = 0
        numB = 0
        bulls = [False for x in range(l)]
        # cows = [False for x in range(l)]
        other = []
        secretDigt = {}
        
        for i in range(l):
            if secret[i] == guess[i]:
                bulls[i] = True
                numA += 1
            else:
                if secret[i] not in secretDigt:
                    secretDigt[secret[i]] = 1
                else:
                    secretDigt[secret[i]] += 1
        
        for i in range(l):
            if bulls[i] is False:
                if guess[i] in secretDigt and secretDigt[guess[i]] > 0:
                    numB += 1
                    secretDigt[guess[i]] -= 1
        
        
        return str(numA) + 'A' + str(numB) + 'B'