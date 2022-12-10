from typing import List

n, m = map(int, input().split())

def CheckingValidness(group, validness) -> int:
    for i in group:
        if abs(i) <= 1000:
            validness += 1
    return validness

def Game(numbers, m) -> List[int]:
    count = 0
    boka = 0
    zhoka = 0
    tmpnum = 0
    max = -1000 * m

    while len(numbers) != 0:
        for num in range(m):
            tmpnums = numbers.copy()
            tmpnums = tmpnums[0:(num + 1)]

            if sum(tmpnums) > max:
                max = sum(tmpnums)
                tmpnum = num

        numbers = numbers[(tmpnum + 1)::]
        count += 1

        if count % 2 == 0:
            zhoka += max
        else:
            boka += max

        max = -1000 * m

    return [boka, zhoka]

if 4 <= n <= 50000 and 3 <= m <= 100:
    SumValidness = 0
    nums = list(map(int, input().split()))
    nums = nums[0:n]

    SumValidness = CheckingValidness(nums, SumValidness)

    if SumValidness == len(nums):

        if Game(nums, m)[1] >= Game(nums, m)[0]:
            print(0)
        else:
            print(1)