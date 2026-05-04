def twoSum(nums, target):
    """
    Finds two indices in nums that add up to target.
    
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    # Create a hash map to store: value -> index
    prevMap = {} 
    
    for i, n in enumerate(nums):
        diff = target - n
        # If the complement (diff) is already in the map, we found our pair
        if diff in prevMap:
            return [prevMap[diff], i]
        
        # Otherwise, store the current number and its index
        prevMap[n] = i
    
    # Per constraints, a solution always exists, so we don't need a fallback.
    return []
