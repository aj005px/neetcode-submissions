class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = []
        temp= {}
        counts = Counter(nums)
        for i in counts:
            temp[i] = counts[i]
        temp = sorted(temp.items(),key=lambda x: x[1],reverse=True)
        i=0
        while k!=0:
            sol.append(temp[i][0])
            i=i+1
            k=k-1
        return sol