class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kth_highest_scores = nums
        heapq.heapify(self.kth_highest_scores)

        # self.kth_highest_scoresという名のため、リストサイズをk個にした。
        while len(self.kth_highest_scores) > self.k:
            heapq.heappop(self.kth_highest_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.kth_highest_scores, val)
        while len(self.kth_highest_scores) > self.k:
            heapq.heappop(self.kth_highest_scores)
        return self.kth_highest_scores[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)