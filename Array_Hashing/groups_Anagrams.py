#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)
for s in strs:
    count = [0]*26 #a..z
    for c in s:
        count[ord(c)-ord("a")] += 1
    res[tuple(count)].append(s)
print(res.values())

def get_value():
    return "Not Present"

testdict = defaultdict(get_value)
testdict["1"] = "ram"
#print(testdict)
#print(testdict["3"])