class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]]+=1
            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]]+=1
        slist = list(sdict.items())
        tlist = list(tdict.items())
        slist = sorted(slist)
        tlist = sorted(tlist)
        if slist==tlist:
            return True
        else:
            return False