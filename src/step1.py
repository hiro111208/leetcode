# kth highestとあったのでheapqの使用を思いつく
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapqの初期化の仕方を忘れたため、ドキュメントを読む
        self.kth_highest_scores = nums
        heapq.heapify(self.kth_highest_scores)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.kth_highest_scores, val)
        while len(self.kth_highest_scores) > self.k:
            heapq.heappop(self.kth_highest_scores)
        return self.kth_highest_scores[0]

# 振り返り
# - min heap / max heapがあるのを何となく覚えていたが、heapq.heappopで最大値、最小値どちらがpopされるのか忘れていた。
# - heapqのドキュメントをしっかり読んでいなくて、heapq.nlargestがn番目に大きな値を返すのかと勘違いした。ドキュメントはしっかり読まなければと反省した。
# - 変数名の付け方について指摘される傾向があるので、そこは気をつけた。
# 初期化時、self.kth_highest_scoresと言っておきながら、k個以上値が入りそうなので、k個に減らすようpopしようと思う。

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)