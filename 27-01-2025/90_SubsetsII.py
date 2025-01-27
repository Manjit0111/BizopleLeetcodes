class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[[]]
        seen=set()
        for index1 in nums:
            tmp_answer=[]
            for index2 in answer:
                sum=index2+[index1]
                if tuple(sum) not in seen:
                    tmp_answer.append(sum) 
                    seen.add(tuple(sum))
            answer+=tmp_answer
        return answer
