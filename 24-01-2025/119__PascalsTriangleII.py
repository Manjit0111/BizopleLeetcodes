class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        Answer=[]
        Answer.append([1])
        for raw in range(rowIndex):
            temp_raw=[1]
            for cols in range(raw):
                temp_raw.append(Answer[raw][cols]+Answer[raw][cols+1])
            temp_raw.append(1)
            Answer.append(temp_raw)
        return Answer[rowIndex]
        