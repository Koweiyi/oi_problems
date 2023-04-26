n = int(input())
nums = [x for x in map(int, input().split())]

nums.sort()

last = 1
for j in range(1, n):
    if nums[j] != nums[j - 1]:
        nums[last] = nums[j]
        last += 1
print(last)
for x in nums[:last]:
    print(x, end=" ")