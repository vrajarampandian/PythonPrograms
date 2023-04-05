#Anagram - a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
class Solution:
    #Time complexity O(n)
    #Space O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c],0)
            countT[t[c]] = 1 + countT.get(t[c],0)

        for i in countS:
            if countS[i] != countT.get(i,0):
                return False
        return True