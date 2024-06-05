class TwoSum:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """

        return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

        Brute force Solution: O(n2)
        Tim: Can we do better?
        Yes,
        time complexity: O(n).
            We traverse the list containing nnn elements only once.
            Each lookup in the table costs only O(1) time.

        Space complexity: O(n).
        The extra space required depends on the number of items stored in the hash table,
        which stores at most n elements.

        """
        num_dict = {}  # Search in a hash table is O(1) compared to O(n) in a list. Trade-off is space complexity

        for i in range(len(nums)):
            deficit = target - nums[i]
            if deficit in num_dict:  # O(1) search, removed the need for nested loop
                return [num_dict[deficit], i]
            num_dict[nums[i]] = i
