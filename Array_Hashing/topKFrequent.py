#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

nums = [1,1,1,2,2,3]
k = 3
count = {}
freq = [[] for i in range(len(nums)+1)]

print(freq)
for n in nums:
    count[n] = 1 + count.get(n,0)
print(count)
for n, c in count.items():
    freq[c].append(n)

print(freq)
res = []
for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)
            break

nums = [1,1,1,2,2,3]

hmap = {}

for item in nums:
    if item in hmap:
        hmap[item] += 1

    else:
        hmap[item] = 1

hmap_sorted = sorted(hmap.items(), key=lambda x: x[1], reverse=True)

result = [hmap_sorted[i][0] for i in range(k)]

print(result)