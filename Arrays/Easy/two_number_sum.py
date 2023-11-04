array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    nums = {}

    for num in array:
        maybeMatch = targetSum - num
        if maybeMatch in nums:
            print(nums)
            return [maybeMatch, num]
        else:
            nums[num] = True
    return []

print(twoNumberSum(array, targetSum))