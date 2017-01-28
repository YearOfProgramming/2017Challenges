from collections import Counter

singlenumber = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
cnt = Counter() #initialize Counter from collections

for i in singlenumber: #count words in list
    cnt[i] += 1

for i in singlenumber:
    if cnt[i] == 1:
        print(singlenumber[i])

