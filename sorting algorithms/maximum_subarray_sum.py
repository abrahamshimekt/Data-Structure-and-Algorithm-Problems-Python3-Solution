i = 0
j = 1
nums = [4, 1, -4, 2, 6, 1, 0]
best = 0
sum_ = nums[0]
while i < len(nums) and j < len(nums):
    sum_ = sum(nums[i:j + 1])
    best = max(best, sum_)
    j += 1
    if j == len(nums):
        i += 1
        j = i + 1
print(best)
best = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        best = max(best, total)
print(best)

best = 0
total = 0
for i in range(len(nums)):
    total = max(nums[i], nums[i] + total)
    best = max(best, total)
print(best)

for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j + 1] = nums[j +1], nums[j]
print(nums)

nums = [3,4,5,1,2]
for i in range(len(nums)):
    nums[i] = bin(nums[i]).replace("0b","")
nums = [4,2,6,7,3,4,2]
book_keeping = [0]*(max(nums)+1)
for num in nums:
    book_keeping[num] +=1
nums = []
i = 0
while i <len(book_keeping):
    if book_keeping[i] == 0:
        i +=1
    elif book_keeping[i] > 0:
        nums.append(i)
        book_keeping[i] -= 1

print(nums)

s = "ardahjkj"
i = 0
j = len(s)-1
new_s = list(s)
dict_vowels = {"a":1,"e":2,"i":3,"o":4,"u":5}
while i < len(s):
    if new_s[i] not in dict_vowels:
        i +=1
    if new_s[j] not in dict_vowels:
        j -=1
    if j < i:
        break
    else:
        new_s[i],new_s[j] = new_s[j],new_s[i]
        i +=1
        j -=1
print("".join(new_s))


