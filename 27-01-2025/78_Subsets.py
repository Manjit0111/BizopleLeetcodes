class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[[]]
        for index1 in nums:
            tmp_answer=[]
            for index2 in answer:
                sum=index2+[index1]
                tmp_answer.append(sum) 
            answer+=tmp_answer
        return answer