class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Answer=[]
        Answer.append([1])
        for raw in range(numRows-1):
            temp_raw=[1]
            for cols in range(raw):
                temp_raw.append(Answer[raw][cols]+Answer[raw][cols+1])
            temp_raw.append(1)
            Answer.append(temp_raw)
        return Answer