class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas = [[1]]
        for i in range(numRows-1):
            temp = [0] + pas[i] + [0]
            row = []
            for j in range(len(pas[-1])+1):
                row.append(temp[j]+temp[j+1])
            pas.append(row)
        return pas
                