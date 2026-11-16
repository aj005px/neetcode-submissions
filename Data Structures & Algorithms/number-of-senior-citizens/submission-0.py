class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = []
        temp =""
        for i in details:
            temp = i[::-1]
            p = temp[2:4]
            ans.append(int(p[::-1]))
        count = 0
        for i in ans:
            if i>60:
                count+=1
        return count