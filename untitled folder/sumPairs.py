
def sumPairs(nums, desiredSum):
    """
    nums = list[int]
    sum = int
    """
    dict1 = {}
    count = 0
    for item in nums:

        dict1[item] = count
        count = count + 1

    for i in range(0, len(nums) - 1):

        if dict1[desiredSum - nums[i]] != i:

            return [nums[i], desiredSum]
        else:
            return False


def zeroSum(nums):
    """

    """
    temp = nums
    listOfTriples = []
    for item in temp:

         tempSum = -temp[0]

         x =  sumPairs(temp,tempSum)
         if not x:
             x = x + [temp[0]]
             temp.remove(temp[0])

             listOfTriples.append(x)






x = range(-50,100)

zeroSum(x)
