class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer=[]
        int_value=int("".join(map(str,digits)))
        int_value+=1
        str_value=str(int_value)
        for index in str_value:
            answer.append(int(index))
        return answer