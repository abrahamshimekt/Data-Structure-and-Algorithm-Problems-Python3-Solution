"""
The problem is to partition a string as much as possible that each character only appears in
only one partition
s = "ababcbacadefegdehijhklij"
i = 0
j = 0

output = []
max = max(max,last_appearence[s[j]]) = 15
if max == j:
   output.append(j-i +1)
    j +=1
    i = j
    max = 0
else:
  j +=1
last_appearence = {a:8,b:5,c:7,d:14,e:15,f:11,g:12,h:19,i:22,j:23,l:21}
"""
from collections import Counter


def partitionLabels(s):
    output = []
    max_partition = 0
    last_appreance = {}
    for i in range(len(s)):
        if s[i] not in last_appreance:
            last_appreance[s[i]] = i
        else:
            last_appreance[s[i]] = i
    i = j = 0
    while j < len(s):
        max_partition = max(max_partition, last_appreance[s[j]])
        if max_partition == j:
            output.append(j - i + 1)
            j += 1
            i = j
            max_partition = 0
        else:
            j += 1
    return output


print(partitionLabels("ababcbacadefegdehijhklij"))
